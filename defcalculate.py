import numpy
import pandas as pd

nopovtor = 0
nopovtor2 = 0
summin = 0
summax = 0
chillmin = 0
chillmax = 0
TariFF = []
Names = []
fio = []
mincount = []
maxcount = []
dfa = pd.DataFrame(columns=['Kod', 'Колво'])


fgkod2min = ['В 01.066.001', 'В 01.066.002', 'В 01.066.002', 'В 01.066.002', 'А 16.07.004.000.071',
             'А 16.07.004.000.071', 'А 16.07.004.000.071', 'А 16.07.004.000.071', 'А 23.07.002.027', 'А 23.07.002.027',
             'А 23.07.002.027', 'А 23.07.002.027', 'А 16.07.004.000.401', 'А 16.07.004.000.401', 'А 16.07.004.000.401',
             'А 16.07.004.000.401', 'А 16.07.004.000.401', 'А 16.07.004.000.401', 'В01.066.000.000.005',
             'В01.066.000.000.005', 'В01.066.000.000.005', 'В01.066.000.000.005', 'В01.066.000.000.005',
             'В01.066.000.000.005','А 23.07.000.000.030','А 23.07.000.000.030','А 23.07.000.000.030','А 23.07.000.000.030',
             'А 23.07.000.000.030','А 23.07.000.000.030','А 16.07.004.000.386',
             'А 16.07.004.000.386','А 16.07.004.000.386','А 16.07.004.000.386',
             'А 16.07.004.000.386','А 16.07.004.000.386','А 23.07.000.000.001',
             'А 23.07.000.000.001',
             'А 23.07.000.000.001','А 23.07.000.000.001','А 23.07.000.000.001','А 23.07.000.000.001',
             'А 23.07.000.000.001','А 23.07.000.000.001',
             'А 23.07.000.000.002','А 23.07.000.000.002','А 23.07.000.000.002','А 23.07.000.000.002',
             'А 23.07.000.000.002','А 23.07.000.000.002',
             'А 23.07.000.000.005','А 23.07.000.000.005','А 23.07.000.000.005','А 23.07.000.000.005',
             'А 23.07.000.000.005','А 23.07.000.000.005','А 23.07.000.000.005','А 23.07.000.000.005',
             'А 23.07.000.000.005','А 23.07.000.000.005','А 23.07.000.000.005','А 23.07.000.000.005']

fgkod2min = numpy.array(fgkod2min)


fgkod2min2 = ['А 16.07.004.000.386','А 16.07.004.000.386','А 16.07.004.000.386','А 16.07.004.000.386',
              'А 16.07.004.000.386','А 16.07.004.000.386']

fgkod2min2 = numpy.array(fgkod2min2)


fgkod2min3 = ['А 23.07.000.000.030','А 23.07.000.000.030','А 23.07.000.000.030','А 23.07.000.000.030',
              'А 23.07.000.000.030','А 23.07.000.000.030']

fgkod2min3 = numpy.array(fgkod2min3)


fgkod2min4 = ['В01.066.000.000.005',
              'В01.066.000.000.005', 'В01.066.000.000.005', 'В01.066.000.000.005', 'В01.066.000.000.005',
              'В01.066.000.000.005']

fgkod2min4 = numpy.array(fgkod2min4)


fgkod2max = ['В 01.066.001', 'В 01.066.002', 'В 01.066.002', 'В 01.066.002', 'А 16.07.004.000.071',
             'А 16.07.004.000.071', 'А 16.07.004.000.071', 'А 16.07.004.000.071','А 16.07.004.000.072',
             'А 16.07.004.000.072','А 23.07.002.027', 'А 23.07.002.027','А 23.07.002.027', 'А 23.07.002.027',
             'А 23.07.002.027', 'А 23.07.002.027',
             'А 16.07.004.000.401', 'А 16.07.004.000.401', 'А 16.07.004.000.401',
             'А 16.07.004.000.401', 'А 16.07.004.000.401', 'А 16.07.004.000.401',
             'А 11.07.011','А 11.07.011','А 11.07.011','А 11.07.011','В01.066.000.000.006','В01.066.000.000.006',
             'В01.066.000.000.006','В01.066.000.000.006','В01.066.000.000.006','В01.066.000.000.006',
             'А16.07.004.000.380','А16.07.004.000.380','А16.07.004.000.380','А16.07.004.000.380',
             'А16.07.004.000.380','А16.07.004.000.380','А23.07.000.000.029','А23.07.000.000.029','А23.07.000.000.029',
             'А23.07.000.000.029','А23.07.000.000.029',
             'А23.07.000.000.029',
             'А 23.07.000.000.004','А 23.07.000.000.004','А 23.07.000.000.004','А 23.07.000.000.004',
             'В01.066.000.000.008','В01.066.000.000.008','В01.066.000.000.008','В01.066.000.000.008',
             'В01.066.000.000.008','В01.066.000.000.008','А 16.07.004.000.377','А 16.07.004.000.377',
             'А 16.07.004.000.377','А 16.07.004.000.377','А 16.07.004.000.377','А 16.07.004.000.377',
             'А 23.07.000.000.028','А 23.07.000.000.028','А 23.07.000.000.028',
             'А 23.07.000.000.028','А 23.07.000.000.028','А 23.07.000.000.028',
             'В01.066.000.000.011','В01.066.000.000.011','В01.066.000.000.011','В01.066.000.000.011',
             'В01.066.000.000.011','В01.066.000.000.011','В01.066.000.000.011','В01.066.000.000.011',
             'А 16.07.004.000.399','А 16.07.004.000.399','А 16.07.004.000.399','А 16.07.004.000.399',
             'А 16.07.004.000.399','А 16.07.004.000.399','А 16.07.004.000.399','А 16.07.004.000.399',
             'А 23.07.000.000.013',
             'А 23.07.000.000.013','А 23.07.000.000.013','А 23.07.000.000.013','А 23.07.000.000.013',
             'А 23.07.000.000.013','А 23.07.000.000.013','А 23.07.000.000.013']

fgkod2max = numpy.array(fgkod2max)


fgkod2max2 = ['А16.07.004.000.380','А16.07.004.000.380','А16.07.004.000.380','А16.07.004.000.380',
              'А16.07.004.000.380','А16.07.004.000.380']

fgkod2max2 = numpy.array(fgkod2max2)


fgkod2max3 = ['А23.07.000.000.029','А23.07.000.000.029','А23.07.000.000.029','А23.07.000.000.029','А23.07.000.000.029',
              'А23.07.000.000.029']

fgkod2max3 = numpy.array(fgkod2max3)


fgkod2max4 = ['В01.066.000.000.006','В01.066.000.000.006',
              'В01.066.000.000.006','В01.066.000.000.006','В01.066.000.000.006','В01.066.000.000.006']

fgkod2max4 = numpy.array(fgkod2max4)


