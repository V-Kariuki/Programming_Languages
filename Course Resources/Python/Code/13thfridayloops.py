number1=0
while number1<5:
    print(number1)
    number1=number1+1

while expression:
    while expression:
        statements
        statements
    
list1 = ["my", "class","and","school"]
for word in list1:
    print (word)

fruits = {'apple':5,'mango': 10,'orange':20}
for fruit in fruits.items():
    print(fruit)

for iterable in sequence:
    for iterable1 in sequence:
        statements
        statements
       
plants = ["apple","mango","pear"]

for plant in plants:
    for letter in plant:
        print (", ",letter,end="")
        
    print(", ",plant," \n, ")    
     

for letter in "goodmorning":
    if letter == "o":
        continue
    print ("current value: ", letter," ", end=",")
    
for letter in "goodmorning":
    if letter == "n":
        break
print ("current value: ", letter)

for letter in "goodmorning":
    pass
print ("current value: ", letter)

#Strings
my_string = "hello"
#index 0 =h, 1 = e, 2 = l, 3 = l, 4 = o
print (my_string)
print (my_string[0])
print (my_string[0:3])
print (my_string[:3])
print (my_string[3:])
print (my_string[0:5:2])
print (len(my_string))
print (my_string.upper())
print (my_string.lower())
print (my_string.find("l"))
print (my_string.replace("l","L"))
print (my_string.replace("l","L").upper())
for index,character in enumerate(my_string):
    print(index,"=", character)

string2=" world"
print (my_string+string2)

#tuples
my_tuple = (10,"hello","world",10,90.5,10)
print (my_tuple)
print (my_tuple.count(10))
print (my_tuple.index(10))
print (len(my_tuple))
print (my_tuple[4])

#Lists
my_list = ["hello","world","good","morning"]
print (my_list)
print (my_list[0])
print (my_list[0:3])
print (my_list[:3])
print (my_list[3:])
print (my_list[0:5:2])
print (len(my_list))
my_list.append("new")
print (my_list)
my_list.insert(0,"new")
print (my_list)
my_list.pop()
print (my_list)
my_list.remove("good")
print (my_list)
my_list.reverse()
print (my_list)
my_list.sort()
print (my_list)
list2 = ["order" , "list"]
my_list.extend(list2)
print (my_list)
my_list.clear()
print (my_list)