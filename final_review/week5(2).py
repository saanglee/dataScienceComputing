# week5 (2) Bank Class

class Bank:
    def __init__(self):
        self.__name = ''
        self.__pw = ''
        self.__money = None
        self.__info = {}
        self.__pattern = {} # 소비 패턴
        self.__is__logged_in = False

    # 초기 화면

    def register(self):
        self.__name = input('이름 입력: ')
        self.__pw = input('비번 입력: ')

        if self.__name in self.__info:
            print('이미 존재하는 사용자')
            self.register()

        else:
            with open('info.txt', 'a') as f: # 파일 추가 모드 'a' 기존 파일이면 데이터 추가, 없는 파일이면 새 파일(info.txt) 생성
                f.write(self.__name + ', ' + self.__pw + '0\n')

            self.__info[self.__name] = [self.__pw, 0] # info 딕셔너리 {name: [pw, 0]}
            print('계정 등록 완료')
            self.login()

    def login(self):
        self.__name = input('이름: ')
        self.__pw = input('비번: ')

        if self.__name not in self.__info:
            print('존재하지 않는 사용자')
            self.login()
            return
        elif self.__pw != self.info[self.__name][0]:
            print('비밀번호 틀림')
            self.login()
            return
        else:
            self.__is_logged_in = True
            self.__pattern[self.__name] = []
            print(f'{self.__name}님 환영합니다.')
            self.program()

    # 메인화면
    def deposit(self): # 입금
        self.__money = int(input('입금액: '))
        self.__info[self.__name][1] += self.__money

        print(f'입금 후 잔액: {self.__name}: {self.__info[self.__name][1]}')
        self.program()

    def spend(self): # 출금
        print(f'현재 잔액: {self.__info[self.__name][1]}')
        self.__money = int(input('출금액: '))
        self.__info[self.__name][1] -= self.__money

        # 소비패턴 기록
        self.__pattern[self.__name].append(self.__money)
        print(f'금 후 잔액: {self.__name}: {self.__info[self.__name][1]}')
        self.program()

    def s_pattern(self):
        x = len(self.__pattern[self.__name]) # 몇번 출금
        y = self.__pattern[self.__name]      # 출금 리스트

        print(f'평균 사용액: {np.mean(self.__pattern[self.__name])}')
        # np.mean(..) 리스트의 평균을 구함

        plt.plot(list(range(1, x+1)), y, 'ro') # plt.plot(x축값, y축값, 'ro') ro는 red circle  
        plt.savefig('spend_pattern.png')       # plot 저장
        plt.show()

        self.program()


    # Controller
    def program(self):

        # 로그인 상태
        if self.__is_logged_in: # 메인화면
            print('[메인화면] >>> 0을 누르면 로그아웃됩니다 <<<')
            print('1. 입금 2. 출금 3. 소비 패턴 보기')
            choice = input('>>> ')
            
        if choice == '1':
            self.deposit()
        elif choice == '2':
            self.spend()
        elif choice == '3':
            self.s_pattern()
        elif choice == '0':
            print('>>> 로그아웃합니다. <<<')
            self.__is_logged_in = False
            return

        # 초기화면
        else:
            with open('info.txt', 'r') as f: # info.txt파일을 읽기 모드'r'로 열기
                for line in f:
                    name, pw, money = line.split(',')
                    money = money.replace('\n', '')
                    self.__info[name] = [pw, int(money)]




        





        
        
