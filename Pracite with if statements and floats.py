#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Melissa
#
# Created:     17/07/2015
# Copyright:   (c) Melissa 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Practice with if and float
#freeToaster = False
#deposit = float(input("How much would you like to deposite today? \n If more than $150 you will get a free toaster."))
#if deposit >= 150:
#    print("You just won a free toaster!")
#    freeToaster = True
#else:
#    print("Thank you for your deposite you win a free t-shirt.")

#print("Have a nice day!")
shippingFee = 10
shippingOrder = int(input("What is your total order amount in dollars?"))
if shippingOrder <= 50:
   order = (shippingOrder + shippingFee)
   print(order)
else:
 print("Thank you for shopping with us!")