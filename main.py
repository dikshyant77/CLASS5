#create a variable number 
num = 1
if num >0:
    print("this is a positive number")

num1 = -2
if num1 >0:
    print("positive number")
    
#create a variable 
num2 = -2
if num2 >0:
    print("this is a positive number")
else:
    print("this is a negative number")

#ask the user to enter a number
num = int(input("enter the number "))
if num <15:
    print(num,"Is less than 15")
else:
    print(num,"Is greater than 15")

#ask the user to enter a number and check whether it's a positive number
num = int(input("enter a number "))
if num <0:
    print(num,"is a negative number ")
else:
    print(num,"is a positive bumber ")