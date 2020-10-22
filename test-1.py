# This a Beta type of saying hi and bye. Treat with care!

# What does this do?
# - Takes Age and adds it
# - Says glad your day is__ 
# - says that its good to meet you __



#Simple Time Import
import time

# First Message
print('Hello world! How is it going')
myDay = input() #Response
print('Glad you are doing, ' + myDay) #Glad you are doing __

# Another 5 Seccond wait
time.sleep(3)



# Seccond Message
print('What is your name?') # ask for their name
myName = input() #Response
print('It is good to meet you, ' + myName)



# Fourth Message
print('What is your age?') # ask for their age
myAge = input() #Response

print('You will be ' + str(int(myAge) + 1) + ' in a year.')
print('I will be 2 years old in 2 years.')



# Made by Noah | Tutorial online
