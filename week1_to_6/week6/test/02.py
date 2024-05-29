import random

class GameController:
  def __init__(self, name: str):
    self.__name = name
    self.__target = Target()
      
  def play(self):
    print("Game Start")
    target_num = self.__target.get_target_num()
    # prob = 1/16
    # name = self.__name
    while True:
      target_num = self.__target.get_target_num()
      user_num = Reader.input_number()
      decision = Decision(target_num, user_num, self.__target.get_prob())
      
      if decision.iswin():
        print(f"{self.__name}, win!")
        print(f"Target number: {decision.target_num}, input number: {decision.user_num}, probability: {decision.prob}")
        if Reader.ox(f"{self.__name}, continue(y/n)"): # 재시작
          target_num = self.__target.get_target_num()
          # prob = 1/16
          self.__target.reset_prob()
        else:
          break
      elif decision.islose():
        print(f"{self.__name}, lose!")
        print(f"Target number: {decision.target_num}, input number: {decision.user_num}, probability: {decision.prob}")
        if Reader.ox(f"{self.__name}, continue(y/n)"): 
          target_num = self.__target.get_target_num()
          # prob = 1/16
          self.__target.reset_prob()
        else:
          break
      else:
        print(decision.updown)

  #     if decision.iswin() or decision.islose():
  #       self.handle_result(decision)
  #       if not Reader.ox(f"{self.__name}, continue(y/n)"):
  #         break
  #     else:
  #       print(decision.updown)
    
  # def handle_result(self, decision):
  #   result = "win" if decision.iswin() else "lose"
  #   print(f"{self.__name}, {result}!")
  #   print(f"Target number: {decision.target_num}, input number: {decision.user_num}, probability: {decision.prob}")
  #   self.__target.reset_prob()
        

class Target:
  def __init__(self):
    self.__prob = 1/16
  
  def get_target_num(self) -> int:
    self.__target_num = random.randint(1, 16)
    return self.__target_num
      
  def get_prob(self) -> float:
    self.__prob *= 2
    print('Target class) prob: ', self.__prob)
    return self.__prob
  
  def reset_prob(self):
    self.__prob = 1/16

class Decision:
  def __init__(self, target_num: int, user_num: int, prob: float):
    # save info
    self.__target_num = target_num
    self.__user_num = user_num
    self.__prob = prob
      
  @property
  def target_num(self) -> int:
    # return target_num
    return self.__target_num
      
  @property
  def user_num(self) -> int:
    return self.__user_num
      
  @property
  def prob(self) -> float:
    return self.__prob
      
  @property
  def updown(self) -> str:      
    if self.__target_num > self.__user_num:
      return "UP! Try again!"
    elif self.__target_num < self.__user_num:
      return "DOWN! Try again!"
      
  def iswin(self) -> bool:
    return self.__target_num == self.__user_num
      
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