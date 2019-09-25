class Animal:
    def __init__(self, name,age):
        self.name = name
        self.health = 0
        self.happiness = 0
        self.age=age
    def display_info(self):
        print(self.name,self.age, self.health, self.happiness)
        return self
    def feed(self):
        raise NotImplementedError
class Lion(Animal):
    def __init__(self, name,age):
        super().__init__(name,age)
        self.health = 5
        self.happiness = 3
    def feed(self):
        self.health += 7
        self.happiness += 3
        return self
class Tiger(Animal):
    def __init__(self, name,age):
        super().__init__(name,age)
        self.health = 2
        self.happiness = 6
    def feed(self):
        self.health += 8
        self.happiness += 5
        return self
class Bear(Animal):
    def __init__(self, name,age):
        super().__init__(name,age)
        self.health = 7
        self.happiness = 1
    def feed(self):
        self.health += 2
        self.happiness += 8
        return self
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def lion(self, name,age):
        self.animals.append(Lion(name,age))
        return self.animals[-1]
    def tiger(self, name,age):
        self.animals.append(Tiger(name,age))
        return self.animals[-1]
    def bear(self, name,age):
        self.animals.append(Bear(name,age))
        return self.animals[-1]
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
zoo1 = Zoo("Chuy")
zoo1.print_all_info()
zoo1.lion("tt",2).feed().feed()
zoo1.tiger("i.t",5).feed()
zoo1.bear("y",5).feed().feed()
zoo1.print_all_info()