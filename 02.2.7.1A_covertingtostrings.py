myinteger = 11
print(type(myinteger))

# converting integer to string using a string function.
mynintegertostring = str(myinteger)
print(type(mynintegertostring))


from datetime import date
mydate = date.today()
# print("Today's date: " + mydate) # this will yield a type error.
# cannot do an implicit conversion with String + other data type.
# I need 'String' + 'String'.
# use the following explicit conversion to enable the implicit conversion.

mydatetostring = str(mydate)
print("Today's date: " + mydatetostring)

mydatetostring = str(date.today())
print("Today's date: " + mydatetostring)

# python starts with the inner most function.
print("Today's date: " + str(date.today()))

# Or I could simply use the ',' instead of using the '+'.
# this enables to use the 'Strig' and 'date' data type in one print statement.
print("Today's date:", date.today())

aboolean = "True"
conversion = bool("1")
print(type(conversion))
