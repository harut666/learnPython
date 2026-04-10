def numGiven(num):
    """
    Выводит в консоль первую цифру данного целого числа.
    """
    if not isinstance(num, int):
        return "Please enter an integer"

    # Преобразуем число в строку
    s_num = str(abs(num)) # Используем abs(), чтобы корректно обработать отрицательные числа (например, -123 -> '1')

    # Первая цифра — это первый символ строки
    first_digit_str = s_num[0]

    # Возвращаем эту цифру как строку (или можно преобразовать обратно в int, если нужно)
    return first_digit_str

# --- Тестирование функции ---

# Пример 1: Положительное число
number1 = 54321
result1 = numGiven(number1)
print(f"Число: {number1}, Первая цифра: {result1}")

# Пример 2: Однозначное число
number2 = 7
result2 = numGiven(number2)
print(f"Число: {number2}, Первая цифра: {result2}")

# Пример 3: Отрицательное число (важно учесть знак!)
number3 = -98765
result3 = numGiven(number3)
print(f"Число: {number3}, Первая цифра: {result3}")

# Пример 4: Ноль
number4 = 0
result4 = numGiven(number4)
print(f"Число: {number4}, Первая цифра: {result4}")

# Пример 5: Некорректный ввод
invalid_input = "abc"
result5 = numGiven(invalid_input)
print(f"Ввод: '{invalid_input}', Результат: {result5}")