fgkod2max5 = ['А 16.07.004.000.377','А 16.07.004.000.377',
              'А 16.07.004.000.377','А 16.07.004.000.377','А 16.07.004.000.377','А 16.07.004.000.377']

fgkod2max5 = numpy.array(fgkod2max5)


fgkod2max6 = ['А 23.07.000.000.028','А 23.07.000.000.028','А 23.07.000.000.028',
              'А 23.07.000.000.028','А 23.07.000.000.028','А 23.07.000.000.028']

fgkod2max6 = numpy.array(fgkod2max6)


fgkod2max7 = ['В01.066.000.000.008','В01.066.000.000.008','В01.066.000.000.008','В01.066.000.000.008',
              'В01.066.000.000.008','В01.066.000.000.008']

fgkod2max7 = numpy.array(fgkod2max7)


fgkod2max8 = ['А 16.07.004.000.399','А 16.07.004.000.399','А 16.07.004.000.399','А 16.07.004.000.399',
              'А 16.07.004.000.399','А 16.07.004.000.399','А 16.07.004.000.399','А 16.07.004.000.399']

fgkod2max8 = numpy.array(fgkod2max8)


fgkod2max9 = ['А 23.07.000.000.013',
              'А 23.07.000.000.013','А 23.07.000.000.013','А 23.07.000.000.013','А 23.07.000.000.013',
              'А 23.07.000.000.013','А 23.07.000.000.013','А 23.07.000.000.013']

fgkod2max9 = numpy.array(fgkod2max9)


fgkod2max10 = ['В01.066.000.000.011','В01.066.000.000.011','В01.066.000.000.011','В01.066.000.000.011',
               'В01.066.000.000.011','В01.066.000.000.011','В01.066.000.000.011','В01.066.000.000.011']

fgkod2max10 = numpy.array(fgkod2max10)

fgkod2max11 = ['А16.07.004.000.380','А16.07.004.000.380','А16.07.004.000.380','А16.07.004.000.380',
               'А16.07.004.000.380','А16.07.004.000.380','А23.07.000.000.029','А23.07.000.000.029','А23.07.000.000.029',
               'А23.07.000.000.029','А23.07.000.000.029',
               'А23.07.000.000.029','В01.066.000.000.006','В01.066.000.000.006',
               'В01.066.000.000.006','В01.066.000.000.006','В01.066.000.000.006','В01.066.000.000.006',
               'А 16.07.004.000.377','А 16.07.004.000.377',
               'А 16.07.004.000.377','А 16.07.004.000.377','А 16.07.004.000.377','А 16.07.004.000.377',
               'А 23.07.000.000.028','А 23.07.000.000.028','А 23.07.000.000.028',
               'А 23.07.000.000.028','А 23.07.000.000.028','А 23.07.000.000.028','В01.066.000.000.008',
               'В01.066.000.000.008','В01.066.000.000.008','В01.066.000.000.008',
               'В01.066.000.000.008','В01.066.000.000.008','А 16.07.004.000.399','А 16.07.004.000.399',
               'А 16.07.004.000.399','А 16.07.004.000.399',
               'А 16.07.004.000.399','А 16.07.004.000.399','А 16.07.004.000.399','А 16.07.004.000.399',
               'А 23.07.000.000.013',
               'А 23.07.000.000.013','А 23.07.000.000.013','А 23.07.000.000.013','А 23.07.000.000.013',
               'А 23.07.000.000.013','А 23.07.000.000.013','А 23.07.000.000.013','В01.066.000.000.011',
               'В01.066.000.000.011','В01.066.000.000.011','В01.066.000.000.011',
               'В01.066.000.000.011','В01.066.000.000.011','В01.066.000.000.011','В01.066.000.000.011']

fgkod2max11 = numpy.array(fgkod2max11)

print(fgkod2max11)

fgkod3min = ['В 01.066.001', 'В 01.066.002', 'В 01.066.002', 'В 01.066.002', 'А 16.07.004.000.071',
             'А 16.07.004.000.071', 'А 16.07.004.000.071', 'А 16.07.004.000.071', 'А 23.07.002.027', 'А 23.07.002.027',
             'А 23.07.002.027', 'А 23.07.002.027', 'А 16.07.004.000.401', 'А 16.07.004.000.401', 'А 16.07.004.000.401',
             'А 16.07.004.000.401','А 11.07.011','А 11.07.011','А 11.07.011','А 11.07.011','В01.066.000.000.005',
             'В01.066.000.000.005', 'В01.066.000.000.005', 'В01.066.000.000.005','А 16.07.004.000.386',
             'А 16.07.004.000.386','А 16.07.004.000.386','А 16.07.004.000.386','А 23.07.000.000.030',
             'А 23.07.000.000.030','А 23.07.000.000.030','А 23.07.000.000.030','А 23.07.000.000.001',
             'А 23.07.000.000.001','А 23.07.000.000.001','А 23.07.000.000.001','А 23.07.000.000.002',
             'А 23.07.000.000.002','А 23.07.000.000.005','А 23.07.000.000.005','А 23.07.000.000.005',
             'А 23.07.000.000.005','А 23.07.000.000.005','А 23.07.000.000.005','В01.066.000.000.012','А 16.07.035',
             'А 23.07.000.000.032','А 23.07.000.000.080','А 23.07.000.000.080']

fgkod3min = numpy.array(fgkod3min)

fgkod3min2 = ['А 16.07.004.000.386','А 16.07.004.000.386','А 16.07.004.000.386','А 16.07.004.000.386']

fgkod3min2 = numpy.array(fgkod3min2)

fgkod3min3 = ['А 23.07.000.000.030','А 23.07.000.000.030','А 23.07.000.000.030','А 23.07.000.000.030',]

fgkod3min3 = numpy.array(fgkod3min3)

fgkod3min4 = ['В01.066.000.000.005',
              'В01.066.000.000.005', 'В01.066.000.000.005', 'В01.066.000.000.005']

fgkod3min5 = ['В01.066.000.000.012']

fgkod3min5 = numpy.array(fgkod3min5)

fgkod3min6 = ['А 16.07.035']

fgkod3min6 = numpy.array(fgkod3min6)

fgkod3min7 = ['А 23.07.000.000.032']

fgkod3min7 = numpy.array(fgkod3min7)

fgkod3min4 = numpy.array(fgkod3min4)

