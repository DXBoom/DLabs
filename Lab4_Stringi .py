#Zadanie 1
print("--------------Zadanie 1---------------")

str1 = "Allo!"
str2 = "Herr Gruber!"

print ("Lenght str1:", len(str1))
print ("Lenght str2:", len(str2))
print ("Concatenate str1 and str2:", str1 + str2)
str3 = 2 * (str1 + str2)
print ("Str3:", str3)

#Zadanie 2
print("--------------Zadanie 2---------------")
strCat = "Ala ma kota Felka"

print(strCat.replace("a", "*"))

for letter in strCat:
    if letter.isupper():
        strCat = strCat.replace(letter, letter.lower())
print(strCat)

for letter in strCat:
    if letter.islower():
        strCat = strCat.replace(letter, letter.upper())
print(strCat)

#Zadanie 3
print("--------------Zadanie 3---------------")

strCustom = "Change and open your mind!"

for i in range(len(strCustom)):
    if strCustom[i] != " ":
        print(strCustom[i])

for j in strCustom:
    if j != " ":
        print(j)

#Zadanie 4
print("--------------Zadanie 4---------------")

strEmpty = ""

for i in range(ord('a'), ord('z') + 1):
    strEmpty += chr(i)

print("Created str:", strEmpty)
print("Created str from 2 to 7:", strEmpty[2:7])
print("Created str from 0 to 10:", strEmpty[0:10])
print("Created str after 15:", strEmpty[15:len(strEmpty)])

#Zadanie 5
print("--------------Zadanie 5---------------")

stringLast = "Organizatorom marszu plany pokrzyżowała pogoda, która pogorszyła się w ciągu kwadransa"

print("String Last:", stringLast)

if 'pogoda' in stringLast:
    print("We have *pogoda* word!")

sep = 'pogoda, '
stripped = stringLast.split(sep, 1)[1]
print("Replaced last string:", stripped.upper())

