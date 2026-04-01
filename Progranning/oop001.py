class Dog:
  def __init__(self,name,age,origin,food):
    self.name = name
    self.age = age 
    self.origin = origin
    self.food = food
  def info(self):
    print(f"Name:{name},Age:{age},origin:{origin},food:{food}")


 
 
    
    
def woof():
  name = input("dog name: ")
  a = input("dog age: ")
  o = input("dog native to: ")
  f = input("what food your dog eat? : ")
  dog_record = Dog(name,a,o,f)
  return dog_record


print(woof().name)
