import addition,subtraction,multiplication,division
while True:
    print("Hello!!!, Welcome To Calculator " )
    a=float(input("Enter the first number: "))
    operation=input("enter the operation: + or - or * or / ")
    b=float(input("Enter the second number: "))
    if operation=="+":
       result=addition.add(a,b)
       print(f"the result of addition {a} and {b} is {result}")
    elif operation=="-":
       result=subtraction.subtraction(a,b)
       print(f"the result of subtraction {a} and {b} is {result}")
    elif operation=="*":
       result=multiplication.multiplication(a,b)
       print(f"the result of multiplication of {a} and {b} is {result}")
    elif operation=="/":
        if b==0:
            print("not defined")
        else:
            result=division.division(a,b)
            print(f"the result of division of {a} and {b} is {result}")
    print("THANK YOU FOR VISITING")
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
        break
