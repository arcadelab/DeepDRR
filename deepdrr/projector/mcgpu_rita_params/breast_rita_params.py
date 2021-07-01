import numpy as np

# data taken from McGPU files (Badal A, Badano A. Accelerating Monte Carlo simulations of photon transport in a voxelized geometry using a massively parallel graphics processing unit. Med Phys. 2009 Nov;36(11):4878–80. )

#[RAYLEIGH INTERACTIONS (RITA sampling  of atomic form factor from EPDL database)]
#[SAMPLING DATA FROM COMMON/CGRA/: X, P, A, B, ITL, ITU] <- ITL is lower bound for "hinted" binary search, ITU is upper bound for "hinted" binary search

breast_RITA_PARAMS = np.array([
	[  0.0000000000E+00,  0.0000000000E+00, -2.3448694719E-02, -2.4541269308E-04,   1,   2],
	[  1.7941030058E-03,  1.1602695672E-02, -2.3538337185E-02, -7.9977734684E-05,   1,   3],
	[  3.5882060116E-03,  2.2660219091E-02, -4.5398336041E-02, -1.2531355295E-04,   2,   4],
	[  7.1764120232E-03,  4.3268317875E-02, -8.3886237502E-02, -1.6231970091E-05,   3,   4],
	[  1.4352824046E-02,  7.9302974507E-02, -7.7424186028E-02,  1.9460431854E-04,   3,   4],
	[  2.1529236070E-02,  1.0976429422E-01, -7.1396616769E-02,  2.7467290296E-04,   3,   5],
	[  2.8705648093E-02,  1.3587902815E-01, -6.5972619095E-02,  3.1233700538E-04,   4,   5],
	[  3.5882060116E-02,  1.5854991058E-01, -6.1119256008E-02,  3.3206995168E-04,   4,   5],
	[  4.3058472139E-02,  1.7845081950E-01, -5.6767504914E-02,  3.4270804470E-04,   4,   5],
	[  5.0234884162E-02,  1.9609322015E-01, -5.2848555546E-02,  3.4793552093E-04,   4,   5],
	[  5.7411296186E-02,  2.1187158506E-01, -9.4157064517E-02,  1.3953137376E-03,   4,   6],
	[  7.1764120232E-02,  2.3900743385E-01, -8.2859915658E-02,  1.3682043314E-03,   5,   6],
	[  8.6116944278E-02,  2.6165149100E-01, -7.3278079426E-02,  1.3140868568E-03,   5,   6],
	[  1.0046976832E-01,  2.8097992905E-01, -6.5071854641E-02,  1.2417861462E-03,   5,   7],
	[  1.1482259237E-01,  2.9779456042E-01, -5.7995747772E-02,  1.1582218831E-03,   6,   7],
	[  1.2917541642E-01,  3.1265967248E-01, -5.1865143214E-02,  1.0689258289E-03,   6,   7],
	[  1.4352824046E-01,  3.2598314597E-01, -8.9276473028E-02,  3.7296680956E-03,   6,   7],
	[  1.7223388856E-01,  3.4913751103E-01, -7.3115380446E-02,  3.0507587869E-03,   6,   8],
	[  2.0093953665E-01,  3.6890128737E-01, -6.0590598212E-02,  2.4585004100E-03,   7,   8],
	[  2.2964518474E-01,  3.8626488250E-01, -5.0853150547E-02,  1.9649465152E-03,   7,   8],
	[  2.5835083284E-01,  4.0185790276E-01, -4.3251142360E-02,  1.5646618682E-03,   7,   9],
	[  2.8705648093E-01,  4.1609835007E-01, -3.7284958769E-02,  1.2450807204E-03,   8,   9],
	[  3.1576212902E-01,  4.2927394913E-01, -3.2573610871E-02,  9.9205969464E-04,   8,  10],
	[  3.4446777711E-01,  4.4158892489E-01, -2.8827694060E-02,  7.9244919602E-04,   9,  10],
	[  3.7317342521E-01,  4.5319213596E-01, -2.5827720910E-02,  6.3503584486E-04,   9,  11],
	[  4.0187907330E-01,  4.6419464621E-01, -4.5721438600E-02,  1.8401281150E-03,  10,  11],
	[  4.5929036948E-01,  4.8471705078E-01, -3.8859776260E-02,  1.2066251782E-03,  10,  12],
	[  5.1670166567E-01,  5.0363489193E-01, -3.4166214077E-02,  8.0042016358E-04,  11,  12],
	[  5.7411296186E-01,  5.2125423491E-01, -3.0863880999E-02,  5.3496331237E-04,  11,  12],
	[  6.3152425804E-01,  5.3778237825E-01, -2.8475257306E-02,  3.5818743605E-04,  11,  12],
	[  6.8893555423E-01,  5.5336694964E-01, -5.1952500035E-02,  7.8223364979E-04,  11,  13],
	[  8.0375814660E-01,  5.8211991792E-01, -4.7385448459E-02,  3.0841534601E-04,  12,  13],
	[  9.1858073897E-01,  6.0813760093E-01, -4.4445390504E-02,  6.9747062422E-05,  12,  13],
	[  1.0334033313E+00,  6.3183755947E-01, -4.2374966042E-02, -5.4688700962E-05,  12,  14],
	[  1.1482259237E+00,  6.5352637208E-01, -4.0799113365E-02, -1.2066999944E-04,  13,  14],
	[  1.2630485161E+00,  6.7344400146E-01, -3.9521369888E-02, -1.5545047044E-04,  13,  15],
	[  1.3778711085E+00,  6.9178646178E-01, -7.3934242224E-02, -7.0929761992E-04,  14,  15],
	[  1.6075162932E+00,  7.2438112895E-01, -7.0550989132E-02, -7.3082793883E-04,  14,  16],
	[  1.8371614779E+00,  7.5237298046E-01, -6.7746438213E-02, -6.3358741909E-04,  15,  16],
	[  2.0668066627E+00,  7.7657419083E-01, -6.4797883440E-02, -6.6542558169E-04,  15,  17],
	[  2.2964518474E+00,  7.9763122292E-01, -6.2496728098E-02, -6.2599132179E-04,  16,  17],
	[  2.5260970322E+00,  8.1605536732E-01, -6.0376054621E-02, -5.8785353923E-04,  16,  18],
	[  2.7557422169E+00,  8.3225408145E-01, -5.8408341196E-02, -5.5226501167E-04,  17,  18],
	[  2.9853874017E+00,  8.4655998865E-01, -5.6574296744E-02, -5.1951003798E-04,  17,  18],
	[  3.2150325864E+00,  8.5924678349E-01, -1.0375982374E-01, -1.9036665646E-03,  17,  19],
	[  3.6743229559E+00,  8.8063259818E-01, -9.8173728425E-02, -1.7015664172E-03,  18,  19],
	[  4.1336133254E+00,  8.9781577564E-01, -9.3187092184E-02, -1.5306262273E-03,  18,  20],
	[  4.5929036948E+00,  9.1179399413E-01, -8.8705119606E-02, -1.3846547230E-03,  19,  20],
	[  5.0521940643E+00,  9.2329061359E-01, -8.4652432510E-02, -1.2588746894E-03,  19,  20],
	[  5.5114844338E+00,  9.3283957431E-01, -8.0968116114E-02, -1.1496231623E-03,  19,  21],
	[  5.9707748033E+00,  9.4084132547E-01, -7.7602401739E-02, -1.0540606241E-03,  20,  21],
	[  6.4300651728E+00,  9.4760051500E-01, -7.4514247509E-02, -9.6995359579E-04,  20,  22],
	[  6.8893555423E+00,  9.5335190772E-01, -7.1669515435E-02, -8.9552023609E-04,  21,  23],
	[  7.3486459118E+00,  9.5827853588E-01, -1.2863860476E-01, -3.2007601564E-03,  22,  23],
	[  8.2672266507E+00,  9.6620491040E-01, -1.2045992535E-01, -2.7742742197E-03,  22,  24],
	[  9.1858073897E+00,  9.7221900739E-01, -1.1327388971E-01, -2.4274577917E-03,  23,  24],
	[  1.0104388129E+01,  9.7686897372E-01, -1.0690633883E-01, -2.1416789316E-03,  23,  25],
	[  1.1022968868E+01,  9.8052366011E-01, -1.0122261269E-01, -1.9034629620E-03,  24,  26],
	[  1.1941549607E+01,  9.8343777511E-01, -9.6116717124E-02, -1.7028576554E-03,  25,  27],
	[  1.2860130346E+01,  9.8579122853E-01, -1.6643918158E-01, -5.8431889507E-03,  26,  27],
	[  1.4697291824E+01,  9.8930013906E-01, -1.5318764750E-01, -4.8257218631E-03,  26,  27],
	[  1.6534453301E+01,  9.9173138792E-01, -1.4188228939E-01, -4.0536453865E-03,  26,  28],
	[  1.8371614779E+01,  9.9347132810E-01, -1.3212658548E-01, -3.4541035445E-03,  27,  28],
	[  2.0208776257E+01,  9.9475068675E-01, -1.2362468706E-01, -2.9793211443E-03,  27,  29],
	[  2.2045937735E+01,  9.9571325261E-01, -2.0560442409E-01, -9.7790617272E-03,  28,  29],
	[  2.5720260691E+01,  9.9702858982E-01, -1.8599658056E-01, -7.6796178650E-03,  28,  29],
	[  2.9394583647E+01,  9.9785268556E-01, -1.6977034479E-01, -6.1969466039E-03,  28,  30],
	[  3.3068906603E+01,  9.9839607242E-01, -1.5613797152E-01, -5.1101500639E-03,  29,  30],
	[  3.6743229559E+01,  9.9876932609E-01, -2.4762217673E-01, -1.5929461967E-02,  29,  31],
	[  4.4091875471E+01,  9.9922809738E-01, -2.2027928530E-01, -1.1818083335E-02,  30,  31],
	[  5.1440521382E+01,  9.9948347400E-01, -1.9827311524E-01, -9.1289759154E-03,  30,  32],
	[  5.8789167294E+01,  9.9963709046E-01, -2.9559278936E-01, -2.6529003600E-02,  31,  32],
	[  7.3486459118E+01,  9.9980066876E-01, -2.5863057000E-01, -1.8262729736E-02,  31,  32],
	[  8.8183750941E+01,  9.9987877910E-01, -3.5221721337E-01, -4.7513013179E-02,  31,  33],
	[  1.1757833459E+02,  9.9994537194E-01, -4.1211483364E-01, -1.0003105195E-01,  32,  33],
	[  1.7636750188E+02,  9.9998260550E-01, -3.5786168056E-01, -5.1007592249E-02,  32,  33],
	[  2.3515666918E+02,  9.9999236669E-01, -3.6453528410E-01, -3.3436553113E-01,  32,  33],
	[  4.7031333835E+02,  9.9999897896E-01, -3.5954118925E-01, -3.4304143595E-01,  32,  34],
	[  9.4062667670E+02,  9.9999986649E-01, -3.5786525735E-01, -3.4648925254E-01,  33,  34],
	[  1.8812533534E+03,  9.9999998270E-01, -3.5852935524E-01, -3.4642894102E-01,  33,  34],
	[  3.7625067068E+03,  9.9999999776E-01, -3.6116763468E-01, -3.4360823793E-01,  33,  35],
	[  7.5250134136E+03,  9.9999999971E-01, -3.6588139619E-01, -3.3805727900E-01,  34,  35],
	[  1.5050026827E+04,  9.9999999996E-01, -3.7311591463E-01, -3.2928616602E-01,  34,  36],
	[  3.0100053655E+04,  9.9999999999E-01, -3.8351927651E-01, -3.1646401767E-01,  35,  36],
	[  6.0200107309E+04,  1.0000000000E+00, -3.9766052951E-01, -2.9872842772E-01,  35,  36],
	[  1.2040021462E+05,  1.0000000000E+00, -4.1549584705E-01, -2.7578096185E-01,  35,  37],
	[  2.4080042924E+05,  1.0000000000E+00, -4.3572305027E-01, -2.4868164277E-01,  36,  37],
	[  4.8160085847E+05,  1.0000000000E+00, -4.5567034829E-01, -2.2020192342E-01,  36,  38],
	[  9.6320171695E+05,  1.0000000000E+00, -4.7237542541E-01, -1.9393615501E-01,  37,  38],
	[  1.9264034339E+06,  1.0000000000E+00, -4.8422364219E-01, -1.7254950890E-01,  37,  38],
	[  3.8528068678E+06,  1.0000000000E+00, -4.9150751811E-01, -1.5677180339E-01,  37,  38],
	[  7.7056137356E+06,  1.0000000000E+00, -4.9556895538E-01, -1.4583971425E-01,  37,  39],
	[  1.5411227471E+07,  1.0000000000E+00, -4.9774341361E-01, -1.3848567857E-01,  38,  39],
	[  3.0822454942E+07,  1.0000000000E+00, -4.9892342070E-01, -1.3357235361E-01,  38,  39],
	[  6.1644909885E+07,  1.0000000000E+00, -4.9959670855E-01, -1.3027336917E-01,  38,  39],
	[  1.2328981977E+08,  1.0000000000E+00, -5.0000543725E-01, -1.2803773436E-01,  38,  40],
	[  2.4657963954E+08,  1.0000000000E+00, -5.0026738377E-01, -1.2650812616E-01,  39,  40],
	[  4.9315927908E+08,  1.0000000000E+00, -5.0044189960E-01, -1.2545286232E-01,  39,  40],
	[  9.8631855815E+08,  1.0000000000E+00, -4.0315255428E-01, -4.1616927187E-02,  39,  41],
	[  1.4794778372E+09,  1.0000000000E+00, -3.2305494524E-01, -2.0760479206E-02,  40,  41],
	[  1.9726371163E+09,  1.0000000000E+00, -2.6750205351E-01, -1.2438298859E-02,  40,  41],
	[  2.4657963954E+09,  1.0000000000E+00, -2.2770375795E-01, -8.2837625663E-03,  40,  42],
	[  2.9589556745E+09,  1.0000000000E+00, -1.9801201448E-01, -5.9124303500E-03,  41,  42],
	[  3.4521149535E+09,  1.0000000000E+00, -1.7508124659E-01, -4.4316337744E-03,  41,  43],
	[  3.9452742326E+09,  1.0000000000E+00, -1.5686572466E-01, -3.4451206736E-03,  42,  43],
	[  4.4384335117E+09,  1.0000000000E+00, -1.4205897668E-01, -2.7549559749E-03,  42,  44],
	[  4.9315927908E+09,  1.0000000000E+00, -1.2979213349E-01, -2.2532596409E-03,  43,  44],
	[  5.4247520698E+09,  1.0000000000E+00, -1.1946656693E-01, -1.8771427936E-03,  43,  45],
	[  5.9179113489E+09,  1.0000000000E+00, -1.1065711454E-01, -1.5879261505E-03,  44,  45],
	[  6.4110706280E+09,  1.0000000000E+00, -1.0305381704E-01, -1.3607564613E-03,  44,  46],
	[  6.9042299071E+09,  1.0000000000E+00, -9.6425534698E-02, -1.1790719124E-03,  45,  46],
	[  7.3973891861E+09,  1.0000000000E+00, -9.0596475212E-02, -1.0314905368E-03,  45,  47],
	[  7.8905484652E+09,  1.0000000000E+00, -8.5430609406E-02, -9.0998070902E-04,  46,  47],
	[  8.3837077443E+09,  1.0000000000E+00, -8.0821056999E-02, -8.0874357233E-04,  46,  47],
	[  8.8768670234E+09,  1.0000000000E+00, -7.6682691913E-02, -7.2350746384E-04,  46,  48],
	[  9.3700263024E+09,  1.0000000000E+00, -7.2946885387E-02, -6.5106944420E-04,  47,  49],
	[  9.8631855815E+09,  1.0000000000E+00, -6.9557700486E-02, -5.8898974386E-04,  48,  49],
	[  1.0356344861E+10,  1.0000000000E+00, -6.6469091894E-02, -5.3538348931E-04,  48,  50],
	[  1.0849504140E+10,  1.0000000000E+00, -6.3642814725E-02, -4.8877585437E-04,  49,  51],
	[  1.1342663419E+10,  1.0000000000E+00, -6.1046841675E-02, -4.4799948333E-04,  50,  52],
	[  1.1835822698E+10,  1.0000000000E+00, -5.8654150140E-02, -4.1212065236E-04,  51,  53],
	[  1.2328981977E+10,  1.0000000000E+00, -5.6441782309E-02, -3.8038532119E-04,  52,  55],
	[  1.2822141256E+10,  1.0000000000E+00, -5.4390109217E-02, -3.5217917938E-04,  54,  56],
	[  1.3315300535E+10,  1.0000000000E+00, -5.2482248971E-02, -3.2699768672E-04,  55,  57],
	[  1.3808459814E+10,  1.0000000000E+00, -5.0703602777E-02, -3.0442334871E-04,  56,  60],
	[  1.4301619093E+10,  1.0000000000E+00, -4.9041481862E-02, -2.8410829728E-04,  59,  63],
	[  1.4794778372E+10,  1.0000000000E+00, -4.7484805186E-02, -2.6576080731E-04,  62, 128],
	[  1.5287937651E+10,  1.0000000000E+00,  0.0000000000E+00,  0.0000000000E+00, 127, 128],
])