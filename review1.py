
def main():
    # problem1()
    # exercise2()
    # challenge1()
    challenge2()


# Create a function that has a loop that quits with q.
# If the user doesn't enter q, ask them to input another string.
# BONUS: Make sure the code can handle whatever case the User enters the q as (uppercase or lowercase).

# should i continue to use infinite loops or use defined begin end while loops?
# re read the problem to make sure i have it right
# spelling is important to!!

def problem1():
    userinput = input("gimme some knowledge")

    while(True):
        if(userinput.lower() == "q"):
            print("my one weakness!?!")
            break
        else:
            userinput = input("gimme something else to feed on")

# Write 2 functions: exercise2() and exercise2_helper(num1, num2, num3. operation)
#
# The function exercise2_helper(num1, num2, num3) should expect 3 numbers,
# and an operation to perform as a String as parameters.
# The function should support 3 operations:

# SUM - Return the sum of the 3 numbers
# PROD - Return the product of the 3 numbers
# AVG - Return the average of the 3 numbers

# The operation and the returned value should then be printed out back in the main exercise2() function.
# Return INVALID OPERATION if an operation passed in that isn't supported. HINT: Use switch/case

# calling one function inside another is ok.
# as long as the function you call is within scope of the calling function
# math is important, also python doesn't have a switch case function so use elif for most scenarios since it does the same thing.
# re read the question and check your spelling!!

def exercise2():
    # KEY: Nice touch having the user enter the numbers
    numberone = int(input("give me your first number"))
    numbertwo = int(input("I need another number please."))
    numberthree = int(input("And your final number please"))
    oper = input("what do you want to do with it? sum/prod/avg")
    exercise2_helper(numberone,numbertwo,numberthree,oper)


def exercise2_helper(num1,num2,num3,operation):
    if(operation.lower() == "sum"):
        print(f"{num1+num2+num3} is the sum.")
    elif(operation.lower() == "prod"):
        print(f"{(num1*num2)*num3} is the product.")
    elif(operation.lower() == "avg"):
        print(f"{(num1+num2+num3)//3} is the average.")
    else:
        print("invalid operation.")

# Write a function that prompts the User for the number of stars to print.
# Then use a loop to print a number of stars/asterisks starting with 1 and up to the number entered by the User.
#
# If rows is 5, it should print the following:
#
# *
# **
# ***
# ****
# *****

# use a loop and use input to set the end.
# if you want to build a "pyramid" need a second variable counting backwards and grow faster then your starting range.
#  reduceingvariable-=2 can be used

def challenge1():
    starnumber = int(input("how many starts do you want me to go to?"))
    for x in range(1,starnumber+1):
        print("*"*x)


# Write a function for checking the speed of drivers.
# Prompt the User to enter the speed that a driver was observed driving at.
#
# If speed is less than 70, it should print Ok.
#
# Otherwise, for every 5mph above the speed limit (70),
# it should give the driver one demerit point and print the total number of demerit points.
#
# For example, if the speed is 80, it should print: Points: 2.
#
# If the driver gets more than 12 points,
# the function should print: License Suspended

# order of operation matters.
# loop can be used for rerunning through the number.
# for loop can be used for range?
# while loop can also be used.

# for x in range(70,userspeed+1,5):
# userpoints+=1

# use without a loop
# if userspeed >70
# userpoints = (userspeed-70//5)
# print(f"{userspeed} gets you {userpoints}
# print (" %d gets you %d" % userspeed , userpoints")

def challenge2():
    userspeed = int(input("how fast were you going?"))
    speedcal = userspeed
    userpoints = 0
    while(True):
        if(speedcal > 74):
            speedcal -=5
            userpoints+=1
        elif(userpoints >= 12):
            print("License suspended")
            break
        elif(userspeed <= 70):
            print("you're ok to go.")
            break
        else:
            print(f"{userspeed} gets you {userpoints} ")
            break





if __name__ == '__main__':
    main()
