# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:10:26 2022
Edited on Fri Sep 9 08:43:00 2022

@author: kristoferpelletier
"""
from datetime import date, timedelta
#from enum import IntEnum
#import time
import calendar
#from dateutil.relativedelta import relativedelta


monthweekstarts = [0,4,9,13,17,22,26,30,35,39,43,48]

quarterstarts = [0,13,26,39]


def LeapYearCheck(yr):
    '''
    CHECKS WHETHER OR NOT THE CURRENT LOWES 
    FISCAL YEAR IS A LEAP YEAR

    Parameters
    ----------
    yr : Int
        THE LOWES FISCAL YEAR

    Returns
    -------
    bool
        IS LEAP YEAR OR IS NOT LEAP YEAR.

    '''
    if (yr % 4) == 0: 
        if (yr % 100) == 0: 
            if (yr % 400) == 0: 
                return True
            else: 
                return False
        else: 
             return True
    else: 
        return False
    
def WeeksintheYear(dte):
    '''
    CALCULATES THE AMOUNT OF WEEKS IN THE LOWES FISCAL YEAR

    Parameters
    ----------
    dte : DATE
        TAKES A DATE IT IS CREATED TO USE FEB 1.

    Returns
    -------
    int
        THE NUMBER OF WEEKS.

    '''
    weekday = (dte.weekday()+2)%7
    #print('weekday =', weekday)
    leapyear = LeapYearCheck(dte.year)
    #print('leapyear:', leapyear)
    
    if leapyear:
        if weekday == 2:
            return 53
        else:
            return 52
    else:
        if weekday == 3:
            return 53
        else:
            return 52     


def smallest_dayinfebfirstweek(year):
    '''
    TAKES THE YEAR AND GIVES BACK THE  FIRST DAY OF FEBRUARY
    IN THE LOWES FISCALYEAR

    Parameters
    ----------
    year : INT
        THE FISCAL YEAR IN QUESTION.

    Returns
    -------
    firstday : INT
        THE FIRST OF FEB IN THE CURRENT FISCAL YEAR.

    '''
    lastyear = year - 1
    febfirst = date(year,2,1)
    febfirstweekday = febfirst.weekday()
    firstday = 1
    if (febfirstweekday >= 3 and febfirstweekday <= 5) or WeeksintheYear(date(lastyear,2,1)) == 53:
        firstday = firstday + (5-febfirstweekday)    
    return firstday


def first_fiscalday(year, day):
    '''
    RETURNS THE FIRST DAY OF THE FISCAL YEAR

    Parameters
    ----------
    year : INT
        FISCAL YEAR.
    day : INT
        TAKES THE SMALLES DAY IN FEBRUARY DURING THE CURRENT 
        FISCAL YEAR.

    Returns
    -------
    start : DATE
        RETURNS THE DATE OF THE FIRST DAY OF THE FISCAL YEAR.

    '''
    today = date(year,2,day)
    start = today - timedelta(days=(today.weekday()+2)%7)
    return start

def firstdayofweek(dte):
    '''
    GIVEN A DATE, RETURN THE FIRST DAY OF THAT WEEK

    Parameters
    ----------
    dte : DATE
        A DATE THAT IS IN QUESTION.

    Returns
    -------
    start : DATE
        THE FIRST DAY OF THE WEEK THE GIVEN DATE FALLS IN.

    '''
    start = dte - timedelta(days=(dte.weekday()+2)%7)
    return start

def lastdayofweek(dte):
    '''
    GIVEN A DATE, RETURN THE LAST DAY OF THAT WEEK

    Parameters
    ----------
    dte : DATE
        A DATE THAT IS IN QUESTION.

    Returns
    -------
    end : DATE
        THE LAST DAY OF THE WEEK THE GIVEN DATE FALLS IN.

    '''
    start = firstdayofweek(dte)
    end = start + timedelta(days=6)
    return end

def last_day_of_month(dte): 
    '''
    RETURNS THE LAST DAY OF THE MONTH OF THE DATE

    Parameters
    ----------
    dte : DATE
        THE DATE IN QUESTION.

    Returns
    -------
    DATE
        THE LAST DAY OF THE MONTH THAT THE GIVEN DATE
        FALLS IN.

    '''
    last_day = calendar.monthrange(dte.year, dte.month)[1]    
    return date(dte.year,dte.month,last_day)

def fiscal_year(dte): 
    '''
    RETURNS THE FISCAL YEAR OF THE GIVEN DATE

    Parameters
    ----------
    dte : DATE
        THE DATE IN QUESTION.

    Returns
    -------
    INT
        THE FISCAL YEAR THAT THE GIVEN DATE FALLS IN.

    '''
    thisyear = dte.year 
    
    lastyear = thisyear - 1
    
    
    smallestthisyearfeb = smallest_dayinfebfirstweek(thisyear)
    firstofyear = first_fiscalday(thisyear, smallestthisyearfeb)
    
    if dte.month == 1:
        
        #end_of_month = last_day_of_month(dte)
        #lastdaycheck = lastdayofweek(end_of_month)
        if dte < firstofyear:#lastdaycheck >= date(thisyear,1,31) and lastdaycheck <= date(thisyear,2,3):
            return lastyear
        else:
            return thisyear
    elif dte.month == 2:
        checkday = date(dte.year,2,smallest_dayinfebfirstweek(thisyear))
        if dte >= checkday:
            return thisyear
        else:
            return lastyear
    else:
        return thisyear

def last_week_date(dte):
    '''
    WHEN GIVEN A DATE, GIVES THE CORRESPONDING DATE FROM LAST WEEK

    Parameters
    ----------
    dte : DATE
        GIVEN DATE.

    Returns
    -------
    DATE
        THE CORRESPONDING DATE LAST WEEK.

    '''
    return dte - timedelta(days=7)




def lyWeekstartdate(dte):
    '''
    RETURNS THE FIRST DAY OF THE WEEK LAST YEAR THAT 
    CORRESPONDS WITH THE WEEK THAT IS BEING REPORTED ON.

    Parameters
    ----------
    dte : DATE
        THE DATE IN QUESTION.

    Returns
    -------
    DATE
        FIRST DAY OF THE CORRESPONDING WEEK FROM LAST YEAR.

    '''
    firstofweek = last_week_date(firstdayofweek(dte))
    lydayoffset = firstofweek - timedelta(days=52*7)
    return firstdayofweek(lydayoffset)

def lyWeekenddate(dte):
    '''
    RETURNS THE LAST DAY OF THE CORRESPONDING WEEK FROM
    LAST YEAR

    Parameters
    ----------
    dte : DATE
        THE DATE IN QUESTION.

    Returns
    -------
    DATE
        THE LAST DAY OF THE CORRESPONDING WEEK FROM
        LAST YEAR.

    '''
    firstofweek = last_week_date(firstdayofweek(dte))
    lydayoffset = firstofweek - timedelta(days=52*7)
    return lastdayofweek(lydayoffset)

def first_lastyear(dte):
    '''
    RETURNS THE FIRST DAY OF THE PREVIOUS FISCAL YEAR

    Parameters
    ----------
    dte : DATE
        THE DATE IN QUESTION.

    Returns
    -------
    DATE
        THE FIRST DAY OF THE PREVIOUS FISCAL YEAR.

    '''
    fiscalyear = fiscal_year(dte) - 1
    return first_fiscalday(fiscalyear, smallest_dayinfebfirstweek(fiscalyear))


def howmanyweeksthisyear(dte):
    
    fiscalyear = fiscal_year(dte)
    febday = smallest_dayinfebfirstweek(fiscalyear)
    return(WeeksintheYear(date(fiscalyear, 2 , febday)))
    


def first_day_this_year(dte):
    
    fiscalyear = fiscal_year(dte)
    return first_fiscalday(fiscalyear, smallest_dayinfebfirstweek(fiscalyear))


def first_date(granularity, dte):
    '''
    RETURNS THE FIRST DATE OF A GIVEN GRANULARITY
    Parameters
    ----------
    granularity : STRING
        THREE CHOICES ['year', 'quarter', month]
    dte : DATE
        GIVEN DATE.

    Returns
    -------
    DATE
        THE FIRST DATE OF A GIVEN GRANULARITY

    '''
    d1 =  first_day_this_year(dte)
    
    if granularity == 'year':
        return d1
    elif granularity in ('quarter', 'month'):
        d2 = firstdayofweek(dte)    
        daydiff = (d2 - d1).days
        dayby7 = (daydiff / 7)        
        if granularity == 'quarter':
            quarterstarts.sort(reverse=True)
            qtrstartweek = min(quarterstarts, key=lambda x: x - dayby7 >0)
            return d1 + timedelta(days=7 * qtrstartweek)
        elif granularity == 'month':
            monthweekstarts.sort(reverse=True)
            monthstartweek = min(monthweekstarts, key=lambda x: x - dayby7 >0)
            return d1 + timedelta(days=7 * monthstartweek)



#print(last_week_date(lastdayofweek(date.today())))
'''  
print('+++_+++_+++_+++_+++_+++') 
for i in range(1, 13):
    dte = date(2022, i, 1)
    print('Date =', dte)
    print()
    print('first of year =', first_date('year', dte))
    print('first of quarter =', first_date('quarter', dte))
    print('first of month =', first_date('month', dte))
    print('===============================')
    
print(first_day_this_year(date(2022,1,1)))

'''

