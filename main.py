while True:
    print("n====calculator====")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")

    choice=input("choose an operation:")
    
    if choice=="5":
        print("goodby")
        break
    
    num1=float(input("enter first number:"))
    num2=float(input("enter second number:"))

    if choice=="1":
        result=num1+num2
        print("Result",result)

    elif choice=="2":
        result=num1-num2
        print("Result:",result)
    
    elif choice=="3":
        result=num1*num2
        print("Result:",result)
    
    elif choice=="4":
        if num2==0:
            print("Error:Cannot divide by zero.")
    else:
        result=num1/num2
        print("Result:",result)
    
else:
    print("Invalid choice.")