#1.
#Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

    # 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
    # 2. Change the last_name of the first student from 'Jordan' to 'Bryant'
    # 3. In the sports_directory, change 'Messi' to 'Andres'
    # 4. Change the value 20 in z to 30
#ANSWERS
#1.
x[1][0] = 15 # reassigns the value 10 to 15
print(x[1]) # prints the updated result
#2.
students[0]['last_name'] = 'Bryant'
#3.
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
#4. 
z[0]['y']=30
print(z)

#2.
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for x in range(len(some_list)):
        for key, value in some_list[x].items():
            print(key, value)

iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


#3.
#Get Values From a List of Dictionaries
    # Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
    # Michael
    # John
    # Mark
    # KB


def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
    return some_list

iterateDictionary2('first_name', students)


#4. Iterate Through a Dictionary with List Values
    #Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojos = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
     for key, value in some_dict.items():
        print(len(some_dict[key]))
        print(key)
        for i in range(len(some_dict[key])):
          print(some_dict[key][i])
        # print(*some_dict['locations'])
        # print(len(some_dict['instructors']), instructors )
        # print(*some_dict['instructors'])

printInfo(dojos)
# # output:
# # 7 LOCATIONS
# # San Jose
# # Seattle
# # Dallas
# # Chicago
# # Tulsa
# # DC
# # Burbank
    
# # 8 INSTRUCTORS
# # Michael
# # Amy
# # Eduardo
# # Josh
# # Graham
# # Patrick
# # Minh
# # Devon













