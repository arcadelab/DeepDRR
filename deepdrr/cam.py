from __future__ import annotations
from operator import truediv

from typing import Union, Tuple, Iterable, List, Optional, Any

import numpy as np
from pathlib import Path
import logging

from .geo import HomogeneousObject, FrameTransform, Point2D, Point3D, Vector2D, Vector3D


def generate_uniform_angles(
    phi_range: Tuple[float, float, float],
    theta_range: Tuple[float, float, float],
    degrees: bool = True,
) -> Tuple[np.ndarray, np.ndarray]:
    """Generate a uniform sampling of angles over the given ranges

    Args:
        phi_range (Tuple[float, float, float]): range of angles phi in (min, max, step) form, in degrees.
        theta_range (Tuple[float, float, float]): range of angles theta in (min, max, step) form, in degrees.

    Returns:
        Tuple[np.ndarray, np.ndarray]: phis, thetas over uniform angles, in radians.
    """
    if not degrees:
        raise NotImplementedError
    
    min_theta, max_theta, spacing_theta = theta_range
    min_phi, max_phi, spacing_phi = phi_range
    thetas = np.array(np.arange(min_theta, max_theta + spacing_theta / 2, step=spacing_theta)) / 180 * np.pi
    num_thetas = len(thetas)
    phis = np.array(np.arange(min_phi, max_phi, step=spacing_phi)) / 180 * np.pi
    num_phis = len(phis)
    thetas = np.tile(thetas, num_phis)
    phis = phis.repeat(num_thetas, 0)
    return phis, thetas


def load_projections(
    path: str,
    lim: int = 100000000,
) -> List[CamProjection]:
    """Load all the projections saved in the directory at `path`

    Args:
        path (str): path to the directory containing R.txt, T.txt, and K.txt.
        lim (int, optional): Limits number of projections to read. Defaults to 100000000.

    Returns:
        List[CamProjection]: list of the projections
    """
    root = Path(path)
    Rs = np.loadtxt(root / 'R.txt', max_rows=lim)[:, 0:9].reshape(-1, 3, 3)
    Ks = np.loadtxt(root / 'K.txt', max_rows=lim)[:, 0:3]
    ts = np.loadtxt(root / 'T.txt', max_rows=lim)[:, 0:9].reshape(-1, 3, 3)
    return [CamProjection(R, K, t) for R, K, t in zip(Rs, Ks, ts)]



