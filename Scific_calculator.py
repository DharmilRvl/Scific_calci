import math


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def div(a, b):
    return a / b

def sqrt(a):
    result = math.sqrt(a)
    return result

def exp(a):
    return a ** 2

def sin(x):
    result = math.sin(x)
    return result

def cos(x):
    result = math.cos(x)
    return result

def tan(x):
    result = math.tan(x)
    return result

#choosing th operation
print( """
Choose a number for following operations
1 - addition(x,y)
2 - subtraction(x,y)
3 - multiplication(x,y)
4 - division(x,y)
5 - square(x)
6 - square root(x)
7 - sin(x)
8 - cos(x)
9 - tan(x) """)
op = int(input("what operation you want to perform:"))

while op < 10:
    if op ==1:
        print("enter parameters")
        x1 = int(input("enter x : "))
        y1 = int(input("enter y : "))
        res1 = add(x1,y1)
        print("addition=", res1)
    elif op ==2:
        print("enter parameters")
        x2 = int(input("enter x : "))
        y2 = int(input("enter y : "))
        res2 = subtract(x2,y2)
        print("subtraction=", res2)
    elif op ==3:
        print("enter parameters")
        x3 = int(input("enter x : "))
        y3 = int(input("enter y : "))
        res3 = multiply(x3,y3)
        print("multiplication=", res3)
    elif op ==4:
        print("enter parameters")
        x4 = int(input("enter x"))
        y4 = int(input("enter y"))
        res4 = div(x4,y4)
        print("division=", res4)
    elif op ==5:
        x5 = int(input("enter x"))
        res5 = exp(x5)
        print("square=", res5)
    elif op ==6:
         x6 = int(input("enter x"))
         res6 = sqrt(x6)
         print("squareroot=", res6)
    elif op ==7:
         x7 = int(input("enter x"))
         res7 = sin(x7)
         print("sin(x)=", res7)
    elif op ==8:
         x8 = int(input("enter x"))
         res8 = cos(x8)
         print("cos(x)=", res8)
    elif op ==9:
         x9 = int(input("etner x"))
         res9 = tan(x9)
         print("tan(X)=", res9)

    else:
        print("choose another operation")

    new = int(input("do you want to continue - (yes -1) (no -0):"))
    if new == 1:
        op = int(input("enter new operation:"))
    elif new == 0:
        print("thanks for using the scientific calculator")
        break
        
        
                
        

    


    
