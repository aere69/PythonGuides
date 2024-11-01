def is_leap_year(year):
    """Takes a year and returns True if Leap Year, False if not"""
    
    # Is divisible by 4 with no reminder
    condition_1 = (year%4) == 0
    # Is divisible by 100 with no reminder
    condition_2 = (year%100) == 0
    # Is divisible by 400 with no reminder
    condition_3 = (year%400) == 0
    
    leap = condition_1 and (not condition_2 or condition_3)
    return leap
    
print(is_leap_year(2100))