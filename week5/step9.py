"""
Object-Oriented Programming
객체지향 프로그래밍
"""

class Card:
  def __init__(self, suit, rank, face_up = True): # 기본값 지정 가능 
    # self: class 내부에 정의하는 모든 method의 첫번째 parameter는 "self"
    # self는 생성될 객체 자신을 가리키는 이름임
    self.suit = suit
    self.rank = rank
    self.face_up = face_up
    # 속성변수: 클래스 내부 전역에서 사용 가능
    
card1 = Card('Spade', '7', True)
# print(card1) # <__main__.Card object at 0x10251efd0>
# print(card1.suit, card1.rank, card1.face_up) # Spade 7 True
# print('card1.suit:', card1.suit) # card1.suit: Spade

# 객체의 속성 수정 가능
card1.rank = 'A'
# 그러나 객체 내부 속성 변수를 외부에서 직접 노출? 변경가능한 것은 좋지 않음

# 간판 문자열
# 객체를 실행창에서 참조하면 보여줄 문자열을 정의할 수 있음
class Card:
  def __init__(self, suit, rank, face_up = True):
    self.suit = suit
    self.rank = rank
    self.face_up = face_up
    
  def __str__(self):
    if self.__face_up:
      return self.__suit + "." + self.__rank
    else:
      return "xxxxx" + "." + "xx"
  
  # flip method
  def flip(self):
    self.face_up = not self.face_up
    
  # 클래스 속성 정의 가능
  # 튜플 처럼 변경 불가능한 속성으로 정의하면 안전!
  suits = ('Spade', 'Heart', 'Diamond', 'Clover')
  ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    
# card2 = Card('Spade', '7') # suit를 외부에서 지정함
# card2.flip() # True -> False
# print(Card.suits) # ('Spade', 'Heart', 'Diamond', 'Clover')
# print('card2.suits: ', card2.suits) # ('Spade', 'Heart', 'Diamond', 'Clover')
# print(Card.ranks) # ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

"""
객체 캡슐화 (Encapsulation)
- 객체의 속성(속성변수)을 외부에서 직접 접근하지 못하게 하는 것
- 비공개 속성변수
  - 속성변수 이름 앞에 __를 붙이면 비공개 속성변수로 만들 수 있음
  - 비공개 속성변수는 클래스 내부에서만 접근 가능, 외부에서 직접 접근 불가
"""

class Card3:
  # 비공개private 속성 변수
  __suit = ('Spade', 'Heart', 'Diamond', 'Clover')
  __rank = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    
  def __init__(self, suit, rank, face_up = True):
    self.__suit = suit
    self.__rank = rank
    self.__face_up = face_up
    
  def flip(self):
    self.__face_up = not self.__face_up
    
  # 공개용 메서드 사용
  def get_suit(self):
    return self.__suit
  def get_rank(self):
    return self.__rank
  def get_face_up(self):
    return self.__face_up
  
  # 프로퍼티 장식자
  # @property
  # def suit(self):
  #   return self.__suit
  
  
# print(Card3.__suit) # AttributeError: type object 'Card3' has no attribute '__suit'
# print(Card3.get_suite()) # AttributeError: type object 'Card3' has no attribute 'get_suite'

card3 = Card3('Spade', '7')
print(card3.get_suit()) # Spade


"""
정적 메서드 static method
- 클래스 고유 기능을 정의하기위한 메서드
- 메서드 정의 앞에 @staticmethod 장식자를 붙임
- 객체에 속해있지 않기때문에 self 파라미터 사용하지 않음
- 객체가 없어도 클래스 이름으로 호출 가능
- 그 외 일반 메서드와 동일하게 호출 가능
"""

class Rectangle:
  count = 0 # 클래스 변수
 
  def __init__(self, width, height):
    self.width = width
    self.height = height
    Rectangle.count += 1
  
  # 인스턴스 메서드
  def calcArea(self): 
    area = self.width * self.height
    return area
  
  # 정적 메서드
  @staticmethod
  def isSquare(rectWidth, rectHeight):
    return rectWidth == rectHeight
  
  # 클래스 메서드
  @classmethod
  def printCount(cls):
    print(cls.count)
    
    
square = Rectangle.isSquare(5, 5)
print(square) # True

rect1 = Rectangle(5, 5)
rect2 = Rectangle(2, 5)
rect1.printCount() # 2

"""
Docstring
클래스에 설명을 달아주기 위함
"""