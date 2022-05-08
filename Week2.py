list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("Ascending: ",sorted(list))
print("Descending: ", sorted(list, reverse=True))
# this will not modify the initial list
print("Only evens: ",list[1:4:2] + list[6::3])
print("Only odds: ",list[:5:2] + list[5::3])

only_multiples_of_three = [x for x in list if x % 3 == 0]
print(only_multiples_of_three)