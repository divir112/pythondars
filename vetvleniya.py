my_set = set()
print(my_set)
#добавление элемента
my_set.add(1)
my_set.add(2)
print(my_set)
#проверка нахождения элемента во множестве
print(1 in my_set)

set1 = {0,1,2,3,4}
set2 = {1,2,3,4,5}

#проверка является ли множество подмножеством другого множества
print(set1.issubset(set2))
print(set2.issubset(set1))

#проверка является ли множество надмножестовм другого множества
print(set2.issuperset(set1))
print(set1.issuperset(set2))

#проверка являются ли все элементы множетсва разными от другого множества
print(set1.isdisjoint(set2))

#объединение множеств - возвращает новое множество
set3 = set1.union(set2)
print(set3)

#пересечение- возвращает элементы которые присутствую в обоих множествах
set4 = set1.intersection(set2)
print(set4)

#возвращение неприсутвующих элемнетов множества в другом множестве
set5 = set1.difference(set2)
print(set5)
set6 = set1.symmetric_difference(set2)
print(set6)

#update
set1.update(set2)
print(set1)

#удаление элементов из множества
set1.remove(1)
print(set1)

set1.discard(45)
print(set1)#приудалении несуществующего элемента ошибки не возникнет

print(set1.pop())# удаляет случайный элемент и возвращет его
print(set1)

#полная очистка множества
set1.clear()
print(set1)







