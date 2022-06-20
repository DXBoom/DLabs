import math
import datetime

#Zadanie 1
print("--------------Zadanie 1---------------")

x = int(input("Enter a number: "))

if x >= 0 and x <= 10:
    print("Your evaluation its 2!")

elif x >= 11 and x <= 13:
    print("Your evaluation its 3!")

elif x >= 14 and x <= 16:
    print("Your evaluation its 4!")

elif x >= 17 and x <= 20:
    print("Your evaluation its 5!")

else:
    print("Please, enter a number between 0-20")

#Zadanie 2
print("--------------Zadanie 2---------------")

a = int(input('Enter A parameter: '))
b = int(input('Enter B parameter: '))
c = int(input('Enter C parameter: '))

delta = (b*b)-(4*a*c)
print ("Delta is: ", delta)
 
if delta > 0:
    x1 = -b - math.sqrt(delta) / (2*a)
    x2 = -b + math.sqrt(delta) / (2*a)    
     
    print ("There are two roots of the equation = ", x1, x2)    
     
else:
    if delta == 0:
        x = -b / (2 * a)
        print ("There are one root of the equation", x)
         
    else:
        print ("No zero seats!")

#Zadanie 3
print("--------------Zadanie 3---------------")
kwh = float(input("Enter a number: "))

if kwh > 0 and kwh <= 50:
    kwh_print = kwh * 0.5
    print (kwh_print)

elif kwh > 50 and kwh <= 150:
    kwh_stay = kwh - 50
    kwh_print = (50 * 0.5) + (kwh_stay * 0.75) 
    print (kwh_print)

elif kwh > 150 and kwh <= 250:
    kwh_stay = kwh - 150

    kwh_sum = (50 * 0.5) + (100 * 0.75) + (kwh_stay * 1.20)
    print (kwh_sum)

elif kwh > 250:
    kwh_stay = kwh - 250

    kwh_sum = (50 * 0.5) + (100 * 0.75) + (100 * 1.20) + (kwh_stay * 1.50)
    print (kwh_sum)

#Zadanie 4
print("--------------Zadanie 4---------------")

dayEnter = int(input("Enter a day: "))
currentDate = datetime.date.today()
ourDate = datetime.date(currentDate.year, currentDate.month, dayEnter)

dayNumber = ourDate.weekday()

if dayNumber == 0:
    print ("Monday")
elif dayNumber == 1:
    print ("Tuesday")
elif dayNumber == 2:
    print ("Wednesday")
elif dayNumber == 3:
    print ("Thursday")
elif dayNumber == 4:
    print ("Friday")
elif dayNumber == 5:
    print ("Saturday")
elif dayNumber == 6:
    print ("Sunday")

#Zadanie 5
print("--------------Zadanie 5---------------")

letter = input('Enter Your Characters\n')[0]
letterCheck = letter[0].isupper()

if letterCheck:
    letterLower = letter[0].lower()
else:
    letterLower = letter[0]

print(letterLower)








