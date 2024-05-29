# week7(1)
import random

class Student:
    def __init__(self, name:str, department:str):
        self.__student_number = random.randint(1000, 9999)
        self.__name = name
        self.__department = department

    def __str__(self):  # 클래스의 인스턴스를 
        info = f"Name: {''.join(self.__name)}\nStudent ID: 202171{self.__student_number}\nDepartment: {''.join(self.__department)}"
        return info



def main():
    name = input("name: ").split()
    department = input("Input Department: ").split()

    student = Student(name, department)
