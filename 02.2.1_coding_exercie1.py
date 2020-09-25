#The code below tries to calculate the quotient and remainder
#of a pair of numbers. However, right now None is printing
#in several places throughout the code's execution. Fix the
#code so that it behaves as intended: it should print the
#quotient, remainder, then the message, "We're done!"
#
#HINT: There are a couple ways to do this, and some of those
#ways might be a little advanced right now. Note that 17 // 6
#will correctly calculate the quotient and num_1 % num_2 will
#correctly calculate the remainder.
#
#HINT 2: Click Reset to start over from scratch.

num_1 = 17
num_2 = 6

quotient = print("The quotient is", num_1 // num_2)
print(quotient) # the quotient variable is already being printed, so None here.

remainder = print("The remainder is", num_1 % num_2)
print(remainder) # the remainder variable is already being printed, so None. 

print(print("We're done!"))

# solution:
# get rid of all the 'print' command inside the variables.
# Never assign a variable to a print statment such as line 17 & line 2.
print("#####################")
print("Here is my solution below:")

num_1 = 17
num_2 = 6

quotient = "The quotient is", num_1 // num_2
print(quotient)

remainder = "The remainder is", num_1 % num_2
print(remainder)
print("No more None!")
