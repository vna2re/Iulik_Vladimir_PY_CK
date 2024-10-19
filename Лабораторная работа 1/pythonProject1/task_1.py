numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
summ = 0
# TODO заменить значение пропущенного элемента средним арифметическим
for i in range(0,len(numbers)):
    if numbers[i] == None:
        none_number = i
    else:
        summ += numbers[i]
numbers[none_number] = summ / (len(numbers))
print("Измененный список:", numbers)
