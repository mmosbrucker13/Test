#writing todays date 
#import datetime

#currentDate = datetime.date.today() 
#print(currentDate) 
#print(currentDate.year)
#print(currentDate.month) 
#print(currentDate.day) 

#print(currentDate.strftime('%d, %B, %Y')) 
#strftime.org 

#birthday countdown 
import datetime  
birthday = input('What is your birthday? + " " mm/dd/yyyy?') 
birthdate = datetime.datetime.strptime(birthday,"%m/%d/%Y").date()  
#why did we list datetime twice?
#bc we are calling strptime function which is part of datetime class
#which is in the datetime module
currentDate = datetime.date.today()
print ("It is " + str(birthdate - currentDate) + " until your birthday") 