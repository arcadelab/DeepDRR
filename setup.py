import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deepdrr",
    version="1.1.0a1",
    author="Benjamin D. Killeen",
    author_email="killeen@jhu.edu",
    description="A Catalyst for Machine Learning in Fluoroscopy-guided Procedures.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy",
        "torch",
        "torchvision",
        "nibabel",
        "scikit-image",
        "pydicom",
        "pycuda",
        "pyvista",
        "scipy",
        "pyvista",
    ],
    extras_require={"gpu": ["pycuda"]},
    include_package_data=True,
    python_requires=">=3.8",
)
