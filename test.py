# Структура данных
# Tuple, List, Dictionary, Set

"""# Tuple -> Брать индекс, длину, дубликаты
names = ('Atabek', 'Murtazaev', 'Atabek')  # Группа
print(names, type(names))

# Изменять, Добавлять, Удалять, дубликаты
names = ['Atabek', 'Murtazaev', 'Atabek']  # Группа
print(names, type(names))

# Изменять, Добавлять, Удалять
names = {
    'name': ('Atabek', 'Sultan', 'Atabek',),  # Очередь
    'surname': 'Murtazaev',
    'name': ('Atabek', 'Sultan', 'Atabek',), 
}
print(names)

# Изменять, Добавлять, Удалять
print(names['name'])

names = {'Atabek', 'Murtazaev', 'Atabek'}  # Толпа
print(names)"""

from random import randint
n = 5

numbers = []
for i in range(n):
    numbers.append(randint(1, 10))

print(numbers)
print(f'Summa: {sum(numbers)}')
print(f'Max: {max(numbers)}')
print(f'Min: {min(numbers)}')

# Удаляем дубликаты

new = list(set(numbers))

duplicates = []
for i in range(len(numbers)):
    if numbers[i] not in duplicates:
        duplicates.append(numbers[i])
print(f'Без дубликатов: {duplicates}')
print(f'Без дубликатов: {new}')


# Сортировка
for i in range(len(numbers)): # 5
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(f'После сортировки: {numbers}')