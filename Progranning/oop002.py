class Student:
  def __init__(self,name,age,year,score ):
    self.name = name
    self.age = age
    self.year = year
    self.score = score
  def info(self):
        # Using self. to access the instance attributes
        print(f"Name: {self.name}, Age: {self.age}, Year: {self.year}, Score: {self.score}")
    
def main():
  record = get_student()
  #print(record.name)
  record.info()
    
    
    
def get_student():
  name = str(input("Name: \n"))
  age = int(input("Age \n"))
  year = str(input("Year: \n"))
  score = int(input("Score: \n"))
  student = Student(name,age,year,score)
  return student
    
    
    
if __name__=="__main__":
  main()