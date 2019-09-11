# Write the code to print a literal string saying "Hello World" (#1)
message = "Hello, World"
print(f"{message}")

# Store your name in a variable, and then use it to print the string “Hello {{your name}}!” using a comma in the print function (#2a)
first_name = "Chuy"
last_name = "Medina"
print("Hello, ", first_name, last_name)

# Store your name in a variable, and then use it to print the string “Hello {{your name}}!” using a + in the print function (#2b)
print("Hello, " + first_name + " " + last_name)

#Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a comma in the print function (#3a)
fave_num = 13
print("Hello,",fave_num)

# Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a + in the print function (#3b)
fave_num = "13" # changed num or int to a string of a number. So the I basically turned the number into a string, which sort of gets to job done
print("Hello" + " " + fave_num)

#Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” with the format method (#4a)
fav_food1="sushi"
fav_food2="thai"
print("I love to eat {} and {}".format(fav_food1, fav_food2))

#Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” with f-strings (#4b)
print(f"I love to eat {fav_food1} and {fav_food2}")








