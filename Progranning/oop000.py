class Dog:
  def __init__(self,name,age,origin,food):
    self.name = name
    self.age = age 
    self.origin = origin
    self.food = food
  def info(self):
    print(f"Name:{self.name},Age:{self.age},origin:{self.origin},food:{self.food}")
    


 
 
    
    
def woof():
  name = input("dog name: ")
  age = input("dog age: ")
  origin =input("dog native to: ")
  food = input("what food your dog eat? : ")
  return Dog(name,age,origin,food)
  #print(a)
  #print(f"dog name is {Dog.name} {Dog.age}year old from {Dog.origin} eat {Dog.food}")
  
woof() 
