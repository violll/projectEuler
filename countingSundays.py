from datetime import *

# solution 1
def getSundays(start, end):
    count = 0
    y, m, d = start
    dow = ["Su", "M", "T", "W", "H", "F", "Sa"]

    for y in range(start[0], end[0]+1):
        for m in range(start[1], end[1]+1):
            if dow[(date(y,m,d).weekday()+1)%7] == "Su": count += 1
    return count

# print(getSundays([1901, 1, 1], [2000, 12, 31], 1))

# solution 2
def getSundays(start, end):
    y = start.year
    m = start.month
    count = 0
    currDate = start

    while currDate < end:
        if currDate.weekday() == 6: count += 1
        m += 1
        if m > 12:
            m = 1
            y += 1
        currDate = currDate.replace(year = y, month=m)
    return count

startDate = date(1901, 1, 1)
endDate = date(2000, 12, 31)
# print(getSundays(startDate, endDate))