import math as m

#Zadanie 1
print("--------------Zadanie 1---------------")

print("Liczba Pi =", m.pi)
print("Liczba E =", m.e)
print("Sin(15) =", m.sin(15))
print("10^1/2 =", 10 ** (1/2))
print("2^12 =", 2 ** 12)
print("Log1000 =", m.log10(1000))
print("Log2 1024 =", m.log2(1024))
print("Ln10 =", m.log(10))

#Zadanie 2
print("--------------Zadanie 2---------------")

try:
  a = int((input ("Enter first int number for sum: ")))
  b = int((input ("Enter second int number for sum: ")))
  print("Sum = " + str(a+b))

  c = int((input ("Enter first int number for difference: ")))
  d = int((input ("Enter second int number for difference: ")))
  print("Difference = " + str((c-d)))

  e = int((input ("Enter first int number for product: ")))
  f = int((input ("Enter second int number for product: ")))
  print("Product = " + str(e*f))

  g = int((input ("Enter first int number for quotient: ")))
  h = int((input ("Enter second int number for quotient: ")))
  print("Quotient = " + str(g/h))

except ValueError:
    print ("Please, enter a number!")

#Zadanie 3
print("--------------Zadanie 3---------------")

try:
  a = int((input ("Enter first int number for sum: ")))
  b = int((input ("Enter second int number for sum: ")))
  abComplex = complex(a + b)
  print("Sum = " + str(abComplex))

  c = int((input ("Enter first int number for difference: ")))
  d = int((input ("Enter second int number for difference: ")))
  cdComplex = complex(c - d)
  print("Difference = " + str((cdComplex)))

  e = int((input ("Enter first int number for product: ")))
  f = int((input ("Enter second int number for product: ")))
  efComplex = complex(e * f)
  print("Product = " + str(efComplex))

  g = int((input ("Enter first int number for quotient: ")))
  h = int((input ("Enter second int number for quotient: ")))
  ghComplex = complex(g / h)
  print("Quotient = " + str(ghComplex))

except ValueError:
    print ("Please, enter a number!")

#Zadanie4
print("--------------Zadanie 4---------------")

x1 = float(input("Enter a x1: "))
y1 = float(input("Enter a y1: "))
x2 = float(input("Enter a x2: "))
y2 = float(input("Enter a y2: "))

print(m.sqrt((x2 - x1) * (x2-x1) + (y2 - y1) * (y2 - y1)))

#Zadanie 5
print("--------------Zadanie 5---------------")

celsius = float(input('Enter temperature in celsius: '))

fahrenheit = 1.8 * celsius + 32
kelvin = 273.15 + celsius

print('%0.3f Celsius = %0.3f Kelvin.' % (celsius, kelvin))
print('%0.3f Celsius = %0.3f Fahrenheit.' % (celsius, fahrenheit))