first_room = input('Первая аудитория:').strip()
second_room = input('Вторая аудитория:').strip()
print("Исходные значения:")
print("first_room =", first_room)
print("second_room =", second_room)
temp = first_room  
first_room = second_room  
second_room = temp  
print("После обмена:")
print("first_room =", first_room)
print("second_room =", second_room)
