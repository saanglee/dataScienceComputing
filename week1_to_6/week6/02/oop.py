# 객체지향 프로그래밍(OOP)의 상속과 다형성 (inheritance and polymorphism)
# Python의 상속과 다형성
# Method overriding과 Method overloading의 차이

# 01 상속 (Inheritance)
# class 자식클래스명(부모클래스명):

class Vehicle:
  def __init__(self, name, color):
    self.__name = name # private 변수
    self.__color = color
    
  def getColor(self):
    return self.__color
  
  def setColor(self, color):
    self.__color = color
  
  def getName(self):
    return self.__name

class Car(Vehicle):
  def __init__(self, name, color, model):
    super().__init__(name, color) # 부모클래스의 생성자 호출: name, color 초기화
    self.__model = model # Car 클래스에서 추가된 속성
    
  def getDescription(self):
    # return self.getName() + self.__model + " in " + self.getColor() + " color"
    return f"Name: {self.getName()}, Model: {self.__model}, Color: {self.getColor()}"

c = Car("Toyota Corolla", "Red", "1977")
# print(c.getDescription())


# 02 다중 상속 (Multiple Inheritance)
# class 자식클래스명(부모클래스1, 부모클래스2, ...):

class MySuperClass1:
  def method_super1(self):
    print("method_super1 method called")

class MySuperClass2:
  def method_super2(self):
    print("method_super2 method called")

class ChildClass(MySuperClass1, MySuperClass2):
  def child_method(self):
    print("child method")

c = ChildClass()
# c.method_super1()
# c.method_super2()

class ParentOne:
  def func(self):
    print("Parent One 함수 호출")

class ParentTwo:
  def func(self):
    print("Parent Two 함수 호출")

class Child(ParentOne, ParentTwo):
  def childFunc(self):
    ParentOne.func(self)
    ParentTwo.func(self)

objectChild = Child()

objectChild.childFunc() # Parent One 함수 호출 Parent Two 함수 호출
objectChild.func() # Parent One 함수 호출