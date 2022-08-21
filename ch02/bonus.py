"""The purpose is to use this program to understand the min()
and max() functions. Written by Lindsey Sullivan"""

print('Fist the min() function. This function is used to find the minimum of a data set.','\n',
'We\'ll make the data set by first having you enter your numbers')

x=int(input('Please enter your first number:'))
y=int(input('Please enter your second number:'))
z=int(input('Finally enter a third number:'))

values = x,y,z

print('The numbers you\'ve chosen are the following:',values)
print('Python uses the min() function, we\'ll now take the numbers you provided and',
'find the mimimum.')

minimum=min(values)

print('The minimum is:',minimum)

print('Let\'s focus on finding the maximum now. You may choose to keep your current data set, or begin a new one')

#Reasearched how to make a questionaire in python using if else statements and else if. Then learned that the def
#statement in python starts the body of a function and can be called on if the user doesn't give the correct inital
#input for choice. I also wanted to make it so the entry wasn't case sensative either by adding the lower() function

def question1():
    choice=str(input('Would you like to keep your current values? [y/n]').lower())
    if choice == 'y':
        print ('Perfect! I\'ll keep the current values! Let\'s find the maximum.')     
        maximum=max(values)
        print ('The maximum is:',maximum)
    elif choice == 'n':
        print('You\'ve decided to change your number set, please follow the next prompts.') 
        x = int(input('Please enter your new first number:'))
        y = int(input('Please enter your new second number:'))
        z = int(input('Please enter your new third number:'))
        print('The numbers you\'ve chosen are the following',x,y,z)
        print('Now we will find the maximum of thse new numbers')
        maximum=max(x,y,z)
        print('The maximum is:',maximum)
    else: 
        print('Please only type y or n, please try again.')
question1()

#Improvements for the future - find a way to loop back through the question process if the user selects something outside of Y or N. 