fgkod3max = ['В 01.066.001', 'В 01.066.002', 'В 01.066.002', 'В 01.066.002',
             'В 01.066.002','В 01.066.002','В 01.066.002', 'А 16.07.004.000.071',
             'А 16.07.004.000.071', 'А 16.07.004.000.071', 'А 16.07.004.000.071','А 16.07.004.000.072',
             'А 16.07.004.000.072','А 23.07.002.027', 'А 23.07.002.027','А 23.07.002.027', 'А 23.07.002.027',
             'А 23.07.002.027', 'А 23.07.002.027','А 16.07.021.000.356','А 16.07.021.000.356','А 16.07.053.000.398',
             'А 16.07.053.000.398','А 16.07.053.000.398','А 16.07.053.000.398','А 16.07.004.000.401',
             'А 16.07.004.000.401', 'А 16.07.004.000.401', 'А 16.07.004.000.401',
             'А 11.07.011','А 11.07.011','А 11.07.011','А 11.07.011','В01.066.000.000.008','В01.066.000.000.008',
             'В01.066.000.000.008','В01.066.000.000.008',
             'А 16.07.004.000.377','А 16.07.004.000.377','А 16.07.004.000.377','А 16.07.004.000.377',
             'А 23.07.000.000.028','А 23.07.000.000.028','А 23.07.000.000.028',
             'А 23.07.000.000.028','В01.066.000.000.011','В01.066.000.000.011','В01.066.000.000.011',
             'В01.066.000.000.011','А 16.07.004.000.399','А 16.07.004.000.399','А 16.07.004.000.399',
             'А 16.07.004.000.399','А 23.07.000.000.013','А 23.07.000.000.013','А 23.07.000.000.013',
             'А 23.07.000.000.013','В01.066.000.000.014','А 16.07.036','А 23.07.000.000.014','А 23.07.000.000.015',
             'А 23.07.000.000.016','А 23.07.000.000.019','А 23.07.000.000.019','А 23.07.000.000.020',
             'А 23.07.000.000.020','А 23.07.000.000.021','А 23.07.000.000.021']

fgkod3max = numpy.array(fgkod3max)

fgkod3max2 = ['В01.066.000.000.008','В01.066.000.000.008',
              'В01.066.000.000.008','В01.066.000.000.008']

fgkod3max2 = numpy.array(fgkod3max2)

fgkod3max3 = ['А 16.07.004.000.377','А 16.07.004.000.377','А 16.07.004.000.377','А 16.07.004.000.377']

fgkod3max3 = numpy.array(fgkod3max3)

fgkod3max4 = ['А 23.07.000.000.028','А 23.07.000.000.028','А 23.07.000.000.028',
              'А 23.07.000.000.028']

fgkod3max4 = numpy.array(fgkod3max4)

fgkod3max5 = ['В01.066.000.000.011','В01.066.000.000.011','В01.066.000.000.011','В01.066.000.000.011']

fgkod3max5 = numpy.array(fgkod3max5)

fgkod3max6 = ['А 16.07.004.000.399','А 16.07.004.000.399','А 16.07.004.000.399','А 16.07.004.000.399']

fgkod3max6 = numpy.array(fgkod3max6)

fgkod3max7 = ['А 23.07.000.000.013','А 23.07.000.000.013','А 23.07.000.000.013','А 23.07.000.000.013']

fgkod3max7 = numpy.array(fgkod3max7)

fgkod3max8 = ['В01.066.000.000.014']

fgkod3max8 = numpy.array(fgkod3max8)

fgkod3max9 = ['А 16.07.036']

fgkod3max9 = numpy.array(fgkod3max9)

fgkod3max10 = ['А 23.07.000.000.014']

fgkod3max10 = numpy.array(fgkod3max10)

fgkod3max11 = ['А 23.07.000.000.015']

fgkod3max11 = numpy.array(fgkod3max11)

fgkod3max12 = ['А 23.07.000.000.016']

fgkod3max12 = numpy.array(fgkod3max12)

fgkod3max13 = ['В01.066.000.000.008','В01.066.000.000.008',
               'В01.066.000.000.008','В01.066.000.000.008','А 16.07.004.000.377','А 16.07.004.000.377',
               'А 16.07.004.000.377','А 16.07.004.000.377','А 23.07.000.000.028','А 23.07.000.000.028',
               'А 23.07.000.000.028',
               'А 23.07.000.000.028','В01.066.000.000.011','В01.066.000.000.011',
               'В01.066.000.000.011','В01.066.000.000.011','А 16.07.004.000.399','А 16.07.004.000.399',
               'А 16.07.004.000.399','А 16.07.004.000.399','А 23.07.000.000.013','А 23.07.000.000.013',
               'А 23.07.000.000.013','А 23.07.000.000.013','В01.066.000.000.014','А 16.07.036',
               'А 23.07.000.000.014','А 23.07.000.000.015','А 23.07.000.000.016']

fgkod3max13 = numpy.array(fgkod3max13)

fgkod4min = ['В 01.066.001', 'В 01.066.002', 'В 01.066.002', 'В 01.066.002', 'В 01.066.002', 'В 01.066.002',
             'В 01.066.002', 'А 16.07.004.000.071', 'А 16.07.004.000.071', 'А 16.07.004.000.071', 'А 16.07.004.000.071',
             'А 23.07.002.027', 'А 23.07.002.027', 'А 23.07.002.027', 'А 23.07.002.027', 'А 16.07.021.000.356',
             'А 16.07.021.000.356', 'А 16.07.004.000.401', 'А 16.07.004.000.401', 'В01.066.000.000.005',
             'В01.066.000.000.005', 'А 16.07.004.000.386', 'А 16.07.004.000.386', 'А 23.07.000.000.030',
             'А 23.07.000.000.030', 'В01.066.000.000.012','А 16.07.035', 'А 23.07.000.000.032', 'А 23.07.000.000.080',
             'А 23.07.000.000.080']

fgkod4min = numpy.array(fgkod4min)


fgkod4min2 = ['В01.066.000.000.005', 'В01.066.000.000.005']

fgkod4min2 = numpy.array(fgkod4min2)

fgkod4min3 = ['А 16.07.004.000.386', 'А 16.07.004.000.386']

fgkod4min3 = numpy.array(fgkod4min3)

fgkod4min4 = ['А 23.07.000.000.030', 'А 23.07.000.000.030']

fgkod4min4 = numpy.array(fgkod4min4)

fgkod4min5 = ['В01.066.000.000.012']

fgkod4min5 = numpy.array(fgkod4min5)

fgkod4min6 = ['А 16.07.035']

fgkod4min6 = numpy.array(fgkod4min6)

fgkod4min7 = ['А 23.07.000.000.032']

fgkod4min7 = numpy.array(fgkod4min7)

fgkod4min8 = ['В01.066.000.000.005', 'В01.066.000.000.005','А 16.07.004.000.386', 'А 16.07.004.000.386',
              'А 23.07.000.000.030', 'А 23.07.000.000.030','В01.066.000.000.012','А 16.07.035','А 23.07.000.000.032']

fgkod4min8 = numpy.array(fgkod4min8)

