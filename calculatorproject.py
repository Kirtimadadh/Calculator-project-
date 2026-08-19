while True:
    print("addition")
    print("press 2 for subtraction")
    print("press 3 for multiplication")
    print("press 4 for division")
    print("press 5 for exit")
    choice=int(input("Enter your choice:"))
    if choice==5:
        print("exit")
        break
    if choice in [1,2,3,4]:
        num1=int(input("enter number1:"))
        num2=int(input("enter number2:"))
    if choice==1:
        print("the sum is:",num1+num2)
    elif choice==2:
        print("The diff is:",num1-num2) 
    elif choice==3:
        print("The mul is:",num1*num2)
    elif choice==4:
        print("The division is:",num1/num2) 
    else:
        print("exit")
    
    y=input("Do you want to use calculator again? (y/n)")
    if y!="y":
        print("exit")
        break    
        
           