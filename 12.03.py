


num1=int(input('Enter a number'))
num2=int(input('Enter a second number'))
if num1==num2:
    print('Both numbers are equal')
    if num1>0:
        print('Both numbers are positive')
    elif num1<0:
            print('Both numbers are negative')
    else:
        print('Both numbers are zero')
elif num1>num2:
    print('num1 is greater')
else:
    print('num2 is greater')




num1=int(input('Enter a number'))
num2=int(input('Enter a second number'))
num3=int(input('Enter a third number'))
if num1>=num2 and num1>=num3:
    print('num1 is greatest')
elif num2>=num1 and num2>=num3:
    print('num2 is greatest')
else:
    print('num3 is greatest')



# # Program to print month name based on number (1-12)

number = int(input("Enter a number (1-12): "))

if number == 1:
    print("January")
elif number == 2:
    print("February")
elif number == 3:
    print("March")
elif number == 4:
    print("April")
elif number == 5:
    print("May")
elif number == 6:
    print("June")
elif number == 7:
    print("July")
elif number == 8:
    print("August")
elif number == 9:
    print("September")
elif number == 10:
    print("October")
elif number == 11:
    print("November")
elif number == 12:
    print("December")
else:
    print("Invalid number! Please enter between 1 and 12.")




num1=int(input('Enter a number: '))
num2=int(input('Enter a number2: '))
x=num1
num1=num2
num2=x
print(num1)
print(num2)


# You are developing a simple ticket booking system for a movie theatre. The ticket
# price depends on the age of the person and whether they have a membership card. If
# the person is under 12, the ticket is free. If the person is between 12 and 60: if they
# have a membership card, the ticket costs Rs. 150. If not, the ticket costs Rs 200. If the
# person is above 60, they get a senior citizen discount, and then ticket costs Rs 100.
# Write a python program using nested if-else to calculate and print the ticket price
# based on the users age and membership status. 

age=int(input('Enter a person age: '))
if age<12:
    print('ticket is free')
elif age>=12 and age<=60:
    membership_card=input('do the person have the membership card')
    if membership_card=='yes':
        price=150
    else:
        price=200
        print(price)
else:
    price=100
    print(price)




# A utility company charges different rates based on electricity usage:
# If usage < 100 units then cost Rs 5 per unit
# If usage is between 100 to 300 units:
# First 100 units: Rs 5
#  Next units: Rs 8
# If usage is > 300 units:
#  First 100: Rs 5
#  Next 200: Rs 8
#  Remaining: Rs 10

Usages=int(input('Enter a unit: '))
if Usages<100:
    cost=Usages*5
    print('the total cost of your electricity usages is', cost )
elif Usages<=300:
    cost= (100*5) + (Usages-100)*8
    print('the total cost of your electricity usages is', cost )
else:
    cost= (100*5) + (200*8) + (Usages-300)*10
    print('the total cost of your electricity usages is', cost )    





#  Write a complete Python program that:
#  Asks Player 1 to enter their move ( input: rock, paper, or scissors)
#  Asks Player 2 to enter their move ( input: rock, paper, or scissors)
#  Uses only nested if and else statements
#  Prints who wins or if it's a tie

# Rock Paper Scissors using nested if-else

p1 = input("Player 1, enter your move (rock, paper, scissors): ")
p2 = input("Player 2, enter your move (rock, paper, scissors): ")
if  p1 == 'rock':
    if p2 == 'rock':
        print("It's a tie!")
    else:
        if p2 == 'paper':
            print('player 2 wins')
        else:
            print('player 1 wins')

else:
    if p1 == 'paper':
        if p2 == 'paper':
            print('its a tie')
        else:
            if p2 == 'scissors':
                print('player 2 wins')
            else:
                print('player 1 wins')

    else:
        if p1 == 'scissors':
            if p2 == 'scissors':
                print('its a tie')
            else:
                if p2 == 'rock':
                    print('player 2 wind')
                else:
                    print('player 1 wins')

        else:
            print('invalid input from player 1')






# In a smart building lift system, the lift is currently at floor 5. A person presses
# floor 3. Write a program to decide and display whether the lift should go up, go
# down, or stay at current floor.

current_floor=5
requested_floor=int(input("Enter the floor number "))
if requested_floor>current_floor:
    print("lift should go up")
elif requested_floor<current_floor:
    print("lift should go down")
else:
    print("lift stay at current floor")








# Write a Python program that takes a number as input, first checks if it is positive
# if yes then check whether it is even or odd.



num=int(input('Enter a number'))
if num>0:
    print('positive')
    if num%2==0:
        print('even')
    else:
        print('odd')
else:
    if num<0:
        print('negative')
    else:
        print('zero')








# Take two numbers and find the greater of the two. If they are equal, check if the
# number is positive, negative, or zero.

num1=int(input("Please enter a number"))
num2=int(input('please enter a second number'))
if num1>num2:
    print('num1 is grater')
elif num1<num2:
    print("num2 is greater")
else:
    print('both numbers are equal')
    if num1>0:
        print('positive')
    elif num1<0:
        print('negative')
    else:
        print('zero')




#   Accept input from user If given number is a multiple of both 3 and 5 prints "Fizz
# Buzz" instead of number If given number is a multiple of 3 but not 5 prints "Fizz"
# instead of number If given number is a multiple of 5 but not 3 prints "Buzz"instead
# of number If given number is not multiple of 3 or 5 prints value as usual.

num=int(input("Enter a number: "))
if num%3==0 and num%5==0:
    print('Fizz Buzz')
elif num%3==0:
    print('fizz')
elif num%5==0:
     print('buzz')
else:
    print(num)