list_1 = [1,2,3,4,5,6]
print(f"{list_1}")

list_1.append(7)
print(f"{list_1}")
#[1, 2, 3, 4, 5, 6, 7]

list_1.remove(3)
print(f"{list_1}")
#[1, 2, 4, 5, 6, 7]

list_2 = [1,4,5]

list_1.extend(list_2)
print(f"{list_1}")
#[1, 2, 4, 5, 6, 7, 1, 4, 5]

list_1.insert(3,3)
#index , value
print(f"{list_1}")
#[1, 2, 4, 3, 5, 6, 7, 1, 4, 5]

last = list_1.pop()
print(last)
# it will remove from the list and it will return the last value from the data structure. it also works on multiple ds.

list_1.reverse()
print(list_1);

list_1.sort()
print(list_1)