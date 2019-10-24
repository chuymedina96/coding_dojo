# # # DEFINING THE SIMPLEST POSSIBLE CLASS

# # class User:
# #     def __init__(self, first, last, age):
# #         self.first = first
# #         self.last = last
# #         self.age = 23
# #         self.name = first + " " + last



# # user1 = User("Jo", "Medina", 23)
# # user2 = User("Blanca", "Medina", 23)

# # print(user1.first, user1.age)
# # print(user2.name, user2.age)

# # # l = list())


# # # class Vehicle:
# # #     def __init__(self, make, model, year):
# # #         self.make = make
# # #         self.model = model
# # #         self.year = year

# # # CLASS
# #     # CLASSES IN PYTHON CAN HAVE A SPECIAL __INIT__ METHOD, WHICH GETS CALLED EVERY TIME YOU CREATE AN INSTANCE OF THE CLASS(INSTANTIATE)
# #         # INSTANTIAINIG A CLASS
# #             # CREATING AN OBJECT THAT IS AN INSTANCE OF A CLASS IS CALLED INSTANTIATING A CLASS
# #             # V Vehicle("Honda", "Civic", 2017)
# #             # IN THIS CASE, V BECOMES A HONDA CIVIC, A NEW INSTANCE OF VEHICLE
# #         # SELF
# #             #THE SELF KEYWORD REFERS TO THE CURRENT CLASS INSTANCE.
# #             # SELF MUST ALWAYS BE THE FIRST PARAMETER TO __INIT__ AND ANY METHODS AND PROPERTIES ON CLASS INSTANCES
        


# # class Comment:
# #     def __init__(self, username, text, likes=0):
# #         self.username = username
# #         self.text = text
# #         self.likes = likes
# # user1 = Comment("bluethecat", "omg so cute!",0)
# # print(user1.text)




# # # DUNDER METHODS, NAME MANGLING, AND MORE!

# # #name
# # #__name
# # #__name__

# # class Person:
# #     def __init__(self):
# #         self.name = "Tony"
# #         self._secret = "hi!" # just a naming convention
# #         self.__msg = "I like turtles"
# #         self.__lol = 'HAHAHAHA'
        

# # p = Person()
# # print(p.name)
# # print(p._secret)
# # # print(p.__msg)
# # # print(p._Person._secret)
# # # print(p._Person.lol)




# # ADDING INSTANCE METHODS


class User:
    active_users = 0

    @classmethod #first class method :)
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"
    #@classmethod
    # def from_string(cls, data_str):
        
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users +=1
    def logOut(self): 
        User.active_users -=1
        return f"{self.first} has logged out"

    def fullName(self): # always need to includees self, doesnt need to be self can be any name, but most use self
        return f"{self.first} {self.last}"
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"
    def likes(self, thing):
        self.thing = thing
        return f"{self.first} likes {self.thing}"
    def is_Senior(self):
        return self.age >= 65 # this right here is a boolean expression. Similar to: if(this.true){} is js :)
    def birthday(self):
        self.age +=1
        return f"Happy {self.age}th, {self.first}"
    def sayHello(self):
        print("Hello!!")





# print(User.active_users)
# print(user2.logOut())
# print(User.active_users)
user1 = User("Joe", "Smith", 17)
user2 = User("Blanca", "Lopez", 41)

print(User.display_active_users())
user3 = User("Chuy", "Medina", 24)
user4 = User("Lali", "Avila", 24)
print(User.display_active_users()) # this is not an instance of user, but a method of user, hence a class method
user3 = User("Yo", "Test", 24)
user4 = User("Test", "Yo", 24)
print(user2.logOut())
print(User.display_active_users())

# print(user2.fullName())
# print(user1.likes("Ice Cream"))
# print(user2.likes("chips"))
# print(user2.initials())
# print(user1.initials())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)
# print(user2.is_Senior())
# print(user1.sayHello())


# # CLASS ATTRIBUTES
#     # WE CA ALSO DEFINE ATTRIBUTES DIRECTLY ON A CLASS THAT ARE SHARED BY ALL INSTANCES OF A CLASS AND THE CLASS ITSELF


# class Pet:
#     allowed = ['cat','dog','fish','rat']
#     def __init__(self, name,species):
#         if species not in Pet.allowed:
#             raise ValueError(f"You can't have a {species} pet")
#         self.name = name
#         self.species =species
#     def set_species(self, species):
#         if species not in Pet.allowed: 
#             raise ValueError(f"You can't have a {species} pet")
#         self.species = species


# cat = Pet("Blue", "cat")
# dog = Pet("Wyatt", "dog")
# print(dog)
# print(dog.species)
# dog.species = "rat"
# print(dog.species)
# Pet.allowed.append("pig")
# print(Pet.allowed)


# class Chicken:
#     total_eggs = 0
#     def __init__(self, species, name, eggs=0):
#         self.species = species
#         self.name = name
#         self.eggs = eggs
#     def lay_egg(self):
#         self.eggs += 1
#         Chicken.total_eggs += 1
        
# c1 = Chicken(name="Alica", species="Patridge Silkie")
# c2 = Chicken(name="Amelia", species="Speckled Sussex")
# Chicken.total_eggs
# c1.lay_egg()
# c2.lay_egg()
# c2.lay_egg()
# print(Chicken.total_eggs)













    






























