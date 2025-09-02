class Cat:
    def ___init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a cat.My name is,{self.name},.I am , {self.age},yeard old.")
    def make_sound(self):
        print("Meow")
class Dog:
    def ___init__(self,name,age):
       self.name=name
       self.age=age
    def info(self):
       print(f"I am dog.My name is {self.name}. I am {self.age}years old.;")
    def make_sound(self):
        print("Bow Bow")
cat1 = Cat("Kunji",1)
dog1 = Dog("Jacky",5)
for i in (cat1,dog1):
    i.make_sound()
    i.info