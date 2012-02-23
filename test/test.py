#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2012 Jaemok Jeong(jmjeong@gmail.com)
#
# [2012/02/23]


import transdate_nounicode
from  datetime import date
import os, locale

lun2solprogram = "./lun2sol "

def lunarprogram(year, month, day, leap):
    if not leap:
        leap = 0
    else:
        leap = 1
        
    program = '%s %d %d %d %d' % (lun2solprogram,year,month,day,leap)
    f = os.popen(program)
    f.close
        
    return map(int, f.readline().split())

def main():
    mindate = transdate_nounicode._MINDATE
    maxdate = transdate_nounicode._MAXDATE


    # for i in range(mindate,maxdate):
    for i in range(mindate,maxdate):
        
        d = date.fromordinal(i).timetuple()[:3]
        lunar = transdate_nounicode.sol2lun(d[0],d[1],d[2])
        # print lunar

        solar = transdate_nounicode.lun2sol(lunar[0], lunar[1], lunar[2], lunar[3])
        print solar
        assert(d == solar[:3])

        csolar =  lunarprogram(lunar[0], lunar[1], lunar[2], lunar[3])
        # print list(solar[:3]), csolar
        assert(list(solar[:3]) == csolar)

if __name__ == '__main__':
    main()
