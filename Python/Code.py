        #./configure
        #./configure --enable=optimizations
        #./configure --prefix=/opt
        #make
        #make altinstall
        #python3 --version
        #pip3 --version
#=================
#print("Ao chale haweli pe")

        #=> String always should write in double quotation marks.
        #Indentation are use in python language (without any use do not use any space it will cause of error).

#if 3 > 2:
#    print("3 is getter than 2")

'''
We are just checking the multiple comment line.
Author: Vivek
Date: 24-Aug-2024
'''
'''
a=4
b=5
result=a+b
print(f"The addtion of 4 and 5 is: {result}")
'''

        #Special Characters
            #Always write under a quotes. ("" or '').

#print("Hello Man. \nI'm Vivek Gupta")
    #It'll craete a new line.

#print("Hello Man \bI'm Vivek Gupta")
    #It'll throw character back. (\b\b\b)

#print('It\'s a Vivek\'s books')
    #It'll escape the special character. (windows paths use \\)

#print("Hello Man. \tI'm Vivek Gupta")
    #It'll use tab between the words.

    #To inform the python version or script type. (Which interpereter are us using "Shebank(g) line")
        #!/usr/local/bin/python3

        #Variables  (x=2, Variable is nothing but a reserved memory location to store value. In the other words a vriable in a program given data to the computer to work on)
            #declare and use (No need to declare variable before using then)
            #Don't write quotes around the variable name.
            #Display variables
                #a=4
                #print(a) = 4
                #print('a') = a
                #print((type)a)
#python will work line by line.
            #Re-declare variable
                #If you re-declare the same variable after some code it will assume new one variable.
            #Delete variable
                #del x  (delete the varibale)
            #Rules of define variable
                #It contains letters, numbers and unserscore.
                #It should not keywords and pre-define.
                #It contain space in varibale instead use undersocre.
                #It should not start with a number.
                #It's a case sensitive (x=4 and X=5) both will have defferent value.

#Data type
    #x=4
    #print(id(x)) = It will give the memory location of variable.
    #id=id(x)
    #Every value in python has a data type.
    #Since everything in an object in python programming, data type are actually classes and variable are instance (objects) of these classes.
'''
x=4;y=7.5;z=5+4j
print(x,y,z)    
print(x,type(x))
print(y,type(y))
print(z,type(z))
'''
    
    #Basic data type
        #Numbers
            #int
                #x=4
            #float
                #x=4.5
            #complex
                #x=4+5j
        #string
            #x="Vivek"
            #String always define in single or double duotations
            #If x=Vivek. then it'll try to find the declare variable for Vivek, it'll not feel as a string.
        #Boolean
            #Boolean if True or False, It should me form of True and False without quotations otherwise it'll feel like string.
            #x=True or y=False
    #type(variable_name) will give the type of data stored in variable.

    #Typecasting or Type Conversion.
        #Converting on Data type to another
        #Any data type can be converted into boolean.
            #bool(any_data_type)=Ture or False.
            #bool(non-empty)=True.
        #Any data type can be converted into to a string but reverse is not always true.

        #Integer and Float
            #Integer to Float
'''
a=4
x=float(a)
print(x,type(x))
'''
   
            #Float to Integer
'''
a=4.5
x=int(a)
print(x,type(x))
'''

    #Any data can convert to the string.
'''
a=4
b=4.5
c="Vivek"
d=True
w=str(a)
x=str(b)
z=str(d)
print(w,type(w))    #print(str(a))
print(x,type(x))    #print(str(b))
print(z,type(z))    #print(str(d))
'''
    #Boolean to Integer
'''
a=True
b=False
x=int(a)
y=int(b)
print(x,type(x))    #print(int(a))
print(y,type(y))    #print(int(b))
'''

    #Boolean to String
'''
a=True
z=str(a)
print(z,type(z))    #print(str(a))
'''

'''
???
int_var = int(str_var)
float_var = float(str_var)
list_var = str_var.split()
str_var = ' '.join(list_var)
bool_var = bool(str_var)  # Non-empty string is True, empty string is False
tuple_var = tuple(list_var)
list_var = list(tuple_var)
hash_value = hash("Vivek")
name_to_int = {"Vivek": 1, "Alice": 2, "Bob": 3}
int_value = name_to_int.get("Vivek")  # 1
'''

    #Multiple Variables print

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"First value {num1} + Second value {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"First value {num1} - Second value {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"First value {num1} * Second value {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"First value {num1} / Second value {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()







'''
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)     #global have high priority.

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

print('Hello', 'World')     #Hello World

x = 5
y = "John"
print(x, y)     #5 John

x = 5
y = "John"
print(x + y)    #error because string + number

x = 5
y = 10
print(x + y)    #15

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)    #Python is awesome

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x=4
y=4.5
z="Vivek Gupta"
print(x,y,z)
print("{} {} {}".format(x,y,z))
print("{} \n{} \n{}".format(x,y,z))
print("{} {} {}".format(z,y,x))
print(f"The number value is: {x} \nThe float value is: {y} \nThe String value is: {z}")     #Moslty use the mathod.
final_result=f"The number value is: {x} \nThe float value is: {y} \nThe String value is: {z}"
print(final_result)
'''

    #Input, Output and usage of eval function
'''
a=4
b=8
result=a+b
print(f"Addition of a and b value is: {result}")
'''
'''
print("Provide your first and value for addtion")
#a=input("Enter your first value: ")     It'll take as a string value.
#b=input("Enter your second value: ")    It'll take as a string value.
    #There are two method to print your assign value as a same
#a=int(input("Enter your first value: "))   
#b=int(input("Enter your second value: ))   
a=eval(input("Enter your first value: "))   #It'll consider as what value your given as it is. string provide in quotations.
b=eval(input("Enter your seconf value "))   #It'll consider as what value your given as it is. string provide in quotations.
result=a+b
print(f"Addition of first value {a} and second value {b} is {result}")
'''

    #Basic Opertions
    #String is sequence of characters.
    #In python, string is a sequence of unicode character. Unicode was interduced to include every character in all languages and uniformity in encoding.
    #Sting can define three format "" or '' or """ or """ difference is that in """ """ It'll print as it is.
        #"""
        # My name is
        # Vivek Gupta
        # """ 
    #space is also a charater in python.
