class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)


    def __repr__(self) -> str:
        return f"{self.name} - {self.age}\n"

sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 37, 68, 95)


player = [sakib, musfiq,kamal,jack,kalam]


oldest = max(player, key=lambda player: player.age)

print(oldest)


"""
______________________________________________________
Class Method               |      Static Method
______________________________________________________
1 - Class Method Can Modify Inner Properties - Static Method Can't Modify Inner Properties

2 - IN Class Method class take (cls) as first argument - Static method don't take any specific parameter

3 - class method take cls as parameter and know about the state - Static method don't know about the class state

4 - 

"""


"""
- Write what are getter and setter with proper examples

When i Class Restrict Unauthorized Access to the class Properties. class make them private or Protected properties.  after doing that if we need to fetch or update the properties we can't do that directly on that case we have to use 'Getter' and 'Setter'
- 'getter' used for accessing properties which are directly not available rather we have to use different class to access. also 'setter' are used for updating properties which are not directly available.this is done for unauthorized or unwanted modifying properties
- 'Setter' are used for modifying class properties


"""


"""
- Explain the difference between inheritance and composition with proper examples.


difference between inheritance and composition is when a class extends from other class as parent - child 
the child inherit all the methods and properties from the parent
this is called inheritance but 
when a class use other class a inside that. like storing data of some class
it called composition. Composition class don't inherit from parent but rather use a class inside to store data type.

"""





