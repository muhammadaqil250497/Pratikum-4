list1 = [10,20,30,40,50]
print(list1[2])
print(list1[1:4])
print(list1[4])
print(list1[3])
print()

list1[4] = 6
print(list1[4])
print()

list1[2:3] = [8,7]
print(list1)
print()

list2 = list1[2:4]
print(list2)
print()

list2.append("angka")
print(list2)
print()

list2.append([60, 61, "puluhan"])
print(list2)
print()

list3 = list1 + list2
print(list3)