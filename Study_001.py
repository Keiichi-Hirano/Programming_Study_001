#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
import sys
from datetime import *
from time import *
import calendar
#! /usr/bin/env python
class Color:
    BLACK     = '\033[30m'
    RED       = '\033[31m'
    BLUE      = '\033[34m'
    GREEN     = '\033[32m'
    YELLOW    = '\033[33m'
    PURPLE    = '\033[35m'
    CYAN      = '\033[36m'
    WHITE     = '\033[37m'
    END       = '\033[0m'
    BOLD      = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE   = '\033[07m'

def def_color(line,l,word):
#
    space = " "
    if line == "H":
        if 0 < l < 6:
         return  Color.WHITE + word + Color.END + space
        elif l == 0:
            return  Color.RED + word + Color.END + space
        elif l == 6:
            return  Color.BLUE + word + Color.END + space
    else:
        if 1 < l < 7:
         return  Color.WHITE + word + Color.END + space
        elif l == 1:
            return  Color.RED + word + Color.END + space
        elif l == 0:
            return  Color.BLUE + word + Color.END + space
#        delta = datetime.datetime.today()
#        _, month_day = calendar.monthrange(delta.year, delta.month)
def main():
#
    print ("年月を入力してください '2016/07'.")
    user_input_date = input("Target Year/Month :")
#
    yobi = ["日","月","火","水","木","金","土"]
# print ("{}は{}曜日です".format(user_input_date,yobi[a.weekday()]))
    space = " "
    header = ""
    while user_input_date != "bye":
        try:
            delta = datetime.strptime(user_input_date,'%Y/%m')
            month_day = calendar.monthrange(delta.year, delta.month)
            dayint = month_day[0] + 1
            print ("{}の月初は{}曜日です".format(user_input_date,yobi[dayint]))
            print ("{}の日数は{}日です".format(user_input_date,month_day[1]))
            print ("--------- {} ---------".format(user_input_date))
            for l in range(7):
                header += def_color("H",l,str(yobi[l])) + space
            print(header)
            #dayint
            line = ""
            for l in range(dayint):
                line += space + space + space + space
            for d in range(1,month_day[1]+1):
                de = ( (dayint + d) % 7 )
                if d < 10:
                    line += space + def_color("M",de,str(d)) + space
                else:
                    line +=def_color("M",de,str(d)) + space
                if de == 0:
                    print (line) 
                    line = ""
            print (line) 
        except ValueError:
            print ("誤った日付です")
        user_input_date = input("your date :")
    else:
        sys.exit(1)

if __name__ == '__main__':
        main()
        
