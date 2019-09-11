print ("Hello world")

#Concatentaing strings and variables with the print function.
    # multiple ways to print a string containing data from variables.
name = "zen"
print("My name is,", name)

name = "zen"
print("My name is " + name)

#F-strings (Literal String Interpolation)
first_name = "zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.") #this is the new way to do it :)

first_name = "Chuy"
last_name = "Medina"
age = 23
food = "sushi"

print(f"Hello, my first name is {first_name} and my last name is {last_name}, and also my current age is {age}. I also really enjoy {food}, but I ain't trying to get Mercury poisoning though")

# String.format() method.
first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age)) #putting in variables in the order in which they should fill the brackets.

# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

name = "Jesus Medina"
food = "pizza and sushi"

print("Hello, I really like {} and my name is {}".format(food, name))


# This is an even older way of string interpolation.
    # Rather than curly braces, the % symbol is used to indicate a placeholder, a %s for a string and %d for a number. After the string, a single % separates the string to be interpolated from the values to be inserted into the string, like so:
hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27


# Built-In String Methods
    # We've seen the format method, but there are several more methods that we can run on a string. Here's how to use them:

x = "hello world"
print(x.title()) # this is so weird
# output:
"Hello World"










