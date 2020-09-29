#youruserinput = input("Enter an integer: ")
#input_integer = int(youruserinput) # converting the 'String' to an 'Integer'.
#print(input_integer * input_integer)

myint = 2
if myint == 2:
    print(True)

# 2.2.9 Worked Example 1
#Early feedback suggests the exercise immediately following this
#is a bit difficult. You've seen everything you need to know to do
#it, but it hasn't been the focus yet. So, this worked example shows
#the solution to a similar problem to help you figure out 2.2.9 Coding
#Exercise 1.
#
#Imagine you are trying to print a person's height in the imperial
#system. You have two variables: feet and inches. You want to print
#the height in the typical style -- for example, if feet was 5 and
#inches was 4, you'd want to print 5'4. We're leaving off the
#quotation mark at the end to keep things simple.

#How would we do that?

#First, let's create the variables.
feet = 5
inches = 4

#What happens if we just add them together?

print("Just summing up: ")
print(feet + inches)
print() # blank line

#Yikes! That's not what we want. It just added 5 and 4 and got 9. We
#don't want to add them as numbers, we want to add them as text,
#putting them together.

#So, let's convert them to strings first. That will force Python to
#treat them like text instead of like numbers.

feet_str = str(feet)
inches_str = str(inches)
print("adding them as strings: ")
print(feet_str + inches_str)
print()
print("with apostrophe: ")
print(feet_str + "'" + inches_str) # 'int' + 'str' only works as the integers
# are converted to strings.
