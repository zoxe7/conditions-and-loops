# Задача 1. Проверка числа

n = -5
if n > 0:
    print("positive")  # положительное число
elif n < 0:
    print("negative")  # отрицательное число
else:
    print("zero")      # ноль


# Задача 2. Минимум из двух
a = 12
b = 7
if a < b:
    print(a)          # выводим минимальное значение
else:
    print(b)


# Задача 3. Делится ли на 3
n = 15
if n % 3 == 0:
    print("yes")       # делимость на 3
else:
    print("no")


# Задача 4. Сумма чисел от 1 до N
N = 7
sum_numbers = 0
for i in range(1, N + 1):
    sum_numbers += i     # накапливаем сумму
print(sum_numbers)       # сумма равна 28


# Задача 5. Все нечётные числа
for i in range(1, 16, 2):  # шаг равен 2, значит берем только нечётные
    print(i)


# Задача 6. Количество чётных
even_count = 0
for i in range(1, 21):
    if i % 2 == 0:
        even_count += 1    # увеличиваем счётчик чётных чисел
print(even_count)         # количество чётных чисел равно 10


# Задача 7. Найти букву в строке
s = "banana"
count_a = 0
for char in s:
    if char == 'a':       # считаем символы 'a'
        count_a += 1
print(count_a)            # количество букв 'a' равно 3


# Задача 8. Переворот строки
word = "hello"
reversed_word = ''
for char in word:
    reversed_word = char + reversed_word  # добавляем символ перед существующей строкой
print(reversed_word)                     # результат olleh


# Задача 9. Таблица умножения на число
num = 4
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")     # таблица умножения на 4


# Задача 10. Простая пирамидка
star_row = '*'
for _ in range(4):
    print(star_row)                      # печатаем строку звездочек
    star_row += '*'                      # добавляем одну звезду на следующей итерации


# Задача 11. Сумма чисел, кратных 3 или 5
N = 30
total_sum = 0
for i in range(1, N + 1):
    if i % 3 == 0 or i % 5 == 0:        # проверяем делимость на 3 или 5
        total_sum += i                   # прибавляем подходящее число
print(total_sum)                         # итоговая сумма равна 195


# Задача 12. Второе максимальное из трёх
a = 9
b = 17
c = 17
numbers = sorted([a, b, c])              # сортируем список
second_largest = numbers[1]              # берём второй элемент списка
print(second_largest)                    # вывод второго наибольшего значения


# Задача 13. Количество гласных в строке
s = "education"
vowels = ['a', 'e', 'i', 'o', 'u']
count_vowels = 0
for char in s:
    if char in vowels:                   # проверяем, входит ли символ в набор гласных
        count_vowels += 1                # увеличиваем счётчик
print(count_vowels)                      # итоговое количество гласных символов


# Задача 14. Проверка палиндрома
word = "level"
is_palindrome = True
for i in range(len(word)//2):
    if word[i] != word[-i-1]:            # сравниваем первый и последний символ
        is_palindrome = False
        break                            # прекращаем проверку при первом расхождении
print("yes" if is_palindrome else "no")  # вывод результата проверки


# Задача 15. Простые числа в диапазоне
primes = []
for num in range(2, 31):
    is_prime = True
    for j in range(2, int(num**0.5)+1):  # оптимизация: проверять только до квадратного корня
        if num % j == 0:
            is_prime = False
            break                        # если найдено деление нацело, число составное
    if is_prime:
        primes.append(num)               # сохраняем найденные простые числа
print(primes)                           # вывод простых чисел