fgkod4max = ['В 01.066.001', 'В 01.066.002', 'В 01.066.002', 'В 01.066.002', 'В 01.066.002', 'В 01.066.002',
             'В 01.066.002', 'А 16.07.004.000.071', 'А 16.07.004.000.071', 'А 16.07.004.000.072', 'А 16.07.004.000.072',
             'А 23.07.002.027', 'А 23.07.002.027', 'А 23.07.002.027', 'А 23.07.002.027', 'А 16.07.021.000.356',
             'А 16.07.021.000.356', 'А 16.07.004.000.401', 'А 16.07.004.000.401', 'А 11.07.011', 'А 11.07.011',
             'В01.066.000.000.008', 'В01.066.000.000.008', 'А 16.07.004.000.377', 'А 16.07.004.000.377',
             'А 23.07.000.000.028', 'А 23.07.000.000.028', 'В01.066.000.000.014', 'А 16.07.036', 'А 23.07.000.000.014',
             'А 23.07.000.000.015', 'А 23.07.000.000.016', 'А 23.07.000.000.018', 'А 23.07.000.000.019',
             'А 23.07.000.000.019', 'А 23.07.000.000.020', 'А 23.07.000.000.020', 'А 23.07.000.000.021',
             'А 23.07.000.000.021']

fgkod4max = numpy.array(fgkod4max)

fgkod4max2 = ['В01.066.000.000.008', 'В01.066.000.000.008']

fgkod4max2 = numpy.array(fgkod4max2)

fgkod4max3 = ['А 16.07.004.000.377', 'А 16.07.004.000.377']

fgkod4max3 = numpy.array(fgkod4max3)

fgkod4max4 = ['А 23.07.000.000.028', 'А 23.07.000.000.028']

fgkod4max4 = numpy.array(fgkod4max4)

fgkod4max5 = ['В01.066.000.000.014']

fgkod4max5 = numpy.array(fgkod4max5)

fgkod4max6 = ['А 16.07.036']

fgkod4max6 = numpy.array(fgkod4max6)

fgkod4max7 = ['А 23.07.000.000.014']

fgkod4max7 = numpy.array(fgkod4max7)

fgkod4max8 = ['А 23.07.000.000.015']

fgkod4max8 = numpy.array(fgkod4max8)

fgkod4max9 = ['А 23.07.000.000.016']

fgkod4max9 = numpy.array(fgkod4max9)

fgkod4max10 = ['В01.066.000.000.008', 'В01.066.000.000.008','А 16.07.004.000.377', 'А 16.07.004.000.377',
               'А 23.07.000.000.028', 'А 23.07.000.000.028','В01.066.000.000.014','А 16.07.036',
               'А 23.07.000.000.014','А 23.07.000.000.015','А 23.07.000.000.016']

fgkod4max10 = numpy.array(fgkod4max10)

fgkod5min = ['В 01.066.001', 'В 01.066.002', 'В 01.066.002',
             'В 01.066.002',
             'В 01.066.002', 'А 16.07.004.000.071', 'А 16.07.004.000.072', 'А 23.07.002.027', 'А 23.07.002.027',
             'А 16.07.021.000.356', 'А 16.07.021.000.356', 'А 16.07.021.000.356', 'В01.066.000.000.013', 'А 16.07.023',
             'А 23.07.000.000.049', 'А 16.07.023.000.363']

fgkod5min = numpy.array(fgkod5min)

fgkod5min2 = ['В01.066.000.000.013']

fgkod5min2 = numpy.array(fgkod5min2)

fgkod5min3 = ['А 16.07.023']

fgkod5min3 = numpy.array(fgkod5min3)

fgkod5min4 = ['А 23.07.000.000.049']

fgkod5min4 = numpy.array(fgkod5min4)

fgkod5max = ['В 01.066.001', 'В 01.066.002', 'В 01.066.002', 'В 01.066.002', 'В 01.066.002', 'А 16.07.004.000.071',
             'А 16.07.004.000.072', 'А 16.07.004.000.072', 'А 23.07.002.027', 'А 23.07.002.027', 'А 23.07.002.027',
             'А 16.07.021.000.356', 'А 16.07.021.000.356', 'А 16.07.021.000.356', 'В01.066.000.000.013', 'А 16.07.023',
             'А 23.07.000.000.049', 'А 23.07.000.000.011', 'А 23.07.000.000.012', 'А 16.07.023.000.363',
             'А 16.07.023.000.402', 'А 23.07.000.000.035']

fgkod5max = numpy.array(fgkod5max)

fgkod5max2 = ['В01.066.000.000.013']

fgkod5max2 = numpy.array(fgkod5max2)

fgkod5max3 = ['А 16.07.023']

fgkod5max3 = numpy.array(fgkod5max3)

fgkod5max4 = ['А 23.07.000.000.049']

fgkod5max4 = numpy.array(fgkod5max4)

def localcount(cod,clas):
    localcountmin = [[0]* len(cod) for i in range(len(clas))]
    localcountmax = [[0]* len(cod) for i in range(len(clas))]
    print(localcountmin[0])
    return localcountmin, localcountmax

def local(clas):
    localsummin = []
    localsummax = []
    for i in range(len(clas)):
        localsummin.append(0)
        localsummax.append(0)
    return localsummin, localsummax

def onemin(KOD,TARIF,patient,localsummin,localcountmin):
    global summin
    global chillmin
    global nopovtor
    global nopovtor2
    if nopovtor == 0:
        for i in range(len(KOD)):
            if KOD[i] == 'В 01.066.001':
               chillmin = chillmin+1
               summin = summin + TARIF[i]
               localsummin[patient] = localsummin[patient] + TARIF[i]
               localcountmin[i] = localcountmin[i] + 1
    nopovtor = nopovtor+1


def onemax(KOD, TARIF,patient,localsummax,localcountmax):
    global summax
    global chillmax
    global nopovtor
    global nopovtor2
    if nopovtor2 == 0:
      for i in range(len(KOD)):
          if KOD[i] == 'В 01.066.001':
              chillmax = chillmax + 1
              summax = summax + TARIF[i]
              localsummax[patient] = localsummax[patient]+TARIF[i]
              localcountmax[i] = localcountmax[i] + 1
    nopovtor2 = nopovtor2+1
def twomin(KOD,TARIF,patient,localsummin,localcountmin):
    global summin
    global nopovtor
    global nopovtor2
    notrepeat = 6
    global chillmin
    if nopovtor==0:
      for i in range(len(KOD)):
          for j in range(len(fgkod2min)):
              if KOD[i] == fgkod2min[j]:
                      if KOD[i] == fgkod2min2[0] or KOD[i] == fgkod2min3[0] or KOD[i] == fgkod2min4[0]:
                          if notrepeat != 0:
                              notrepeat = notrepeat - 1
                              chillmin = chillmin + 1
                              summin = summin + TARIF[i]
                              localsummin[patient] = localsummin[patient] + TARIF[i]
                              localcountmin[i] = localcountmin[i] + 1

                      else:
                                  chillmin = chillmin + 1
                                  summin = summin + TARIF[i]
                                  localsummin[patient] = localsummin[patient] + TARIF[i]

                                  localcountmin[i] = localcountmin[i] + 1
    else:
      for i in range(len(KOD)):
          for j in range(len(fgkod2min)):
              if KOD[i] == fgkod2min[j] and KOD[i] != 'В 01.066.001':
                      if KOD[i] == fgkod2min2[0] or KOD[i] == fgkod2min3[0] or KOD[i] == fgkod2min4[0]:
                          if notrepeat != 0:
                              notrepeat = notrepeat - 1
                              chillmin = chillmin + 1
                              summin = summin + TARIF[i]
                              localsummin[patient] = localsummin[patient] + TARIF[i]
                              localcountmin[i] = localcountmin[i] + 1

                      else:
                                  chillmin = chillmin + 1
                                  summin = summin + TARIF[i]
                                  localsummin[patient] = localsummin[patient] + TARIF[i]

                                  localcountmin[i] = localcountmin[i] + 1
    nopovtor = nopovtor+1
