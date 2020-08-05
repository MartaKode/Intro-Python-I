"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

cal = calendar.TextCalendar()

# monthInput = input('Enter month: ')
# yearInput = input('Enter optional [year]:')

sysArgs = [sys.argv[i] for i in range(len(sys.argv))]
 # print(sysArgs)
currentMonth = datetime.today().month
currentYear = datetime.today().year

if len(sysArgs) == 1:
  print(cal.prmonth(currentYear, currentMonth))
elif len(sysArgs) == 2:
  print(cal.prmonth(currentYear, int(sys.argv[1])))
elif len(sysArgs) == 3:
  print(cal.prmonth(int(sys.argv[2]), int(sys.argv[1])))
else:
  print('Please enter optional month and/or year as integers')