import random

rng = random.Random() # random number generator
print(rng.random())
print(rng.randrange(1, 7))

odd = random.randrange(1, 100, 2) # return an odd number between 1 and 100
print(odd)

guess = rng.randint(1, 100) # return a random number between 1 and 100
print(guess)

dinner = random.choice(['pizza', 'pasta', 'salad', 'sushi'])
print(dinner)

# 5 random numbers between 1 and 10
xs = list(range(1, 11))
rng = random.Random()
rng.shuffle(xs) # shuffle 많이 씀!
result = xs[:5] 
print(result)

