import datetime

currentDate = datetime.date.today()
print(currentDate)
print(currentDate.day)
print(currentDate.year)
print(currentDate.strftime("%a"))
print(currentDate.strftime("%A"))
print(currentDate.strftime("%Y"))
print(currentDate.strftime("%Ym"))
print(currentDate.strftime("%B %d %Y"))

currentDateTime = datetime.datetime.now()
print(currentDateTime)