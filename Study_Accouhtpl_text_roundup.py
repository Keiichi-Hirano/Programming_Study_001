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
import string
#import re
        
def trance(I_files,O_files):
#
        f = open(I_files, 'r',encoding="utf-8_sig")

        reader = csv.reader(f)
        #header = next(reader)
        #for row in reader:
        #        writea = pgh.decode(row[0])
        #        print ("{},{}".format(writea,row))
        # text = 'Abcd1!EfgH"#$%2s&\'I()j*5k+,-./:l;MMM<=>NNN?@[\Z]^_`{99|00}7~8'
        #table = str.maketrans( '', '', '\"()<>[]{}')

        #fo = open(O_files, 'w')
        fo = open(O_files, 'w',encoding="utf-8_sig")

        writer = csv.writer(fo, lineterminator='\n')
#        for row in reader:
        for i, row in enumerate(reader):
                if i == 0:
                        new = ["Date"]
                        new.extend(row)
                        writer.writerow(new)
                        continue                        
#                for number in range(130):
                for number in range(129):
        #                if str.isdigit(row[number]) == True and number >= 42 and number < 130 and number != 1:
        #                print(number,row[number],type(row[number]))
        #                print(number,row[number],type(row[number]))
        #                if row[number].isdigit() == True and number >= 42 and number < 130:
#                        if number >= 41 and number < 129 and row[number] != "":
                        if number >= 40 and number < 128 and row[number] != "":
        #                        if float(row[number]).isdecimal() == True:
                                row[number] = round(float(row[number]),5)
        #                        row[number] = float(row[number])
        #                        print(number,row[number])
        #                        print(number,row[number],type(row[number]))
#                        elif number >= 24 or ( number >= 6 and number <= 9 ):
                        elif number >= 23 or ( number >= 5 and number <= 8 ):
                                row[number] = row[number].translate(str.maketrans( '', '',string.punctuation))
                        elif number == 0:
                                new = [row[0]+"-"+row[1]+"-01"]
        #                        row[number] = result = re.sub(re.compile("[!-/:-@[-`{-~]"),"",row[number])
        #                        print(result)
        #        writea = pgh.decode(row[0])
        #        print ("{},{}".format(writea,row))
        #        print(writea) 
        #        row.append(pgh.decode(row[0])[0])
        #        row.append(pgh.decode(row[0])[1])
                new.extend(row)
                writer.writerow(new)
                #writer.writerow(row)
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

def main():
 I_file = 'C:/Users/js0059/Clickhouse/Original_Data/utf_test.txt.csv'
 O_file = 'C:/Users/js0059/Clickhouse/Original_Data/test_out.csv'
 trance(I_file,O_file)


# I_file = 'C:/Users/js0059/Clickhouse/201901/test_input.csv'
# O_file = 'C:/Users/js0059/Clickhouse/201901/test_input_output.csv'
# trance(I_file,O_file)

# print('201901')
# I_file = 'C:/Users/js0059/Clickhouse/201901/account_pl_201901_000000_load.csv'
# O_file = 'C:/Users/js0059/Clickhouse/201901/account_pl_201901_000000_round.csv'
# trance(I_file,O_file)

# print('201902')
# I_file = 'C:/Users/js0059/Clickhouse/201901/account_pl_201902_000000_load.csv'
# O_file = 'C:/Users/js0059/Clickhouse/201901/account_pl_201902_000000_round.csv'
# trance(I_file,O_file)
# 
# print('201903')
# I_file = 'C:/Users/js0059/Clickhouse/201901/account_pl_201903_000000_load.csv'
# O_file = 'C:/Users/js0059/Clickhouse/201901/account_pl_201903_000000_round.csv'
# trance(I_file,O_file)
# 
# print('201904')
# I_file = 'C:/Users/js0059/Clickhouse/201901/account_pl_201904_000000_load.csv'
# O_file = 'C:/Users/js0059/Clickhouse/201901/account_pl_201904_000000_round.csv'
# trance(I_file,O_file) 
# 
# print('201905')
# I_file = 'C:/Users/js0059/Clickhouse/201901/account_pl_201905_000000_load.csv'
# O_file = 'C:/Users/js0059/Clickhouse/201901/account_pl_201905_000000_round.csv'
# trance(I_file,O_file)
 
if __name__ == '__main__':
        main()
