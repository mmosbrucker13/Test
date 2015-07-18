#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Melissa
#
# Created:     16/07/2015
# Copyright:   (c) Melissa 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#dateutil
#import datetime

#currentTime = datetime.datetime.now()
#print(datetime.datetime.strftime(currentTime, '%H:%m'))

#Give someone the length of time they have until a deadline
import datetime
deadline = datetime.datetime.strptime(input("When is the deadline for your project? mm/dd/yyyy, hours:minutes"), "%m/%d/%Y, %H:%M")

currentDateandTime = datetime.datetime.now()

print(str(deadline- currentDateandTime))