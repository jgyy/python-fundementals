def is_year_leap(year):
    return year % 4 == 0

testdata = [1900, 2000, 2016, 1987]
testresults = [False, True, True, False]

for i in range(len(testdata)):
    yr = testdata[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == testresults[i]:
        print("OK")
    else:
        print("Failed")