class Camera(object):
    """Contains all the info you need about the camera and its projections."""

    def __init__(
        self,
        intrinsic_matrix: np.ndarray,
        pixel_size: Union[int, Tuple[int, int]],
        isocenter_distance: float = 1000,
    ) -> None:
        """Generate the camera object.

        Args:
            intrinsic_matrix (np.ndarray): the camera intrinsic matrix K.
            pixel_size (Union[float, Tuple[float, float]]): (width, height) of a pixel, or a single value for both.
            isocenter_distance (float): distance to the isocenter in mm. Usually about 1000.
                The isocenter is the point through which the central ray of the radiation beams passes.
        """
        self.K = intrinsic_matrix
        self.pixel_size = pixel_size
        self.isocenter_distance = isocenter_distance

        self.sensor_size = (int(np.ceil(2 * self.K[0, 2])), int(np.ceil(2 * self.K[1, 2])))
        self.source_to_detector_distance = int(self.K[0, 0] * self.pixel_size[0])

    def __str__(self):
        return f"Camera(intrinsic_matrix = {np.array_str(self.K)}, isocenter_distance = {self.isocenter_distance})"

    @classmethod
    def from_intrinsic_matrix(cls, intrinsic_matrix: np.ndarray) -> Camera:
        return cls(intrinsic_matrix)

    @classmethod
    def from_parameters(
        cls, 
        sensor_size: Union[int, Tuple[int, int]],
        pixel_size: Union[int, Tuple[int, int]],
        source_to_detector_distance: int,
        isocenter_distance: float,
    ) -> Camera:
        """Generate the camera from human-readable parameters.

        This is the recommended way to create the camera.

        Args:
            sensor_size (Union[float, Tuple[float, float]]): (width, height) of the sensor, or a single value for both.
            pixel_size (Union[float, Tuple[float, float]]): (width, height) of a pixel, or a single value for both.
            source_to_detector_distance (int): distance from source to detector
            isocenter_distance (float): isocenter distance

        Returns:
            Camera: camera object
        """
        if isinstance(sensor_size, (int, float)):
            sensor_size = (sensor_size, sensor_size)
        
        if isinstance(pixel_size, (int, float)):
            pixel_size = (pixel_size, pixel_size)
        
        K = np.zeros((3, 3))
        K[0, 0] = source_to_detector_distance / pixel_size[0]
        K[1, 1] = source_to_detector_distance / pixel_size[1]
        K[0, 2] = sensor_size[0] / 2
        K[1, 2] = sensor_size[1] / 2
        K[2, 2] = 1.0
        return cls(K, pixel_size, isocenter_distance)

    @property
    def intrinsic_matrix(self):
        return self.K

    @property
    def sensor_width(self):
        return self.sensor_size[0]

    @property
    def sensor_height(self):
        return self.sensor_size[1]

    @property
    def pixel_width(self):
        return self.pixel_size[0]

    @property
    def pixel_height(self):
        return self.pixel_size[1]

    @staticmethod
    def make_rotation(
        phi: float,
        theta: float,
        rho: float = 0,
    ):
        """Make the rotation matrix given (phi, theta, rho), the angles of the detector.

        Args:
            phi (float): [description]
            theta (float): [description]
            rho (float, optional): [description]. Defaults to 0.
        """
        # rotation around phi and theta
        sin_p = np.sin(phi)
        neg_cos_p = -np.cos(phi)
        z = 0
        sin_t = np.sin(theta)
        cos_t = np.cos(theta)
        omc = 1 - cos_t
        R = np.array([
            [
                sin_p * sin_p * omc + cos_t,
                sin_p * neg_cos_p * omc - z * sin_t, 
                sin_p * z * omc + neg_cos_p * sin_t,
            ],
            [
                sin_p * neg_cos_p * omc + z * sin_t,
                neg_cos_p * neg_cos_p * omc + cos_t,
                neg_cos_p * z * omc - sin_p * sin_t,
            ],
            [
                sin_p * z * omc - neg_cos_p * sin_t,
                neg_cos_p * z * omc + sin_p * sin_t,
                z * z * omc + cos_t,
            ]])
        # rotation around detector priniciple axis
        rho = -phi + np.pi * 0.5 + rho
        R_principle = np.array([[np.cos(rho), -np.sin(rho), 0],
                                [np.sin(rho), np.cos(rho), 0],
                                [0, 0, 1]])
        R = np.matmul(R_principle, R)

        return R

    def make_translation(
        self,
        offset: Optional[List[float]] = None,
    ) -> np.ndarray:
        """Make a translation with the given offset from the isocenter.

        Args:
            offset (Optional[ArrayLike], optional): offset vector as [x, y, z]. None indicates no offset from isocenter. Defaults to None.

        Returns:
            np.ndarray: translation to isocenter containing [x, y, z + isocenter_distance]
        """
        if offset is None:
            return np.array([0, 0, self.isocenter_distance])
        else:
            return np.array([offset[0], offset[1], self.isocenter_distance + offset[2]])

    def make_projections(
        self, 
        phis: List[float],
        thetas: List[float],
        rhos: Optional[List[float]] = None,
        offsets: Optional[List[List[float]]] = None,
        degrees: bool = False,
    ) -> List[CamProjection]:
        """Generate projection matrices for the given phis and thetas, with optional rhos and offsets.

        Args:
            phis (List[float]): list of angles phi in radians (unless degrees is true).
            thetas (List[float]): list of angles theta in radians (unless degrees is True).
            rhos (Optional[List[float]], optional): list of angles rho in radians. Defaults to None.
            offsets (Optional[List[ArrayLike]], optional): list of 3D offsets. Defaults to None.
            degrees (bool): args are in degrees

        Returns:
            List[CamProjection]: list of camera projections onto these views.
        """

        assert len(phis) == len(thetas), 'unequal lengths'

        num_projections = len(phis)
        logging.info(f"generating {num_projections} projections")

        if rhos is None:
            rhos = [0 for _ in range(num_projections)]

        if degrees:
            phis = np.radians(phis)
            thetas = np.radians(thetas)
            rhos = np.radians(rhos)

        if offsets is None:
            offsets = [np.zeros(3) for _ in range(num_projections)]

        projections = []
        for phi, theta, rho, offset in zip(phis, thetas, rhos, offsets):
            R = self.make_rotation(phi, theta, rho)
            t = self.make_translation(offset)
            projections.append(CamProjection(R, self.K, t))
        return projections

    def make_projections_over_range(
        self,
        phi_range: Tuple[float, float, float],
        theta_range: Tuple[float, float, float],
        degrees: bool = True,
    ) -> List[CamProjection]:
        """Generate projection matrices from a uniform set of angles.

        Args:
            phi_range (Tuple[float, float, float]): range of angles phi in (min, max, step) form.
            theta_range (Tuple[float, float, float]): range of angles theta in (min, max, step) form.

        Returns:
            List[CamProjection]: [description]
        """
        phis, thetas = generate_uniform_angles(phi_range, theta_range, degrees=degrees)
        return self.make_projections(phis=phis, thetas=thetas)

