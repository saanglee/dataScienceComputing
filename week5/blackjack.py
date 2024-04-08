"""
Model
- Card
- Hand
- PlayerHand
- Deck

Controller
- BlackjackController
- main() ?

View
- Reader
"""



class Card:
  # 각 카드의 속성(attributes): 모양(suit), 숫자(rank), 카드가 앞면으로 되어 있는지 여부(face_up)
  def __init__(self, suit, rank, face_up=True):
    # Card.__suits와 Card.__ranks에 해당 모양과 숫자가 포함되어 있는지 확인하여 유효한 카드인지를 검사
    # 이 두 변수는 카드의 가능한 모양과 숫자를 나타내는 리스트일 것
    if suit in Card.__suits and rank in Card.__ranks:
      # 모양과 숫자가 유효한지 확인한 후, 비공개 속성(private attribute)으로 설정됨
      self.__suit = suit
      self.__rank = rank
      self.__face_up = face_up
    else:
      print("Error: Not a Valid Card")
    
    self.__value = Card.__rank.index(self.__rank) + 1 
    if self.__value > 10: # 11이상이면
      self.__value = 10

class Deck:
  def __init__(self):
    self.__deck = Card.fresh_deck()
    print("<< A brand-new deck of card! >>")

class Hand:
  def __init__(self, name = "Dealer"):
    self.__name = name
    self.__hand = []

class PlayerHand(Hand):
  def __init__(self, name):
    #  super().__init__(name) 호출을 통해 상위 클래스인 Hand의 생성자를 호출하고, 플레이어 이름을 초기화
    super().__init__(name)
    self.__chips = 0

  def earn_chips(self, n):
    self.__chips += n
    print("You have", self._chips, "chips.")
  
  def lose_chips(self, n):
    self.__chips -= n
    print("You have", self.__chips, "chips.")



# View
# Reader 클래스는 사용자 입력을 처리하는 메서드
class Reader:
  @staticmethod # staticmethod로 정의 -> Reader.register()와 같이 클래스 이름을 사용하여 직접 호출 가능
  def register():
    return input("Enter your name: ")
  
  @staticmethod
  # 사용자에게 'o' 또는 'x'의 입력을 요청하는 메서드
  def ox(message):
    response = input(message).lower()
    # 입력이 'o'나 'x'가 아닌 경우, 올바른 입력을 받을 때까지 사용자에게 반복해서 동일한 메시지를 표시
    while not (response == 'o' or response == 'x'):
      response = input(message).lower()
    return response == 'o' # 사용자가 'o'를 입력하면 True를, 'x'를 입력하면 False를 반환
  

# Controller 

class BlackjackController:
  def __init__(self, name):
    self.__player = PlayerHand(name)
    self.__dealer = Hand()
    self.__deck = Deck()
    
  def play(self):
    # 게임 로직
    print('== new game ==')
    
    player = self.__player
    dealer = self.__dealer
    deck = self.__deck
    
    # deck.next()를 호출 -> deck에서 카드를 한 장씩 번갈아 가며 두 번 받는다.
    # 딜러의 두 번째 카드는 open=False -> 게임 시작 시에는 보이지 않는다.
    player.get(deck.next())
    dealer.get(deck.next())
    player.get(deck.next())
    dealer.get(deck.next(open=False))
    
    print('Dealer: ', dealer)
    print(player.name, ':', player)
    
    # player 총 점수가 21점인지 확인하고, 블랙잭이면 플레이어가 이기고 칩을 두 배로 받는다.
    if player.total == 21:
      print("Blackjack!", player.name, "wins.")
      player.earn_chips(2)
    # 플레이어의 총점이 21점 미만이면, Reader.ox를 통해 플레이어에게 추가 카드를 받을지 여부를 물어본다.
    else:
      while player.total < 21 and Reader.ox(player.name + ": Hit? (o/x) "):
        # 플레이어가 추가 카드를 원하면 deck.next()를 통해 덱에서 카드를 한 장 받고, 새로운 카드를 포함한 핸드를 출력한다. ?
        player.get(deck.next())
        print(player.name, ":", player)
        
        # 플레이어가 21점을 넘으면 ("busts"), 게임에서 지고 칩을 하나 잃는다.
        if player.total > 21:
          print(player.name, "busts!")
          player.lose_chips(1)
        
        # 플레이어가 21점을 넘지 않았고
        else:
          # 딜러의 점수가 16점 이하면, 딜러는 계속해서 카드를 뽑는다.
          while dealer.total <= 16:
            dealer.get(deck.next())
          # 딜러가 21점을 넘으면 ("Dealer busts!"), 플레이어가 이기고 칩을 하나 얻는다. 
          if dealer.total > 21:
            print("Dealer busts!")
            player.earn_chips(1)
          elif dealer.total == player.total:
            print("We draw.")
          elif dealer.total > player.total:
            print(player.name, "loses.")
            player.lose_chips(1)
          else:
            print(player.name, "wins.")
            player.earn_chips(1)
            
    # dealer.open()을 호출하여 딜러의 모든 카드를 공개한다.
    dealer.open()
    # 게임의 최종 결과를 출력한다.
    print("Dealer: ", dealer)
    
    # player.clear()와 dealer.clear()를 호출하여 플레이어와 딜러의 손을 비워 다음 라운드를 준비한다.
    player.clear()
    dealer.clear()
  
  # main 함수는 프로그램의 시작점으로, 플레이어 이름을 등록하고 게임을 시
  # 플레이어가 게임을 계속하고 싶지 않다면, 루프를 빠져나오고 게임을 종료
  def main():
    print("Welcome to SMaSH Casino!")
    name = Reader.register()
    game = BlackjackController(name)
    while True:
      game.play()
      if not Reader.ox("Play more, ", + name + "? (o/x) "):
        break
    print("Bye, " + name + "!")
  
  if __name__ == "__main__":
    main()

      
    