def twomax(KOD,TARIF,patient,localsummax,localcountmax):
    global summax
    global chillmax
    global nopovtor
    global nopovtor2
    notrepeat = 6
    notrepeat2 = 6
    notrepeat3 = 8
    if nopovtor2==0:
      for i in range(len(KOD)):
          for j in range(len(fgkod2max)):
              if KOD[i] == fgkod2max[j]:
                      if KOD[i] == fgkod2max2[0] or KOD[i] == fgkod2max3[0] or KOD[i] == fgkod2max4[0]:
                          if notrepeat != 0:
                              notrepeat = notrepeat - 1
                              chillmax = chillmax + 1
                              summax = summax + TARIF[i]
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1

                      elif KOD[i] == fgkod2max5[0] or KOD[i] == fgkod2max6[0] or KOD[i] == fgkod2max7[0]:
                          if notrepeat2 != 0:
                              notrepeat2 = notrepeat2 - 1
                              chillmax = chillmax + 1
                              summax = summax + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1

                              localsummax[patient] = localsummax[patient] + TARIF[i]
                      elif KOD[i] == fgkod2max8[0] or KOD[i] == fgkod2max9[0] or KOD[i] == fgkod2max10[0]:
                          if notrepeat3 != 0:
                              notrepeat3 = notrepeat3 - 1
                              chillmax = chillmax + 1
                              summax = summax + TARIF[i]
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1

                      else:
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
    else:
      for i in range(len(KOD)):
          for j in range(len(fgkod2max)):
              if KOD[i] == fgkod2max[j] and KOD[i] != 'В 01.066.001':
                      if KOD[i] == fgkod2max2[0] or KOD[i] == fgkod2max3[0] or KOD[i] == fgkod2max4[0]:
                          if notrepeat != 0:
                              notrepeat = notrepeat - 1
                              chillmax = chillmax + 1
                              summax = summax + TARIF[i]
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1

                      elif KOD[i] == fgkod2max5[0] or KOD[i] == fgkod2max6[0] or KOD[i] == fgkod2max7[0]:
                          if notrepeat2 != 0:
                              notrepeat2 = notrepeat2 - 1
                              chillmax = chillmax + 1
                              summax = summax + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1

                              localsummax[patient] = localsummax[patient] + TARIF[i]
                      elif KOD[i] == fgkod2max8[0] or KOD[i] == fgkod2max9[0] or KOD[i] == fgkod2max10[0]:
                          if notrepeat3 != 0:
                              notrepeat3 = notrepeat3 - 1
                              chillmax = chillmax + 1
                              summax = summax + TARIF[i]
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1

                      else:
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
    nopovtor2 = nopovtor2+1

def threemin(KOD,TARIF,patient,localsummin,localcountmin):
    global summin
    global chillmin
    global nopovtor
    global nopovtor2
    notrepeat = 4
    notrepeat2 = 1
    if nopovtor==0:
      for i in range(len(KOD)):
          for j in range(len(fgkod3min)):
              if KOD[i] == fgkod3min[j]:
                      if KOD[i] == fgkod3min2[0] or KOD[i] == fgkod3min3[0] or KOD[i] == fgkod3min4[0]:
                          if notrepeat != 0:
                              notrepeat = notrepeat - 1
                              summin = summin + TARIF[i]
                              chillmin = chillmin + 1
                              localcountmin[i] = localcountmin[i] + 1
                              localsummin[patient] = localsummin[patient] + TARIF[i]
                      elif KOD[i] == fgkod3min5[0] or KOD[i] == fgkod3min6[0] or KOD[i] == fgkod3min7[0]:
                          if notrepeat2 != 0:
                              notrepeat2 = notrepeat2 - 1
                              summin = summin + TARIF[i]
                              chillmin = chillmin + 1
                              localcountmin[i] = localcountmin[i] + 1
                              localsummin[patient] = localsummin[patient] + TARIF[i]
                      else:
                          summin = summin + TARIF[i]
                          chillmin = chillmin + 1
                          localsummin[patient] = localsummin[patient] + TARIF[i]
                          localcountmin[i] = localcountmin[i] + 1
    else:
      for i in range(len(KOD)):
          for j in range(len(fgkod3min)):
              if KOD[i] == fgkod3min[j] and KOD[i] != 'В 01.066.001':
                      if KOD[i] == fgkod3min2[0] or KOD[i] == fgkod3min3[0] or KOD[i] == fgkod3min4[0]:
                          if notrepeat != 0:
                              notrepeat = notrepeat - 1
                              summin = summin + TARIF[i]
                              chillmin = chillmin + 1
                              localcountmin[i] = localcountmin[i] + 1
                              localsummin[patient] = localsummin[patient] + TARIF[i]
                      elif KOD[i] == fgkod3min5[0] or KOD[i] == fgkod3min6[0] or KOD[i] == fgkod3min7[0]:
                          if notrepeat2 != 0:
                              notrepeat2 = notrepeat2 - 1
                              summin = summin + TARIF[i]
                              chillmin = chillmin + 1
                              localcountmin[i] = localcountmin[i] + 1
                              localsummin[patient] = localsummin[patient] + TARIF[i]
                      else:
                          summin = summin + TARIF[i]
                          chillmin = chillmin + 1
                          localsummin[patient] = localsummin[patient] + TARIF[i]
                          localcountmin[i] = localcountmin[i] + 1
    nopovtor = nopovtor+1
