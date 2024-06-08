#PRAGYA MISHRA 0801IT221158
my_dict = {'A1': [1, 2, 3], 'A2': [5, 6, 7], 'A3': [9, 10, 11]}
print("Key", "Value_1", "Value_2", "Value_3")
for key, values in my_dict.items():
    print(key, end='     ')
    for value in values:
        print(value, end='      ')
    print()
