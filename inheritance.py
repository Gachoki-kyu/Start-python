class animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age

class man(animal):
    def __init__(self,name,age):
        super().__init__(name,age)
        print(f"my name is {self.name} and i am {self.age}")

    def speak(self):
        print('i can also talk')
    
    def move(self):
        print('i move by walking')

class dog(man):
    def __init__(self,name,age):
        super().__init__(name,age)
        print(f"its a {self.name}, he is {self.age} years since was born")
    
    def speak(self):
        print("i bark")

man1 = man('ben',23)
man1.speak()
man1.move()

p = dog("wendy",4)
p.move()
p.speak()

   



