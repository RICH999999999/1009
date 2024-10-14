#Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

#Вызовы функции с разным количеством аргументов
print_params()                  # Без аргументов
print_params(10)                # Только a
print_params(10, 'новая строка') # a и b
print_params(b=25)              # Только b
print_params(c=[1, 2, 3])       # Только c

#Распаковка параметров
values_list = [3.14, 'текст', False]
values_dict = {'a': 42, 'b': 'слово', 'c': None}

print_params(*values_list)   # Распаковка списка
print_params(**values_dict)  # Распаковка словаря

#Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)    # Распаковка списка и передача 42
