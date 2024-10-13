#learning classes and objects
class wen:
    x = 5 # class declaration
obj = wen()
print(obj.x)
 # the above object declaration is not mostly used in real world problems

 # using the _init_() function
class person:
    def __init__(self,name,age):
     self.name = name
     self.age = age

    def speak(self):
        print(f"my name is {self.name}and i am{self.age}years old")


p1 = person("ben", 23)
p1.speak()