def threemax(KOD,TARIF,patient,localsummax,localcountmax):
    global summax
    global chillmax
    global nopovtor
    global nopovtor2
    notrepeat = 4
    notrepeat2 = 4
    notrepeat3 = 1
    if nopovtor2==0:
      for i in range(len(KOD)):
          for j in range(len(fgkod3max)):
              if KOD[i] == fgkod3max[j]:
                      if KOD[i] == fgkod3max2[0] or KOD[i] == fgkod3max3[0] or KOD[i] == fgkod3max4[0]:
                          if notrepeat != 0:
                              notrepeat = notrepeat - 1
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
                      elif KOD[i] == fgkod3max5[0] or KOD[i] == fgkod3max6[0] or KOD[i] == fgkod3max7[0]:
                          if notrepeat2 != 0:
                              notrepeat2 = notrepeat2 - 1
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
                      elif KOD[i] == fgkod3max8[0] or KOD[i] == fgkod3max9[0] or KOD[i] == fgkod3max10[0] or KOD[i] == fgkod3max11[0] or KOD[i] == fgkod3max12[0]:
                          if notrepeat3 != 0:
                              notrepeat3 = notrepeat3 - 1
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
                      else:
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
    else:
      for i in range(len(KOD)):
          for j in range(len(fgkod3max)):
              if KOD[i] == fgkod3max[j] and KOD[i] != 'В 01.066.001':
                      if KOD[i] == fgkod3max2[0] or KOD[i] == fgkod3max3[0] or KOD[i] == fgkod3max4[0]:
                          if notrepeat != 0:
                              notrepeat = notrepeat - 1
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
                      elif KOD[i] == fgkod3max5[0] or KOD[i] == fgkod3max6[0] or KOD[i] == fgkod3max7[0]:
                          if notrepeat2 != 0:
                              notrepeat2 = notrepeat2 - 1
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
                      elif KOD[i] == fgkod3max8[0] or KOD[i] == fgkod3max9[0] or KOD[i] == fgkod3max10[0] or KOD[i] == fgkod3max11[0] or KOD[i] == fgkod3max12[0]:
                          if notrepeat3 != 0:
                              notrepeat3 = notrepeat3 - 1
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
                      else:
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
    nopovtor2 = nopovtor2+1



def fourmin(KOD,TARIF,patient,localsummin,localcountmin):
    global summin
    global chillmin
    global nopovtor
    global nopovtor2
    notrepeat = 2
    notrepeat2 = 1
    if nopovtor==0:
      for i in range(len(KOD)):
          for j in range(len(fgkod4min)):
              if KOD[i] == fgkod4min[j]:
                      if KOD[i] == fgkod4min2[0] or KOD[i] == fgkod4min3[0] or KOD[i] == fgkod4min4[0]:
                          if notrepeat != 0:
                              notrepeat = notrepeat - 1
                              summin = summin + TARIF[i]
                              chillmin = chillmin + 1
                              localsummin[patient] = localsummin[patient] + TARIF[i]
                              localcountmin[i] = localcountmin[i] + 1
                      elif KOD[i] == fgkod4min5[0] or KOD[i] == fgkod4min6[0] or KOD[i] == fgkod4min7[0]:
                          if notrepeat2 != 0:
                              notrepeat2 = notrepeat2 - 1
                              summin = summin + TARIF[i]
                              chillmin = chillmin + 1
                              localsummin[patient] = localsummin[patient] + TARIF[i]
                              localcountmin[i] = localcountmin[i] + 1
                      else:
                          chillmin = chillmin + 1
                          summin = summin + TARIF[i]
                          localsummin[patient] = localsummin[patient] + TARIF[i]
                          localcountmin[i] = localcountmin[i] + 1
    else:
      for i in range(len(KOD)):
          for j in range(len(fgkod4min)):
              if KOD[i] == fgkod4min[j] and KOD[i] != 'В 01.066.001':
                      if KOD[i] == fgkod4min2[0] or KOD[i] == fgkod4min3[0] or KOD[i] == fgkod4min4[0]:
                          if notrepeat != 0:
                              notrepeat = notrepeat - 1
                              summin = summin + TARIF[i]
                              chillmin = chillmin + 1
                              localsummin[patient] = localsummin[patient] + TARIF[i]
                              localcountmin[i] = localcountmin[i] + 1
                      elif KOD[i] == fgkod4min5[0] or KOD[i] == fgkod4min6[0] or KOD[i] == fgkod4min7[0]:
                          if notrepeat2 != 0:
                              notrepeat2 = notrepeat2 - 1
                              summin = summin + TARIF[i]
                              chillmin = chillmin + 1
                              localsummin[patient] = localsummin[patient] + TARIF[i]
                              localcountmin[i] = localcountmin[i] + 1
                      else:
                          chillmin = chillmin + 1
                          summin = summin + TARIF[i]
                          localsummin[patient] = localsummin[patient] + TARIF[i]
                          localcountmin[i] = localcountmin[i] + 1
    nopovtor = nopovtor+1
def fourmax(KOD,TARIF,patient,localsummax,localcountmax):
    global summax
    global chillmax
    global nopovtor
    global nopovtor2
    notrepeat = 2
    notrepeat2 = 1
    if nopovtor2==0:

      for i in range(len(KOD)):
          for j in range(len(fgkod4max)):
              if KOD[i] == fgkod4max[j]:
                  if KOD[i] == fgkod4max2[0] or KOD[i] == fgkod4max3[0] or KOD[i] == fgkod4max4[0]:
                          if notrepeat != 0:
                              notrepeat = notrepeat - 1
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
                  elif KOD[i] == fgkod4max5[0] or KOD[i] == fgkod4max6[0] or KOD[i] == fgkod4max7[0] or KOD[i] == fgkod4max8[0] or KOD[i] == fgkod4max9[0]:
                          if notrepeat2 != 0:
                              notrepeat2 = notrepeat2 - 1
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
                  else:
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
    else:
      for i in range(len(KOD)):
          for j in range(len(fgkod4max)):
              if KOD[i] == fgkod4max[j] and KOD[i] != 'В 01.066.001':
                  if KOD[i] == fgkod4max2[0] or KOD[i] == fgkod4max3[0] or KOD[i] == fgkod4max4[0]:
                          if notrepeat != 0:
                              notrepeat = notrepeat - 1
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
                  elif KOD[i] == fgkod4max5[0] or KOD[i] == fgkod4max6[0] or KOD[i] == fgkod4max7[0] or KOD[i] == fgkod4max8[0] or KOD[i] == fgkod4max9[0]:
                          if notrepeat2 != 0:
                              notrepeat2 = notrepeat2 - 1
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
                  else:
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
    nopovtor2 = nopovtor2+1
