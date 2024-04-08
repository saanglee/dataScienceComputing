# 오버로딩, 오버라이딩 

# 오버로딩 (Overloading)
# 동일한 연산자(또는 메서드)가 서로 다른 자료형을 처리하는 것
# 같은 클래스 내에 같은 이름의 메서드를 사용하는 것 - 덮어쓰는 경우가 돼서 잘 안씀


# 오버라이딩 (Overriding)

class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def speak(self):
    print(f"{self.name} is speaking")

class CS_Student(Student):
  def __init__(self, name, age, major):
    super().__init__(name, age)
    self.major = major
  
  def speak(self): # 오버라이딩: 부모클래스의 메서드를 자식클래스에서 재정의 (덮어씀)
    print(f"{self.name} is speaking about CS / major: {self.major}")
    
student = Student("Tom", 21)
student.speak() # Tom is speaking    

cs_student = CS_Student("Alice", 20, "CS")
cs_student.speak() # Alice is speaking about CS / major: CS