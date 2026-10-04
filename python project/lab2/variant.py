total_volume = int(input("Общий объём: "))
capacity = int(input("Вместимость одной единицы: "))

full_units = total_volume // capacity
remainder = total_volume % capacity
units_needed = (total_volume + capacity - 1) // capacity

print(f"Полностью заполненных единиц: {full_units}")
print(f"Остаток: {remainder}")
print(f"Всего единиц нужно: {units_needed}")