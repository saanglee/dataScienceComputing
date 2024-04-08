import random

class GameController:
  def __init__(self, name: str):
    self.__name = name
    self.__target = Target()
      
  def play(self):
    print("Game Start")
    tnum = self.__target.get_tnum()
    prob = 1/16
    name = self.__name
    while True:
      inum = Reader.input_number()
      prob = self.__target.get_prob()
      decision = Decision(tnum, inum, prob) 
      
      if decision.iswin():
        print(f"{name}, win!")
        print(f"Target number: {decision.tnum}, input number: {decision.inum}, probability: {decision.prob}")
        if Reader.ox(f"{name}, continue(y/n)"): # 재시작
          tnum = self.__target.get_tnum()
          prob = 1/16
        else:
          break
      elif decision.islose():
        print(f"{name}, lose!")
        print(f"Target number: {decision.tnum}, input number: {decision.inum}, probability: {decision.prob}")
        if Reader.ox(f"{name}, continue(y/n)"): 
          tnum = self.__target.get_tnum()
          prob = 1/16
        else:
          break
      else:
        print(decision.updown)

class Target:
  def __init__(self):
    self.__prob = 1/16
  
  def get_tnum(self) -> int:
    self.__tnum = random.randint(1, 16)
    return self.__tnum
      
  def get_prob(self) -> float:
    self.__prob *= 2
    print('Target class) prob: ', self.__prob)
    return self.__prob

class Decision:
  def __init__(self, tnum: int, inum: int, prob: float):
    # save info
    self.__tnum = tnum
    self.__inum = inum
    self.__prob = prob
      
  @property
  def tnum(self) -> int:
    # return tnum
    return self.__tnum
      
  @property
  def inum(self) -> int:
    return self.__inum
      
  @property
  def prob(self) -> float:
    return self.__prob
      
  @property
  def updown(self) -> str:      
    if self.__tnum > self.__inum:
      return "UP! Try again!"
    elif self.__tnum < self.__inum:
      return "DOWN! Try again!"
      
  def iswin(self) -> bool:
    return self.__tnum == self.__inum
      
  def islose(self) -> bool:
    return self.__prob >= 1 

class Reader():
  @staticmethod
  def get_name() -> str:
    # get player name from user
    name = input("Input name: ")
    return name

  @staticmethod
  def ox(message: str) -> bool:
    ans = input("continue(y/n): ")
    if ans == "y":
      return True
    elif ans != "n":
      print("Please input y or n")
      return Reader.ox(message)

  @staticmethod
  def input_number() -> int:
    return int(input("Input number: "))
        
def main():
    reader = Reader()
    name = reader.get_name()
    
    gamecontroller = GameController(name)
    gamecontroller.play()
    
if __name__ == "__main__":
    main()