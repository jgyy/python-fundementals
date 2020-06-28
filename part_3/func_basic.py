def is_year_leap(year):
    return year % 4 == 0

def days_in_month(year,month):
    leap = 1 if is_year_leap(year) else 0
    dim = {
        1: 31, 2: 28 + leap, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    return dim.get(month)

def day_of_year(year,month,day):
    days = day
    for i in range(1, month):
        days += days_in_month(year, i)
    return days

print(day_of_year(2000,12,31))

testyears = [1900, 2000, 2016, 1987]
testmonths = [ 2, 2, 1, 11]
testresults = [28, 29, 31, 30]
for i in range(len(testyears)):
    yr = testyears[i]
    mo = testmonths[i]
    print(yr,mo,"->",end="")
    result = days_in_month(yr,mo)
    if result == testresults[i]:
        print("OK")
    else:
        print("Failed")
