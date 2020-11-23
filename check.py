def check_user_input(n):
    if n >= 0:
        print("You entered positive Number")
    else:
        print("You entered negative number")

input=int(input("enter the number"))
check_user_input(input)