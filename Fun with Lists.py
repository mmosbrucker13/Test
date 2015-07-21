#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Melissa
#
# Created:     20/07/2015
# Copyright:   (c) Melissa 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Lists
guests = ['Melissa', 'Beth', 'Kaylie', 'John','Stephanie']
#term index referes to the position in list
activity = ['Swimming','Upolstering','Soccer','Running']
print(guests[1])
print(guests[-2])
print(guests[0]+' '+activity[0])
#print list, one after another
nbrInList = len(guests)
for steps in range (nbrInList):
    print (guests[steps])
    guests.sort()