def fivemin(KOD,TARIF,patient,localsummin,localcountmin):
    global summin
    global chillmin
    global nopovtor
    global nopovtor2
    notrepeat = 1
    if nopovtor==0:
     for i in range(len(KOD)):
         for j in range(len(fgkod5min)):
             if KOD[i] == fgkod5min[j]:
                     if KOD[i] == fgkod5min2[0] or KOD[i] == fgkod5min3[0] or KOD[i] == fgkod5min4[0]:
                         if notrepeat != 0:
                             notrepeat = notrepeat - 1
                             summin = summin + TARIF[i]
                             chillmin = chillmin + 1
                             localsummin[patient] = localsummin[patient] + TARIF[i]
                             localcountmin[i] = localcountmin[i] + 1
                     else:
                             summin = summin + TARIF[i]
                             chillmin = chillmin + 1
                             localsummin[patient] = localsummin[patient] + TARIF[i]
                             localcountmin[i] = localcountmin[i] + 1
    else:
     for i in range(len(KOD)):
         for j in range(len(fgkod5min)):
             if KOD[i] == fgkod5min[j] and KOD[i] != 'В 01.066.001':
                     if KOD[i] == fgkod5min2[0] or KOD[i] == fgkod5min3[0] or KOD[i] == fgkod5min4[0]:
                         if notrepeat != 0:
                             notrepeat = notrepeat - 1
                             summin = summin + TARIF[i]
                             chillmin = chillmin + 1
                             localsummin[patient] = localsummin[patient] + TARIF[i]
                             localcountmin[i] = localcountmin[i] + 1
                     else:
                             summin = summin + TARIF[i]
                             chillmin = chillmin + 1
                             localsummin[patient] = localsummin[patient] + TARIF[i]
                             localcountmin[i] = localcountmin[i] + 1
    nopovtor = nopovtor+1
def fivemax(KOD,TARIF,patient,localsummax,localcountmax):
    global summax
    global chillmax
    global nopovtor
    global nopovtor2
    notrepeat = 1
    if nopovtor2==0:
      for i in range(len(KOD)):
          for j in range(len(fgkod5max)):
              if KOD[i] == fgkod5max[j]:
                      if KOD[i] == fgkod5max2[0] or KOD[i] == fgkod5max3[0] or KOD[i] == fgkod5max4[0]:
                          if notrepeat != 0:
                              notrepeat = notrepeat - 1
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i]+1
                      else:
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
    else:
      for i in range(len(KOD)):
          for j in range(len(fgkod5max)):
              if KOD[i] == fgkod5max[j] and KOD[i] != 'В 01.066.001':
                      if KOD[i] == fgkod5max2[0] or KOD[i] == fgkod5max3[0] or KOD[i] == fgkod5max4[0]:
                          if notrepeat != 0:
                              notrepeat = notrepeat - 1
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i]+1
                      else:
                              summax = summax + TARIF[i]
                              chillmax = chillmax + 1
                              localsummax[patient] = localsummax[patient] + TARIF[i]
                              localcountmax[i] = localcountmax[i] + 1
    nopovtor2 = nopovtor2+1
