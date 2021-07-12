import numpy as np

# data taken from McGPU files (Badal A, Badano A. Accelerating Monte Carlo simulations of photon transport in a voxelized geometry using a massively parallel graphics processing unit. Med Phys. 2009 Nov;36(11):4878–80. )

#[RAYLEIGH INTERACTIONS (RITA sampling  of atomic form factor from EPDL database)]
#[SAMPLING DATA FROM COMMON/CGRA/: X, P, A, B, ITL, ITU] <- ITL is lower bound for "hinted" binary search, ITU is upper bound for "hinted" binary search

skin_ICRP110_RITA_PARAMS = np.array([
	[  0.0000000000E+00,  0.0000000000E+00, -3.2041866130E-02, -2.4511419068E-04,   1,   2],
	[  2.8785386004E-03,  1.7072008511E-02, -3.1658741939E-02, -8.2138095475E-05,   1,   2],
	[  5.7570772008E-03,  3.3064508545E-02, -5.9974507916E-02, -1.4548816082E-04,   1,   3],
	[  1.1514154402E-02,  6.2169983561E-02, -1.0778427961E-01, -1.2994904567E-04,   2,   3],
	[  2.3028308803E-02,  1.1097006308E-01, -9.7594146777E-02,  1.0295640100E-04,   2,   4],
	[  3.4542463205E-02,  1.5025464716E-01, -8.8700581263E-02,  2.3925946434E-04,   3,   4],
	[  4.6056617607E-02,  1.8257628996E-01, -8.0933162603E-02,  3.3846625769E-04,   3,   4],
	[  5.7570772008E-02,  2.0967068470E-01, -7.4081432716E-02,  4.1219215327E-04,   3,   5],
	[  6.9084926410E-02,  2.3275407329E-01, -6.7982310222E-02,  4.6492290416E-04,   4,   5],
	[  8.0599080812E-02,  2.5270143396E-01, -6.2515073122E-02,  4.9995779757E-04,   4,   5],
	[  9.2113235213E-02,  2.7015659996E-01, -5.7589050016E-02,  5.2030332460E-04,   4,   5],
	[  1.0362738961E-01,  2.8560263575E-01, -5.3134130881E-02,  5.2872293848E-04,   4,   5],
	[  1.1514154402E-01,  2.9940819463E-01, -4.9094382466E-02,  5.2768419441E-04,   4,   5],
	[  1.2665569842E-01,  3.1185887042E-01, -4.5423871488E-02,  5.1932835551E-04,   4,   5],
	[  1.3816985282E-01,  3.2317889274E-01, -8.0972825080E-02,  1.9856613868E-03,   4,   6],
	[  1.6119816162E-01,  3.4310467319E-01, -7.0146901383E-02,  1.8225475911E-03,   5,   6],
	[  1.8422647043E-01,  3.6023670951E-01, -6.1042961124E-02,  1.6368397329E-03,   5,   6],
	[  2.0725477923E-01,  3.7527741204E-01, -5.3380520166E-02,  1.4485305853E-03,   5,   6],
	[  2.3028308803E-01,  3.8871190302E-01, -9.0007565008E-02,  4.7373891489E-03,   5,   6],
	[  2.7633970564E-01,  4.1204718691E-01, -7.1292973338E-02,  3.5623508819E-03,   5,   7],
	[  3.2239632325E-01,  4.3204164591E-01, -5.7671922001E-02,  2.6572617190E-03,   6,   7],
	[  3.6845294085E-01,  4.4971935650E-01, -4.7685008285E-02,  1.9816232678E-03,   6,   7],
	[  4.1450955846E-01,  4.6570352481E-01, -4.0287385477E-02,  1.4834191557E-03,   6,   7],
	[  4.6056617607E-01,  4.8039437260E-01, -3.4742893091E-02,  1.1168719055E-03,   6,   8],
	[  5.0662279367E-01,  4.9406060418E-01, -3.0535323543E-02,  8.4632008019E-04,   7,   8],
	[  5.5267941128E-01,  5.0688952955E-01, -2.7301886657E-02,  6.4538922421E-04,   7,   8],
	[  5.9873602889E-01,  5.1901601845E-01, -2.4785965651E-02,  4.9501523171E-04,   7,   9],
	[  6.4479264649E-01,  5.3053998318E-01, -4.4553642990E-02,  1.3482289649E-03,   8,   9],
	[  7.3690588171E-01,  5.5206710627E-01, -3.9095797524E-02,  8.1017374751E-04,   8,   9],
	[  8.2901911692E-01,  5.7190231316E-01, -3.5459391266E-02,  4.8609176360E-04,   8,  10],
	[  9.2113235213E-01,  5.9032589930E-01, -3.2934343457E-02,  2.8516957557E-04,   9,  10],
	[  1.0132455873E+00,  6.0753303818E-01, -3.1008804728E-02,  1.6915174998E-04,   9,  10],
	[  1.1053588226E+00,  6.2366964335E-01, -5.7487247331E-02,  1.7688999477E-04,   9,  11],
	[  1.2895852930E+00,  6.5315999891E-01, -5.3925895229E-02, -1.2261467777E-04,  10,  11],
	[  1.4738117634E+00,  6.7946234203E-01, -5.1484739356E-02, -2.5831278241E-04,  10,  12],
	[  1.6580382338E+00,  7.0305278471E-01, -4.9630081238E-02, -3.1902440364E-04,  11,  12],
	[  1.8422647043E+00,  7.2429974595E-01, -4.8108796903E-02, -3.4347357846E-04,  11,  13],
	[  2.0264911747E+00,  7.4350127200E-01, -4.6713175617E-02, -3.3118630872E-04,  12,  13],
	[  2.2107176451E+00,  7.6090690668E-01, -4.5585312492E-02, -2.1331001584E-04,  12,  14],
	[  2.3949441155E+00,  7.7672881189E-01, -4.4197288172E-02, -3.3551608671E-04,  13,  15],
	[  2.5791705860E+00,  7.9115069492E-01, -4.3207636876E-02, -3.2443636084E-04,  14,  15],
	[  2.7633970564E+00,  8.0432605439E-01, -4.2376392922E-02, -1.3144651778E-04,  14,  16],
	[  2.9476235268E+00,  8.1638827405E-01, -7.8767869934E-02, -1.1542950937E-03,  15,  16],
	[  3.3160764677E+00,  8.3763832333E-01, -7.5744592667E-02, -1.0596802430E-03,  15,  17],
	[  3.6845294085E+00,  8.5566755756E-01, -7.2939060842E-02, -9.7365714645E-04,  16,  17],
	[  4.0529823494E+00,  8.7106551153E-01, -7.0225148669E-02, -8.3833723203E-04,  16,  18],
	[  4.4214352902E+00,  8.8429912126E-01, -6.7683692056E-02, -8.1571347180E-04,  17,  18],
	[  4.7898882311E+00,  8.9574063697E-01, -6.5387682784E-02, -7.5386078068E-04,  17,  19],
	[  5.1583411719E+00,  9.0568538165E-01, -6.3230957442E-02, -6.9841970555E-04,  18,  19],
	[  5.5267941128E+00,  9.1437210589E-01, -6.1201839614E-02, -6.4858209388E-04,  18,  20],
	[  5.8952470537E+00,  9.2199523938E-01, -1.1161547655E-01, -2.3341320769E-03,  19,  20],
	[  6.6321529354E+00,  9.3466045085E-01, -1.0539806704E-01, -2.0381742322E-03,  19,  20],
	[  7.3690588171E+00,  9.4465349018E-01, -9.9790595418E-02, -1.7928682393E-03,  19,  21],
	[  8.1059646988E+00,  9.5265054947E-01, -9.4711877876E-02, -1.5875515973E-03,  20,  21],
	[  8.8428705805E+00,  9.5913173827E-01, -9.0093801170E-02, -1.4142078526E-03,  20,  22],
	[  9.5797764622E+00,  9.6444439084E-01, -8.5879018372E-02, -1.2667174755E-03,  21,  22],
	[  1.0316682344E+01,  9.6884406200E-01, -1.5079149543E-01, -4.3459125442E-03,  21,  22],
	[  1.1790494107E+01,  9.7562184972E-01, -1.3926956041E-01, -3.5841842380E-03,  21,  23],
	[  1.3264305871E+01,  9.8050888709E-01, -1.2928728347E-01, -3.0026721856E-03,  22,  23],
	[  1.4738117634E+01,  9.8413066160E-01, -1.2057170426E-01, -2.5502815042E-03,  22,  24],
	[  1.6211929398E+01,  9.8687813265E-01, -1.1290849191E-01, -2.1924622484E-03,  23,  24],
	[  1.7685741161E+01,  9.8900460563E-01, -1.9021512337E-01, -7.1596471880E-03,  23,  25],
	[  2.0633364688E+01,  9.9201861964E-01, -1.7181088061E-01, -5.6004859967E-03,  24,  26],
	[  2.3580988215E+01,  9.9399441727E-01, -1.5656263535E-01, -4.5121559463E-03,  25,  26],
	[  2.6528611741E+01,  9.9535030252E-01, -1.4376941636E-01, -3.7233330626E-03,  25,  27],
	[  2.9476235268E+01,  9.9631566199E-01, -2.3131279419E-01, -1.1642602665E-02,  26,  28],
	[  3.5371482322E+01,  9.9755709872E-01, -2.0489128994E-01, -8.7271477274E-03,  27,  28],
	[  4.1266729376E+01,  9.9828765263E-01, -1.8395154900E-01, -6.8273694973E-03,  27,  29],
	[  4.7161976429E+01,  9.9874852330E-01, -2.7920780615E-01, -2.0197759800E-02,  28,  29],
	[  5.8952470537E+01,  9.9926754788E-01, -2.4320383779E-01, -1.4271579839E-02,  28,  29],
	[  7.0742964644E+01,  9.9953220347E-01, -3.3852311209E-01, -3.8211172437E-02,  28,  30],
	[  9.4323952858E+01,  9.9977371668E-01, -2.9035184589E-01, -2.4353387216E-02,  29,  30],
	[  1.1790494107E+02,  9.9987307537E-01, -2.5365880364E-01, -1.6933389781E-02,  29,  31],
	[  1.4148592929E+02,  9.9992155997E-01, -3.4796943291E-01, -4.4450612815E-02,  30,  31],
	[  1.8864790572E+02,  9.9996381858E-01, -4.1073988354E-01, -9.4514991017E-02,  30,  32],
	[  2.8297185858E+02,  9.9998814299E-01, -3.5494371840E-01, -4.8595037755E-02,  31,  32],
	[  3.7729581143E+02,  9.9999470118E-01, -3.7564229211E-01, -3.1869736886E-01,  31,  32],
	[  7.5459162287E+02,  9.9999926216E-01, -3.7213439743E-01, -3.2645298848E-01,  31,  33],
	[  1.5091832457E+03,  9.9999989946E-01, -3.7356393858E-01, -3.2651960323E-01,  32,  33],
	[  3.0183664915E+03,  9.9999998632E-01, -3.7882200346E-01, -3.2092990243E-01,  32,  34],
	[  6.0367329829E+03,  9.9999999811E-01, -3.8740545321E-01, -3.1063393798E-01,  33,  34],
	[  1.2073465966E+04,  9.9999999973E-01, -3.9906442099E-01, -2.9601719219E-01,  33,  34],
	[  2.4146931932E+04,  9.9999999996E-01, -4.1341003122E-01, -2.7744795678E-01,  33,  35],
	[  4.8293863864E+04,  9.9999999999E-01, -4.2958447496E-01, -2.5574604130E-01,  34,  35],
	[  9.6587727727E+04,  1.0000000000E+00, -4.4616209852E-01, -2.3241573537E-01,  34,  35],
	[  1.9317545545E+05,  1.0000000000E+00, -4.6144850781E-01, -2.0944981171E-01,  34,  35],
	[  3.8635091091E+05,  1.0000000000E+00, -4.7408105437E-01, -1.8873736862E-01,  34,  36],
	[  7.7270182182E+05,  1.0000000000E+00, -4.8350212760E-01, -1.7146782468E-01,  35,  36],
	[  1.5454036436E+06,  1.0000000000E+00, -4.8995645950E-01, -1.5794213117E-01,  35,  36],
	[  3.0908072873E+06,  1.0000000000E+00, -4.9412034842E-01, -1.4780641889E-01,  35,  37],
	[  6.1816145745E+06,  1.0000000000E+00, -4.9671707180E-01, -1.4041934355E-01,  36,  37],
	[  1.2363229149E+07,  1.0000000000E+00, -4.9831850767E-01, -1.3511989191E-01,  36,  38],
	[  2.4726458298E+07,  1.0000000000E+00, -4.9931143682E-01, -1.3134914862E-01,  37,  38],
	[  4.9452916596E+07,  1.0000000000E+00, -4.9993646212E-01, -1.2867664036E-01,  37,  38],
	[  9.8905833192E+07,  1.0000000000E+00, -5.0033756113E-01, -1.2678574562E-01,  37,  39],
	[  1.9781166638E+08,  1.0000000000E+00, -5.0060004679E-01, -1.2544873166E-01,  38,  39],
	[  3.9562333277E+08,  1.0000000000E+00, -5.0077488680E-01, -1.2450350069E-01,  38,  40],
	[  7.9124666554E+08,  1.0000000000E+00, -5.0089309542E-01, -1.2383520496E-01,  39,  40],
	[  1.5824933311E+09,  1.0000000000E+00, -4.0267382038E-01, -4.1163473870E-02,  39,  41],
	[  2.3737399966E+09,  1.0000000000E+00, -3.2252513803E-01, -2.0552367162E-02,  40,  41],
	[  3.1649866622E+09,  1.0000000000E+00, -2.6701854692E-01, -1.2320099627E-02,  40,  42],
	[  3.9562333277E+09,  1.0000000000E+00, -2.2727512092E-01, -8.2080099359E-03,  41,  42],
	[  4.7474799932E+09,  1.0000000000E+00, -1.9763213136E-01, -5.8599345725E-03,  41,  43],
	[  5.5387266588E+09,  1.0000000000E+00, -1.7474234585E-01, -4.3932056303E-03,  42,  44],
	[  6.3299733243E+09,  1.0000000000E+00, -1.5656095486E-01, -3.4158254694E-03,  43,  44],
	[  7.1212199899E+09,  1.0000000000E+00, -1.4178274998E-01, -2.7319139159E-03,  43,  44],
	[  7.9124666554E+09,  1.0000000000E+00, -1.2953997774E-01, -2.2346803457E-03,  43,  45],
	[  8.7037133209E+09,  1.0000000000E+00, -1.1923490352E-01, -1.8618562879E-03,  44,  45],
	[  9.4949599865E+09,  1.0000000000E+00, -1.1044306072E-01, -1.5751364313E-03,  44,  46],
	[  1.0286206652E+10,  1.0000000000E+00, -1.0285502941E-01, -1.3499036240E-03,  45,  46],
	[  1.1077453318E+10,  1.0000000000E+00, -9.6240089582E-02, -1.1697509483E-03,  45,  47],
	[  1.1868699983E+10,  1.0000000000E+00, -9.0422778201E-02, -1.0234014122E-03,  46,  47],
	[  1.2659946649E+10,  1.0000000000E+00, -8.5267326801E-02, -9.0289653703E-04,  46,  48],
	[  1.3451193314E+10,  1.0000000000E+00, -8.0667063529E-02, -8.0248967676E-04,  47,  49],
	[  1.4242439980E+10,  1.0000000000E+00, -7.6537030536E-02, -7.1794722760E-04,  48,  49],
	[  1.5033686645E+10,  1.0000000000E+00, -7.2808736088E-02, -6.4609451344E-04,  48,  50],
	[  1.5824933311E+10,  1.0000000000E+00, -6.9426355831E-02, -5.8451310252E-04,  49,  51],
	[  1.6616179976E+10,  1.0000000000E+00, -6.6343937699E-02, -5.3133447032E-04,  50,  52],
	[  1.7407426642E+10,  1.0000000000E+00, -6.3523314634E-02, -4.8509648462E-04,  51,  53],
	[  1.8198673307E+10,  1.0000000000E+00, -6.0932524750E-02, -4.4464176516E-04,  52,  54],
	[  1.8989919973E+10,  1.0000000000E+00, -5.8544600798E-02, -4.0904451316E-04,  53,  55],
	[  1.9781166638E+10,  1.0000000000E+00, -5.6336632091E-02, -3.7755704793E-04,  54,  56],
	[  2.0572413304E+10,  1.0000000000E+00, -5.4289030021E-02, -3.4957020910E-04,  55,  57],
	[  2.1363659970E+10,  1.0000000000E+00, -5.2384947440E-02, -3.2458366229E-04,  56,  59],
	[  2.2154906635E+10,  1.0000000000E+00, -5.0609815622E-02, -3.0218337455E-04,  58,  61],
	[  2.2946153301E+10,  1.0000000000E+00, -4.8950971934E-02, -2.8202434755E-04,  60,  64],
	[  2.3737399966E+10,  1.0000000000E+00, -4.7397358169E-02, -2.6381725101E-04,  63, 128],
	[  2.4528646632E+10,  1.0000000000E+00,  0.0000000000E+00,  0.0000000000E+00, 127, 128],
])
