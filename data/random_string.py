import random
import datetime

# random.randint(1, 100)  # генерация от 1 до 100
# random.randrange(100)  # генерация одного числа от 1 до 100
# random.random()  # генерация одного числа от 0 до 1
# 100*random.random()

s = "qwertyu1234567"

print(random.choice(s))
print(random.choices(s, k=5))




# t = datetime.datetime.now()
# print(t.timestamp())