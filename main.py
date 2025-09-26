#Explaining float, string and interger  work in python

# age , grade, name = 30, 30.0, "punk"

# new_grade = int(grade)
# print(type(new_grade))


# new_age = float(age)
# print(type(new_age))


# print(age)
# print(grade)
# print(name)

# num = "40" 
# new_Num = int(num)
# print(type(new_Num))





#Explaining the input function 

# print('hello' + input("what is your UserName "))

# instruction
# write a program that print a number of charater of a user.....


# print("hello" + input('enter password'))
# print(len(input('enter your exam subject')))

# name = input('enter your name')
# length = len(name)
# print(length)


# print(len(input('please enter your Username')))

# password = input("enter your password?\n")
# length = len(password)
# print("the length of ur password is : ",  length)



#instruction

# a = input('A')
# b = input('B')

# print()


# my_number = 50
# my_number += 100

# print(my_number)

# num = 45 % 5
# print(num)

# user_Name = 'punkguy'
# print(user_Name)


#instruction1
#1 Create a greeting for the user 
#2 Ask the user the city they grow up in?
#3 Ask the user for their pet name?
#4 Combine the name of their city and pet and show them their brand name?
#5 Make sure the input curse show on a new line




# print("welcome to your brandName ")
# city = input("what city did you grow up?\n")
# pet = input("what is your pet name?\n")


# print("Your brand name is "+  city + " - " +  pet)



#instruction2

# print("Login to your Facebook account")
# db_password = "punkguy"
# user_password = input('enter your password?\n')


# print( db_password == user_password)

#instruction
#1. Create a greeting for the user  calculator tip
#2. what are the total bill?
#3. How many people will  spit?
#4. what percentage will you like to  give?
#5. Each people should spit answer?


# num_length = len(input('enter your name\n'))

# new_num_length = str(num_length)
# print("your name character is:" + new_num_length + "character" )



# two_digital_num = input("type a two digital num :")

# first_digit = two_digital_num[0]
# second_digit = two_digital_num[1]

# result = int(first_digit) + int(second_digit)
# print(result)

# print(4 * 4 / 5 + 3 - 3 )
# print('welcome to pizza delivery\n')
# size = input('what size of pizza did you want? S,M or L\n')
# add_pepperoli = input('do you want Pepperoni? YES OR NO\n')
# extra_cheese = input('do you want cheese?\n')
# bill = 0 

# if pizza > 2:
#  print("Larger than 2")

# print('welcome to a rollercoaster!')
# age = int(input('please enter your age?\n'))
# bill = 0

# if age >= 120:
#     print('you can ride this')




#pizza challlenge


# size = input('what order size did you want? \n')
# sp = 15
# mp = 20
# lp = 25

# if size == 'small':
#     pep_sm = input("did you want to add so pepperoni ?:")
#     if pep_sm == 'yes':
#         print('your total is cost :', sp + 2 )
#     else:
#         print('your total is cost : ', sp )

# elif size == 'medium ':
#     pep_ml = input("did you want to add so pepperoni ?:")
#     if pep_ml == 'yes':
#         print('your total is cost :', mp + 3 )
#     else:
#         print('your total is cost :', mp )

# elif size == 'large':
#     pep_lp = input("did you want to add so pepperoni ?:")
#     if pep_lp == 'yes':
#         print('your total is cost :', lp + 3 )
#     else:
#         print('your total is cost :', lp )

# else: print('invalid size')        



# Python Challenge
# Your task is to write a Python program that will:

#  Take three inputs: l, h, and L: The length of the telephone box shadow (l),
#  the height of the telephone box (h) and the length of the shadow of the Elizabeth Tower (L)
#  Use the three input values to work out the height of the Elizabeth Tower (H)
#  Output the estimated height of the Elizabeth Tower to one decimal place.


# h = 2.51
# I = 1.74
# L = 66.55

# l = float(input("Enter the length of the telephone box shadow (l):"))
# h = float(input("Enter the height of the telephone box (h): "))
# L = float(input("Enter the length of the shadow of the Elizabeth Tower (L): "))
# H = (h * L) / l
# print('THE ESTIMATED HEIGHT OF THE ELIZABETH TOWER (H) IS:' (H) )

Treasure = input('Welcome to Treasure Island. Your mission is to find the treasure\n')


if Treasure == ' right':
     ways = input('left or right?\n')
     if ways == 'right':
         print('Fall into a hole.Game Over.\n')
     else:
          print('')




elif  Treasure == 'left':
     ways = input('left or right?\n')
     if ways == 'left':
         print('swim or wait\n')
         
elif  Treasure == 'swim':
     ways = input('left or right?\n')
     if ways == 'swim':
         print('Attacked by trout.Game Over\n')


    

  
