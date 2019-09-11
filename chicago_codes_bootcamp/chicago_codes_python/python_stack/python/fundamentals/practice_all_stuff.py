# Conditionals
    # Conditional statements allow us to run certain lines of code depending on whether certain conditions are met. In Python, the keywords for conditional statements are if, elif, and else. Here are some examples:
x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
# because x is not greater than 50, the second print statement is the only one that will execute

x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")
# even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

if x < 10:
    print("smaller than 10")
# nothing happens, because the statement is false   


# LOOPS!!!!

#The range function actually comes with a few shortcuts. If we know the increment is going to be plus one, we can actually just ignore the third argument. Furthermore, if we know the increment is going to be positive one and the loop starts at 0, we can also leave off the first argument. In other words, each of the following will result in exactly the same loop:
for x in range(0, 10, 1):
for x in range(0, 10):	# increment of +1 is implied
for x in range(10):	# increment of +1 and start at 0 is implied

# Note that if you need to specify an increment other than +1, all three arguments are required.
for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2



#For Loops through Lists

#If we want to iterate through a list, we could use the range function and send in the length of the list as the stopping value, but if we are not interested in the index values and want to just see the values of each item in the list in order, we can actually loop to get the values of the list directly!

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

#For Loops through Dictionaries

#Dictionaries are also iterable. When we iterate through a dictionary, the iterator is each of the keys of the dictionary.
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

# Dictionaries also have a few additional methods that allow us to iterate through them and have the keys and/or values as the iterator. Test these out to get a better understanding:

# another way to iterate through the keys
for key in capitals.keys():
     print(key)
#to iterate through the values
for val in capitals.values():
     print(val)
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)


#WHILE LOOPS!!

for count in range(0,5,2):
    print("looping - ", count)

#We can rewrite it as a while loop:
count = 0
while count < 5:
    print("looping - ", count)
    count += 1

#The basic syntax for a while loop looks like this:
while <expression>:
    # do something, including progress towards making the expression False. Otherwise we'll never get out of here!


#Else

#There are certain conditions that we give for every loop that we have, but what if the condition was not met and we still would like to do something if that happens? We can then use an else statement with our while loop. Yes, that is right, else in a loop.
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")






