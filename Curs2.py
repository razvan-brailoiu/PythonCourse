my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

myAscendingList = my_list.copy()
myAscendingList.sort()
print(myAscendingList)

myDescendingList = my_list.copy()
myDescendingList.sort(reverse=True)
print(myDescendingList)

mySlicedList = my_list[3:7:3]+my_list[7:10:2]
print(mySlicedList)

mySecondSlicedList = my_list[0:5:4]+my_list[5:9:3]
print(mySecondSlicedList)

multiplesList = []
for i in my_list:
    if i % 3 == 0:
        multiplesList.append(i)
print(multiplesList)