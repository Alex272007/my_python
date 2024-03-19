'''
Задача №41. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
'''
list_3 = [15, 6, 3, 12, 9, 0, 2, 20]
# print(len(list_4 := [list_3[i] for i in range(len(list_3)) if list_3[i-1] 
# < list_3[i] and list_3[(i+1) % len(list_3)] < list_3[i]]))

def find_local_max(i):
    return list_3[i-1] < list_3[i] and list_3[(i+1) % len(list_3)] < list_3[i]

list_3 = [15, 6, 3, 12, 9, 0, 2, 20]

print(len([list_3[i] for i in range(len(list_3)) if find_local_max(i)]))