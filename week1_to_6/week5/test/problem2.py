# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

class Bank:
    def __init__(self):
        self.__name = '' #string
        self.__pw = '' #string
        self.__money = None #int
        self.__info = {} #dictionary
        self.__pattern = {} #dictionary
        self.__is_logged_in = False #boolean
        
        
    ### ========== 초기 화면 ========== ###

    def register(self):
      self.__name = input('이름을 입력하세요: ')
      self.__pw = input('비밀번호를 입력하세요: ')
      
      if self.__name in self.__info:
        print('>>> 이미 존재하는 사용자입니다 <<<')
        self.register() 
      
      else: 
        with open('info.txt', 'a') as f:
          f.write(self.__name + ', ' + self.__pw + ' 0\n')

        self.__info[self.__name] = [self.__pw, 0]
        print('>>> 계정이 등록되었습니다 <<<')
        self.login()
      
      
    def login(self):
      self.__name = input('이름을 입력하세요: ')
      self.__pw = input('비밀번호를 입력하세요: ')
      
      if self.__name not in self.__info:
        print('>>> 존재하지 않는 사용자입니다 <<<')
        self.login()
        return
      
      elif self.__pw != self.__info[self.__name][0]:
        print('>>> 비밀번호가 틀렸습니다 <<<')
        self.login()
        return
      
      else:
        self.__is_logged_in = True
        self.__pattern[self.__name] = []
        print(self.__name + '님 환영합니다!')
        self.program()
    
    ### ========== 메인 화면 ========== ### 

    def deposit(self):
      # input deposit amount
      self.__money = int(input('입금액을 입력하세요: '))
      self.__info[self.__name][1] += self.__money 

      print('입금 후 잔액: ', self.__name + ':', self.__info[self.__name][1])
      self.program()

    def spend(self):
      print('현재 잔액', self.__name + ':', self.__info[self.__name][1])
      self.__money = int(input('출금액을 입력하세요: '))
      self.__info[self.__name][1] -= self.__money
      
      self.__pattern[self.__name].append(self.__money)
      print('출금 후 잔액: ', self.__name + ':', self.__info[self.__name][1])
      self.program()
      
    def s_pattern(self):
      x = len(self.__pattern[self.__name])
      y = self.__pattern[self.__name]
      
      print('평균 사용 금액:', np.mean(self.__pattern[self.__name]))
      
      plt.plot(list(range(1,x+1)), y, 'ro')
      plt.savefig('spend_pattern.png')
      plt.show()
      
      self.program()

    def program(self): # Controller

        if self.__is_logged_in: # Main screen
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
        
        else: # Initial screen
          with open('info.txt', 'r') as f:
            for line in f:
              with open('info.txt', 'r') as f:
                for line in f:
                  name, pw, money = line.split(',')
                  money = money.replace('\n', '')
                  self.__info[name] = [pw, int(money)]
          
          print('[초기화면] >>> 0을 누르면 종료됩니다 <<<')
          print('1. 계정등록 2. 로그인')
          choice = input('>>> ')
          
          if choice == '1':
            self.register()
          elif choice == '2':
            self.login()
            self.program()
          elif choice == '0':
            print('>>> 프로그램을 종료합니다 <<<')
            return

b = Bank()

b.program()