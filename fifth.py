def add(a,b):
    print("Addition of two numbers is:", a+b)

def sub(a,b):
    c=a-b
    print("Subtraction of two numbers is:",c)

def div(a,b):
    print("Division of two numbers is:", a/b)

def mult(a,b):
    print("Multiplication of two number is:", a*b)


num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
add(num1,num2)
sub(num1,num2)
div(num1,num2)
mult(num1,num2)


def covid(name,temp=98):
    print("Name is:",name , " and body temperature is:", temp,"degree")

covid("dhoni")

