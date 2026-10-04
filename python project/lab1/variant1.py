# Запрашиваем название заказа и имя заказчика
name1 = input("Введите название заказа: ")
username= input("Введите имя заказчика: ")

# Первая позиция
pos1 = input("Название первой позиции: ")
num1 = int(input("Количество первой позиции: "))
price1 = float(input("Цена единицы первой позиции: "))

# Вторая позиция
pos2 = input("Название второй позиции: ")
num2 = int(input("Количество второй позиции: "))
price2 = float(input("Цена единицы второй позиции: "))

# Стоимость каждой позиции
cost1 = num1 * price1
cost2 = num2 * price2

# Общие итоги
costall = cost1 + cost2
cost_delivery = float(input("Стоимость доставки: "))
allsum = cost1 + cost2 + cost_delivery
allnum = num1 + num2

# Сдача
vnesena_sum = float(input("Внесённая сумма: "))
sdacha = vnesena_sum - allsum

# Вывод результатов
print("\n" + "="*40)
print(f"Заказ: {name1}")
print(f"Заказчик: {username}")
print("="*40)
print("Название | Количество | Цена | Стоимость")
print("-"*40)
print(f"{pos1} | {num1} | {price1:.2f} | {cost1:.2f}")
print(f"{pos2} | {num2} | {price2:.2f} | {cost2:.2f}")
print("-"*40)
print(f"Сумма товаров без доставки: {costall:.2f}")
print(f"Общая сумма с доставкой: {allsum:.2f}")
print(f"Общее количество единиц: {allnum}")
print(f"Сдача: {sdacha:.2f} руб.")