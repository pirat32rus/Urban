#1).
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda f, s: f == s, first, second))
print(result)

#2).
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for data in data_set:
                file.write(str(data) + '\n')
                
    return write_everything

# Пример
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#3).
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words
        
    def __call__(self):
        return choice(self.words)

# Пример
first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Возможно')

print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
