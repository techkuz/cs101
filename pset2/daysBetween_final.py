# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
def isLeapYear(year):
   
    if year % 4 != 0:
        return False
      
    if year % 100 != 0:
        return True
       
    if year % 400 != 0:
        return False
       
    return True
       

def numberOfDaysInMonth(year, month):
    amountOfDays = 0
    
    if month == 1:
        amountOfDays = 31
    if month == 2:
        if isLeapYear(year) == True:
            amountOfDays = 29
        else:
            amountOfDays = 28
    if month == 3:
        amountOfDays = 31
    if month == 4:
        amountOfDays = 30    
    if month == 5:
        amountOfDays = 31    
    if month == 6:
        amountOfDays = 30
    if month == 7:
        amountOfDays = 31
    if month == 8:
        amountOfDays = 31
    if month == 9:
        amountOfDays = 30
    if month == 10:
        amountOfDays = 31
    if month == 11:
        amountOfDays = 30
    if month == 12:
        amountOfDays = 31
    
    return amountOfDays
            
        
def numberOfDays(year, month, day):
    n = 1
    result_days = 0
    while n != month:
        result_days = result_days + numberOfDaysInMonth(year, n)
        n = n + 1
        
    return result_days + day
    

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    if year2 == year1:
        
        return numberOfDays(year2, month2, day2) - numberOfDays(year1, month1, day1)
    else:
        n = year1
        total_days = 0
        while n != year2:
            total_days = total_days + numberOfDays(n, 12, 31)
            n = n + 1
        
        return total_days + numberOfDays(year2, month2, day2) - numberOfDays(year1, month1, day1)


# Test routine


def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
