# numbers = [1, 2, 3, 4]
# numbers = []
# for i in range(1, 101):
#     numbers.append(i)
# print(numbers)   

# numbers = [i for i in range (1, 101)]
# print(numbers)

# numbers = [i for i in range (1, 101) if i % 3 != 0]
# print(numbers)

# cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
# for x in cells:
#     print('Element:', x)


cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    for y in x:
        print ('Element:', y)