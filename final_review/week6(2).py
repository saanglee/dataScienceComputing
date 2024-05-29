# week6 (2) 1~16 number


class GameController:
    def __init__(self, name:str):
        self.__name = name
        self.__target = Target()

    def play(self):
        print("Game Start")

        target_num = self.__target.get_target_num()
        # prob =
        # ... 


class Target:
    def __init__(self):
        self.__prob = 1/16

    def get_target_num(self) -> int:
        self.__target_num = random.randint(1, 16) # 1~16사이 랜덤 정수 지정
        return self.__target_num

    def get_prob(self) -> float:
        self.__prob *= 2            # 2배수
        print()
        return self.__prob

    def reset_prob(self):
        self.__prob = 1/16


class Decision:
    def __init__(self, target_num: int, user_num: int, prob: float):
        self.__target_num = target_num
        self.__user_num = user_num
        self.__prob = prob

    @property                       # @property decorator는 특별한 attritbute를 정의할 때 사용
    def target_num(self) -> int:    # 내부적으로는 method 호출이지만 외부에서는 attrubute 접근처럼 사용할 수 있음
        return self.__target_num    # private attrubute인 target_num에 직접 접근하는 것을 방지,(캡슐화) property를 통해 접근
                                    # @property만 정의된 경우 이 attrubute(target_num)은 읽기 전용: 값 조회만 가능, 변경 불가
    
    @property
    def user_num(self) -> int:
        return self.__user.num

    @property
    def prob(self) -> float:
    return self.__prob

    @property
    def updown(self) -> str:
        if self.__target_num > self.__user.num:
            return "UP! try again"
        elif self.__target_num < self.__user.num:
            return "DOWN! try again"

    def iswin(self) -> bool:
        return self.__target_num == self.__user_num
    def islose(self) -> bool:
        return self.__prob >= 1


class Reader():
    
    @staticmethod                       # @staticmethod decorator 정적메서드 정의: 클래스의 인스턴스나 클래스 자체에 대한 참조 없이 호출될 수 있는 메서드
    def get_name() -> str:              # 클래스나 인스턴스 속성이나 메서드에 접근하지 않음, 즉 클래스 상태와 무관하게 동작 가능
        name = input("input name: ")    # 클래스의 인스턴스 없이도 호출 가능 예) Reader.get_name()
        return name                     # @staticmethod 없으면 클래스 인스턴스 필요 예) r = Reader() 하고, r.get_name() 

    @ staticmethod
    def ox(message:str) -> bool:
        ans = input("Continue(y/n): ")
        if ans = "y":
            return True
        elif ans != "n":
            print("Please input y or n")
            return Reader.ox(message)
    
    @staticmethod
        def input_number() -> int:
        return int(input("Input number: "))













    




