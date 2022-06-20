import math as m
from math import sin, radians
from time import sleep

#Zadanie 1
print("--------------Zadanie 1---------------")

n = int(input("Enter n number: "))

nCached = n

i = 1
while i <= n:
    print("Show number from 1 to n: ", i)
    i += 1

while n != 0:
    print("Show number from n to 1: ", n)
    n = n - 1

for oddNumbers in range (1, nCached + 1):
    if oddNumbers % 2 != 0:
        print ("Odd numbers: " , oddNumbers)

for evenNumbers in range (1, nCached + 1):
    if evenNumbers % 2 == 0:
        if evenNumbers % 3 == 2:
            if evenNumbers != 2:
                print ("Even numbers with 2: " , evenNumbers)

for oddNumbers in range (1, nCached + 1):
    if oddNumbers % 2 != 0:
        print ("Odd numbers: " , oddNumbers)

for oddNumbers in range (1, nCached):
    if oddNumbers % 5 == 0:
        print ("Multiples numbers 5: " , oddNumbers)

getList = [chr(i) for i in range(ord('a'),ord('z') + 1)]
print(getList)

#Zadanie 2
print("--------------Zadanie 2---------------")

def divisors():
    divisorNumber = int(input("Enter a number: "))
    while True:
        result = set()
        for i in range(1, int(divisorNumber**0.5)+1):
            if divisorNumber % i == 0:
                result.add(i)
                result.add(divisorNumber//i)

        if len(result) > 2:
            print("None first number!")
            print (list(result))

        elif len(result) <= 2:
            print("First number!")
            print (list(result))

        startProgram = int(input("Start program one more time? Enter 0 - Yes/ 1 - No: "))

        if startProgram == 0:
            divisors()
            break
        elif startProgram == 1:
            break

divisors()

#Zadanie 3
print("--------------Zadanie 3---------------")

i = 0
while (i := i + 1) <= 10:
    j = 0
    while (j := j + 1) <= 10:
        print(i * j, end="\t")
    print()

#Zadanie 4
print("--------------Zadanie 4---------------")

startProgramTriangle = int(input("Start default program or enter degree? Enter 0 - Automatic degree/ 1 - Custom degree: "))

def trianFuncDefault():
    i = 0

    while i <= 90:
        print("Sin", i, "-", m.sin(i), end="\t")
        print("Cos", i, "-", m.cos(i), end="\t")
        print("Tn", i, "-", m.tan(i), end="\t")

        if i != 0:
            print("Ctg", i, "-", 1 / m.tan(i), end="\t")

        i = i + 15

def trianFuncCustom():
    i = 0
    getDegreeCustom = int(input("Enter the degree iteration (only if < 90): "))

    while i <= 90:
        print("Sin", i, "-", m.sin(i), end="\t")
        print("Cos", i, "-", m.cos(i), end="\t")
        print("Tn", i, "-", m.tan(i), end="\t")

        if i != 0:
            print("Ctg", i, "-", 1 / m.tan(i), end="\t")

        i = i + getDegreeCustom

if startProgramTriangle == 0:
    trianFuncDefault()

elif startProgramTriangle == 1:
    trianFuncCustom()

#Zadanie 5
print("--------------Zadanie 5---------------")

def wave():
	for a in range(-180, 181):
		s = round( float( "{:.02f}".format( sin( radians(a) ) * 100 ) ) ) // 2
		print(f"{a} degrees:", end="\t")
		print( (s + 50) * " ", end="*\n" )
		sleep(0.01)

wave()