def calculate(classc,KOD,TARIF,localsummin,localsummax,Name,localcountmin,ffio,localcountmax):
    global dfert
    global Names
    global TariFF
    global mincount
    global maxcount
    global fio
    global nopovtor
    global nopovtor2
    TariFF = pd.DataFrame(TARIF)
    dfert = pd.DataFrame(KOD)
    Names = pd.DataFrame(Name)
    fio = pd.DataFrame(ffio)
    print("erweqrr")
    print(Names)
    print("erweqrr")
    for i in range(len(classc)):
        patient = i
        if classc[i] == 11:
          if nopovtor==0 and nopovtor2==0:
            onemin(KOD,TARIF,patient,localsummin,localcountmin[i])
            onemax(KOD,TARIF,patient,localsummax,localcountmax[i])
            nopovtor=0
            nopovtor2=0
        if classc[i] == 12:
          if nopovtor==0 and nopovtor2==0:
            twomin(KOD,TARIF,patient,localsummin,localcountmin[i])
            twomax(KOD,TARIF,patient,localsummax,localcountmax[i])
            nopovtor=0
            nopovtor2=0
        if classc[i] == 13:
          if nopovtor==0 and nopovtor2==0:
            threemin(KOD,TARIF,patient,localsummin,localcountmin[i])
            threemax(KOD,TARIF,patient,localsummax,localcountmax[i])
            nopovtor=0
            nopovtor2=0
        if classc[i] == 14:
          if nopovtor==0 and nopovtor2==0:
            fourmin(KOD,TARIF,patient,localsummin,localcountmin[i])
            fourmax(KOD,TARIF,patient,localsummax,localcountmax[i])
            nopovtor=0
            nopovtor2=0
        if classc[i] == 15:
          if nopovtor==0 and nopovtor2==0:
            fivemin(KOD,TARIF,patient,localsummin,localcountmin[i])
            fivemax(KOD,TARIF,patient,localsummax,localcountmax[i])
            nopovtor=0
            nopovtor2=0
        if classc[i] == 21:
          if nopovtor==0 and nopovtor2==0:
            twomin(KOD,TARIF,patient,localsummin,localcountmin[i])
            twomax(KOD,TARIF,patient,localsummax,localcountmax[i])
            nopovtor=0
            nopovtor2=0
        if classc[i] == 22:
          if nopovtor==0 and nopovtor2==0:
            twomin(KOD,TARIF,patient,localsummin,localcountmin[i])
            twomax(KOD,TARIF,patient,localsummax,localcountmax[i])
          if nopovtor==1 and nopovtor2==1:
            twomin(KOD,TARIF,patient,localsummin,localcountmin[i])
            twomax(KOD,TARIF,patient,localsummax,localcountmax[i])
            nopovtor=0
            nopovtor2=0

        if classc[i] == 23:
          if nopovtor==0 and nopovtor2==0:
            twomin(KOD,TARIF,patient,localsummin,localcountmin[i])
            twomax(KOD,TARIF,patient,localsummax,localcountmax[i])
            if nopovtor==1 and nopovtor2==1:
              threemin(KOD,TARIF,patient,localsummin,localcountmin[i])
              threemax(KOD,TARIF,patient,localsummax,localcountmax[i])
              nopovtor=0
              nopovtor2=0
        if classc[i] == 24:
          if nopovtor==0 and nopovtor2==0:
            twomin(KOD,TARIF,patient,localsummin,localcountmin[i])
            twomax(KOD,TARIF,patient,localsummax,localcountmax[i])
            if nopovtor==1 and nopovtor2==1:
              fourmin(KOD,TARIF,patient,localsummin,localcountmin[i])
              fourmax(KOD,TARIF,patient,localsummax,localcountmax[i])
              nopovtor=0
              nopovtor2=0
        if classc[i] == 25:
          if nopovtor==0 and nopovtor2==0:
            twomin(KOD,TARIF,patient,localsummin,localcountmin[i])
            twomax(KOD,TARIF,patient,localsummax,localcountmax[i])
            if nopovtor==1 and nopovtor2==1:
              fivemin(KOD,TARIF,patient,localsummin,localcountmin[i])
              fivemax(KOD,TARIF,patient,localsummax,localcountmax[i])
              nopovtor=0
              nopovtor2=0
        if classc[i] == 31:
          if nopovtor==0 and nopovtor2==0:
            threemin(KOD,TARIF,patient,localsummin,localcountmin[i])
            threemax(KOD,TARIF,patient,localsummax,localcountmax[i])
            nopovtor=0
            nopovtor2=0
        if classc[i] == 32:
          if nopovtor==0 and nopovtor2==0:
            threemin(KOD,TARIF,patient,localsummin,localcountmin[i])
            threemax(KOD,TARIF,patient,localsummax,localcountmax[i])
            if nopovtor==1 and nopovtor2==1:
              twomin(KOD,TARIF,patient,localsummin,localcountmin[i])
              twomax(KOD,TARIF,patient,localsummax,localcountmax[i])
              nopovtor=0
              nopovtor2=0
        if classc[i] == 33:
          if nopovtor==0 and nopovtor2==0:
            threemin(KOD,TARIF,patient,localsummin,localcountmin[i])
            threemax(KOD,TARIF,patient,localsummax,localcountmax[i])
            if nopovtor==1 and nopovtor2==1:
              threemin(KOD,TARIF,patient,localsummin,localcountmin[i])
              threemax(KOD,TARIF,patient,localsummax,localcountmax[i])
              nopovtor=0
              nopovtor2=0
        if classc[i] == 34:
          if nopovtor==0 and nopovtor2==0:
            threemin(KOD,TARIF,patient,localsummin,localcountmin[i])
            threemax(KOD,TARIF,patient,localsummax,localcountmax[i])
            if nopovtor==1 and nopovtor2==1:
              fourmin(KOD,TARIF,patient,localsummin,localcountmin[i])
              fourmax(KOD,TARIF,patient,localsummax,localcountmax[i])
              nopovtor=0
              nopovtor2=0
        if classc[i] == 35:
          if nopovtor==0 and nopovtor2==0:
            threemin(KOD,TARIF,patient,localsummin,localcountmin[i])
            threemax(KOD,TARIF,patient,localsummax,localcountmax[i])
            if nopovtor==1 and nopovtor2==1:
              fivemin(KOD,TARIF,patient,localsummin,localcountmin[i])
              fivemax(KOD,TARIF,patient,localsummax,localcountmax[i])
              nopovtor=0
              nopovtor2=0
        if classc[i] == 41:
          if nopovtor==0 and nopovtor2==0:
            fourmin(KOD,TARIF,patient,localsummin,localcountmin[i])
            fourmax(KOD,TARIF,patient,localsummax,localcountmax[i])
            nopovtor=0
            nopovtor2=0
        if classc[i] == 42:
          if nopovtor==0 and nopovtor2==0:
            fourmin(KOD,TARIF,patient,localsummin,localcountmin[i])
            fourmax(KOD,TARIF,patient,localsummax,localcountmax[i])
            if nopovtor==1 and nopovtor2==1:
              twomin(KOD,TARIF,patient,localsummin,localcountmin[i])
              twomax(KOD,TARIF,patient,localsummax,localcountmax[i])
              nopovtor=0
              nopovtor2=0
        if classc[i] == 43:
          if nopovtor==0 and nopovtor2==0:
            fourmin(KOD,TARIF,patient,localsummin,localcountmin[i])
            fourmax(KOD,TARIF,patient,localsummax,localcountmax[i])
            if nopovtor==1 and nopovtor2==1:
              threemin(KOD,TARIF,patient,localsummin,localcountmin[i])
              threemax(KOD,TARIF,patient,localsummax,localcountmax[i])
              nopovtor=0
              nopovtor2=0
        if classc[i] == 44:
          if nopovtor==0 and nopovtor2==0:
            fourmin(KOD,TARIF,patient,localsummin,localcountmin[i])
            fourmax(KOD,TARIF,patient,localsummax,localcountmax[i])
            if nopovtor==1 and nopovtor2==1:
              fourmin(KOD,TARIF,patient,localsummin,localcountmin[i])
              fourmax(KOD,TARIF,patient,localsummax,localcountmax[i])
              nopovtor=0
              nopovtor2=0
        if classc[i] == 45:
          if nopovtor==0 and nopovtor2==0:
            fourmin(KOD,TARIF,patient,localsummin,localcountmin[i])
            fourmax(KOD,TARIF,patient,localsummax,localcountmax[i])
            if nopovtor==1 and nopovtor2==1:
              fivemin(KOD,TARIF,patient,localsummin,localcountmin[i])
              fivemax(KOD,TARIF,patient,localsummax,localcountmax[i])
              nopovtor=0
              nopovtor2=0
        if classc[i] == 51:
          if nopovtor==0 and nopovtor2==0:
            fivemin(KOD,TARIF,patient,localsummin,localcountmin[i])
            fivemax(KOD,TARIF,patient,localsummax,localcountmax[i])
            nopovtor=0
            nopovtor2=0
        if classc[i] == 52:
          if nopovtor==0 and nopovtor2==0:
            fivemin(KOD,TARIF,patient,localsummin,localcountmin[i])
            fivemax(KOD,TARIF,patient,localsummax,localcountmax[i])
            if nopovtor==1 and nopovtor2==1:
              twomin(KOD,TARIF,patient,localsummin,localcountmin[i])
              twomax(KOD,TARIF,patient,localsummax,localcountmax[i])
              nopovtor=0
              nopovtor2=0
        if classc[i] == 53:
          if nopovtor==0 and nopovtor2==0:
            fivemin(KOD,TARIF,patient,localsummin,localcountmin[i])
            fivemax(KOD,TARIF,patient,localsummax,localcountmax[i])
            if nopovtor==1 and nopovtor2==1:
              threemin(KOD,TARIF,patient,localsummin,localcountmin[i])
              threemax(KOD,TARIF,patient,localsummax,localcountmax[i])
              nopovtor=0
              nopovtor2=0
        if classc[i] == 54:
          if nopovtor==0 and nopovtor2==0:
            fivemin(KOD,TARIF,patient,localsummin,localcountmin[i])
            fivemax(KOD,TARIF,patient,localsummax,localcountmax[i])
            if nopovtor==1 and nopovtor2==1:
              fourmin(KOD,TARIF,patient,localsummin,localcountmin[i])
              fourmax(KOD,TARIF,patient,localsummax,localcountmax[i])
              nopovtor=0
              nopovtor2=0
        if classc[i] == 55:
          if nopovtor==0 and nopovtor2==0:
            fivemin(KOD,TARIF,patient,localsummin,localcountmin[i])
            fivemax(KOD,TARIF,patient,localsummax,localcountmax[i])
            if nopovtor==1 and nopovtor2==1:
              fivemin(KOD,TARIF,patient,localsummin,localcountmin[i])
              fivemax(KOD,TARIF,patient,localsummax,localcountmax[i])
              nopovtor=0
              nopovtor2=0


    mincount = pd.DataFrame(localcountmin)
    maxcount = pd.DataFrame(localcountmax)
    mincount = mincount.T
    maxcount = maxcount.T
    for i in range(len(localcountmax)):
        localcountmin[i] = 0
        localcountmax[i] = 0

    return summin,summax,chillmin,chillmax,localsummin,localsummax,dfert, Names, TariFF, mincount, fio, maxcount
