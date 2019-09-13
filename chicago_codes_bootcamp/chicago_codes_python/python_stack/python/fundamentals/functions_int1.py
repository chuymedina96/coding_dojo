import random
from colorama import Fore, Back, Style 

def randInt(min=0, max=100):
    if min > max:
        return print(Fore.RED + "Min must be less than max")
    num = round(random.random() * (max-min) +min)
    return num

print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100 
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500







#def beCheerful(name="" , repeat=5):
 #   print(f"hello {name}" * repeat)

#beCheerful()
#print(beCheerful("Michael"))
#beCheerful(repeat=10, name="john")










