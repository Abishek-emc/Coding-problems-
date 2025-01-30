"""Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.
Example 1:
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:
Input: date = "2019-02-10"
Output: 41"""
date = "2019-02-10"
d = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
day =int(date[-2:])
month = int(date[5:7])
total = 0
for i in range(1,month):
    total = total + d[i]
total = total + day
print(total)