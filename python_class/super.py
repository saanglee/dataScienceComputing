"""
자식클래스(subclass)에서 super() 사용하면 부모클래스(super class)의 메서드나 속성에 접근이 가능
특히 메서드 오버라이딩(overriding) 부모클래스 메서드 재정의할 때 super() 사용

"""


class Parent:
    def __init__(self):
        print("Parent __init__")
        self.value = "Parent's value"

class Child(Parent):
    def __init__(self):
        super().__init__()  # Parent 클래스의 __init__ 메서드 호출
        print("Child __init__")
        self.value = "Child's value"

# Child 인스턴스 생성 시, 부모 클래스의 __init__ 도 호출됩니다.
child = Child()
print(child.value)  # "Child's value" 출력