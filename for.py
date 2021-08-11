numbers = [1,3,5,7,9]
for i, item in enumerate(numbers):
    numbers[i] *= 2
    #numbers[i] = item * 2
print(numbers)

persons = [('Ali', 20), ('Umar', 12), ('Shax', 24)]
for name, age in persons:
    print(f"{name} is {age}")

list1 = [2,4,-5,6,8,-2]
list2 = [2,-6,8,3,5,-2]
pairs = []

for i in list1:
    for k in list2:
        if i + k == 0:
            pairs.append((i,k))
print(pairs)