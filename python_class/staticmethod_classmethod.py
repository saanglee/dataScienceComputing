"""
class에 decorator없이 method선언하면 instance method
  첫번째 매개변수로 class instance를 받음 = self
  instance method는 self를 통해 instance속성attribute에 접근하거나 다른 인스턴스 메서드를 호출
"""

class Counter:
  # 3개의 인스턴스 메서드로 이루어진 클래스 Counter
  # 각 인스턴스 메서드는 self라는 첫번째 parameter있음 
  
  # init method -> 인자로 넘어온 value값을 객체의 value속성에 할당
  def __init__(self, value = 0):
    self.value = value
  
  # increment, decrement method -> value 속성값을 변경
  def increment(self, delta = 1):
    self.value += delta 
  def decrement(self, delta = 1):
    self.value -= delta
    
# instance method는 instance를 반드시 먼저 생성하고 instance를 대상으로 호출해야함
counter = Counter() # instance counter 생성
print(counter.value)
counter.increment(3)
print(counter.value)



"""
@classmethod 데코레이터를 사용해서 클래스에 메서드를 선언하면 해당 메서드는 클래스(class) 메서드가 되며
첫번째 매개 변수로 클래스 인스턴스가 아닌 클래스 자체가 넘어오게 됩니다. 
이 첫번째 매개 변수의 이름은 보통 관행적으로 cls라고 하며
클래스 메서드는 이 cls를 통해 클래스 속성(attribute)에 접근하거나, 클래스 메서드를 호출할 수 있습니다. 
하지만, 인스턴스 메서드와 달리 인스턴스 속성에 접근하거나 다른 인스턴스 메서드를 호출하는 것은 불가능합니
"""


"""
@staticmethod 데코레이터를 사용해서 클래스에 메서드를 선언하면 해당 메서드는 정적(static) 메서드
정적 메서드는 인스턴스 메서드나 클래스 메서드와 달리 첫번째 매개 변수가 할당되지 않습니다. 
따라서 정적 메서드 내에서는 인스턴스/클래스 속성에 접근하거나, 인스턴스/클래스 메서드를 호출하는 것이 불가능합니다.
"""

class StringUtils:
    @staticmethod
    def toCamelcase(text):
        words = iter(text.split("_"))
        return next(words) + "".join(i.title() for i in words)

    @staticmethod
    def toSnakecase(text):
        letters = ["_" + i.lower() if i.isupper() else i for i in text]
        return "".join(letters).lstrip("_")




