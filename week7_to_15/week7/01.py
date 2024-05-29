import random

class Student:
  def __init__(self, name: str, department: str):    
    # generate student number
    self.__student_number = random.randint(1000, 9999)
    self.__name = name
    self.__department = department
      
  def __str__(self):
      info = f"Name: {''.join(self.__name)}\nStudent ID: 202171{self.__student_number}\nDepartment: {''.join(self.__department)}"
      return info
  
  # def get_info(self):
  #   info = f"Name: {''.join(self.__name)}\nStudent ID: 202171{self.__student_number}\nDepartment: {''.join(self.__department)}"
  #   return info
        
def main():
    name = input("Input Student Name: ")
    department = input("Input Department: ")
    
    #################
    student = Student(name, department)
    
    print(student)
    #print(student.get_info())

if __name__ == "__main__":
    main()