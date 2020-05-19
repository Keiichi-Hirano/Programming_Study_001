#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#! /usr/bin/env python
import pygeohash as pgh
#pgh.encode(42.6, -5.6) # >>> 'ezs42e44yx96'
#pgh.encode(42.6, -5.6, precision=5) # >>> 'ezs42'
#print(pgh.decode('ezs42'))
# >>> ('42.6', '-5.6')
#pgh.geohash_approximate_distance('bcd3u', 'bc83n') # >>> 625441\
import csv
import pprint

I_files = 'C:/Users/js0059/OneDrive - Coca-Cola Bottlers Japan/_MarkLogic/_Memos/VM_Tableau/Csv/xn76us_t_ccaa_dm_foot_traffic_par_p_201911191332_test.csv'
O_files = 'C:/Users/js0059/OneDrive - Coca-Cola Bottlers Japan/_MarkLogic/_Memos/VM_Tableau/Csv/Gro_transfor.csv'

f = open(I_files, 'r')

reader = csv.reader(f)
header = next(reader)
#for row in reader:
#        writea = pgh.decode(row[0])
#        print ("{},{}".format(writea,row))

fo = open(O_files, 'w')

writer = csv.writer(fo, lineterminator='\n')
for row in reader:
        writea = pgh.decode(row[0])
#        print ("{},{}".format(writea,row))
#        print(writea) 
        row.append(pgh.decode(row[0])[0])
        row.append(pgh.decode(row[0])[1])
        writer.writerow(row)
        #writer.writerows(array2d)

f.close()
fo.close()
#################################
#with open(I_files) as f:
##with open(O_files, 'w') as fo:
#
#    reader = csv.reader(f)
#    for row in reader:
#        writea = pgh.decode(row[0])
#        print ("{},{}".format(writea,row))
##        writer = csv.writer(fo)
##        writer.writerows(l)
#