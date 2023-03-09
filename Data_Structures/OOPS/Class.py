class Dog:
    
    # Class attribute
    species = "Canis familiaris"
    
    def __init__(self, name, age):              # only class methods and constructors require self 
        self.name = name                    # instance attributes 
        self.age = age
        
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

print(buddy.name)
print(miles.age)
print(miles.species)