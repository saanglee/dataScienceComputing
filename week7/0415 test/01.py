import random

class Student:
  def __init__(self, name: str, department: str):    
    # generate student number
    self.__student_number = random.randint(10000000, 99999999)
    
    self.__name = name
    self.__department = department
    
      
  def __str__(self):
      ### Edit Here ###
      
      # save student info
      info = f"Name: {''.join(self.__name)}\nStudent ID: {self.__student_number}\nDepartment: {''.join(self.__department)}"
      return info
        
def main():
    # input student name, department
    name = input("Input Student Name: ").split()
    department = input("Input Department: ").split()
    #################
    student = Student(name, department)
    
    print(student)

if __name__ == "__main__":
    main()