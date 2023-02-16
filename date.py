#datetime module
import datetime
#get date time now
x= datetime.datetime.now()
print(x)
print(x.year)
#to get the name of the weekday
print(x.strftime("%A") + " " + str(x.month)+ " "+ str(x.year))
print(x.strftime("%p"))
print(x.strftime("%A"))