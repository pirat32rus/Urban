#Requests

import requests

response = requests.get('https://requests.readthedocs.io/en/latest/index.html')
if response.status_code == 200:
    data = response.text
    print("Данные:", data)
else:
    print("Ошибка:", response.status_code)

#Pandas

import pandas as pd

file_path = 'data.csv'
data = pd.read_csv(file_path)

print("Первые 5 строк данных:")
print(data.head())

print("\nИнформация о данных:")
print(data.info())

print("\nКоличество пропущенных значений по столбцам:")
print(data.isnull().sum())

print("\nОсновная статистика числовых столбцов:")
print(data.describe())

if 'категория' in data.columns:
    print("\nГруппировка по категории:")
    numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns
    print(data.groupby('категория')[numeric_cols].mean())

#Matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')
plt.title('Простой график')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()

data = [1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
plt.hist(data, bins=5, alpha=0.7, color='blue')
plt.title('Гистограмма')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.show()


# Эти три библиотеки (requests, pandas, matplotlib) внушительно расширяют возможности Python.
#С помощью requests вы можете легко взаимодействовать с веб-сервисами и получать данные из интернета.
#pandas предлагает мощные методы анализа и обработки табличных данных, что делает работу с данными более простой и эффективной.
#Наконец, matplotlib позволяет визуализировать данные и представлять результаты анализа в доступной и понятной форме.