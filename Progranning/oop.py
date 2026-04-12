class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
        
        
def main():
    x = get_person()
    print(x.name)













def get_person():
    #person = Person()
    #person.name = input("name?\n")
    name = input("name: \n")
    age = input("Age: \n")
    person = Person(name,age)
    return person
    

if __name__=="__main__":
    main()
        