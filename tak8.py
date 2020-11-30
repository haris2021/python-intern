#exceptional handling
try:
    d1 = {'a': '1', 'b': '2'}
    d1['c']
except KeyError:
    print("Key not found")

try:
    print(d)
except NameError:
    print("name not found")

try:
    print(10/0)
except ZeroDivisionError:
    print("Division by zero")

try:
    import mod1
except ModuleNotFoundError:
    print("No module named 'module1'")

try:
    h=int(input("enter a value:"))
    print(h)
except ValueError:
    print("please enter numerical value")

try:
    a, b = 1, 2
    print(ab)
except:
    print("syntax error")


#name error
def callme():
    print("hello")
try:
    calme()
except NameError:
    print("no such function exist")
except:
    print("some other error")

#getting input from user
try :
    age=int(input("enter age::" ))
    print("age is:",age)
except:
    print("please enter a number")

#calculator
try:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

    num1 = int(input("Enter first number:"))
    num2 = int(input("enter the second number:"))
    ch = int(input("Please enter yur choice:"))

    if ch == 1:
        print("answer is:", num1 + num2)
    elif ch == 2:
        print("answer is:", num1 - num2)
    elif ch == 3:
        print("answer is:", num1 * num2)
    elif ch == 4:
         if num2 == 0 :
             print("Divison by zero cannot be done")
         else:
              print("answer is:", num1 / num2)


    else:
        print("Invalid choice")

except ValueError:
    print(" Please Enter valid inputs")



