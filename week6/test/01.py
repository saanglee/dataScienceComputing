class Category:
  # name:str
  # categ:str
  def __init__(self, name):
    self.__name = name
  
  def get_name(self) -> str:
    return self.__name
  
  def get_categ(self) -> str:
    all_veges = ['Potato', 'Broccoli', 'Carrot', 'Cabbage', 'Spinach', 'Tomato', 'Cucumber', 'Onion', 'Garlic', 'Pumpkin', 'Sweet Potato', 'Bell Pepper', 'Eggplant', 'Zucchini', 'Celery', 'Asparagus', 'Green Bean', 'Mushroom', 'Corn', 'Pea']
    if self.__name in all_veges:
      return "vegetable"
    else:
      return "fruit"
    

class Product(Category):
  # name:str
  # cost:float
  # quantity:int
  def __init__(self, name, cost, quantity):
    super().__init__(name)
    self.__cost = cost
    self.__quantity = quantity
      

  def get_cost(self) -> int:
    return self.__cost
  
  def get_quantity(self) -> int:
    return self.__quantity

  def inStock(self) -> bool:
    if self.__quantity >= 5:
      # print("재고가 충분합니다.")
      return True
  
  def update_quantity(self, nsold): 
    self.__quantity -= nsold
    return self.__quantity
    

class Finance:
    # money:float
  def __init__(self):
    self.__money = 0

  def get_money(self) -> int:
    return self.__money

  def update(self, product, nsold):
    self.__money += product.get_cost() * nsold
  
        

class Market:
    # cash:Finance
    # p_list:List[Product]
  def __init__(self, p_list):
    self.__cash = Finance()
    self.__p_list = p_list
    
  def get_cash(self) -> int:
    return self.__cash.get_money()

  def get_list(self) -> list:
    return self.__p_list

  def checkStock(self) -> int: 
    return len(self.__p_list)
    
  def sell(self, prod, nsold):
    if prod.inStock() == True:
      self.__cash.update(prod, nsold)
      prod.update_quantity(nsold)
    else:
      print(prod.get_name(), "은/는 재고가 적어 팔 수 없습니다.")
      # return False
  


#### Do not edit Here ####
potato = Product("Potato", 0.40, 20)
broccoli = Product("Broccoli", 0.60, 3)
mangosteen = Product("Mangosteen", 10.00, 5)
cucumber = Product("Cucumber", 13.00, 15)
spinach = Product('Spinach', 4.00, 30)
blueberry = Product('Blueberry', 5.00, 4)
grapefruit = Product('Grapefruit', 7.00, 17)


PL0 = Market([])
PL1 = Market([potato, broccoli])
PL2 = Market([mangosteen, blueberry, grapefruit])
market = Market([potato, broccoli, mangosteen, cucumber, spinach, blueberry, grapefruit])

print(PL0.checkStock() == 0)
print(PL1.checkStock() == 1)
print(PL2.checkStock() == 2)
print(market.checkStock() == 5)

for p in PL1.get_list():
    print(p.get_categ() == 'vegetable')

for p in PL2.get_list():
    print(p.get_categ() == 'fruit')

for p in market.get_list():
    if p in [broccoli, blueberry]:
        print(p.inStock() == False)
    else:
        print(p.inStock() == True)

for p,s in zip(market.get_list(), [15,15,3,8,20,2,13]):
    market.sell(p,s)

for p in [potato, broccoli, mangosteen, cucumber, spinach, blueberry, grapefruit]:
    print('현재 {}의 재고는 {}입니다'.format(p.get_name(), p.get_quantity()))

print('현재 수확물을 팔고 남은 돈은 {}입니다.'.format(market.get_cash()))