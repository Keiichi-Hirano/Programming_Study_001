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
        fo = open(O_files, 'w',encoding="utf-8_sig")
        writer = csv.writer(fo, lineterminator='\n')
#        for row in reader:
        for i, row in enumerate(reader):
                if i == 0:
                        #Hearder 編集
                        new = ["Date"]
                        new.extend(row)
                        writer.writerow(new)
                        continue                        
                for number in range(129):
                        # 金額項目の小数点５桁以下の四捨五入
                        if number >= 40 and number < 128 and row[number] != "":
                                row[number] = round(float(row[number]),5)
                        # テキスト項目の記号文字の除外
                        elif number >= 23 or ( number >= 5 and number <= 8 ):
                                row[number] = row[number].translate(str.maketrans( '', '',string.punctuation))
                        # 日付の編集
                        elif number == 0:
                                new = [row[0]+"-"+row[1]+"-01"]
                new.extend(row)
                writer.writerow(new)
        f.close()
        fo.close()

def main():
 I_file = 'C:/Users/js0059/Clickhouse/Original_Data/utf_test.txt.csv'
 O_file = 'C:/Users/js0059/Clickhouse/Original_Data/test_out.csv'
 trance(I_file,O_file)

if __name__ == '__main__':
        main()
