from random import randint


# sp = []
# for i in range(10):
#     sp.append(randint(1,20))
# print(sp)
# print( sp := [randint(1,20) for _ in range(10)] )

sp = [1,23,3,4,5,6,8,9]
# print( [item for item in sp] )
print( [item **2 for item in sp if item % 2] ) # количество элементов уменьшилось
print( [item **2 if item % 2 else 0 for item in sp ] )  # если надо одинаковое кол-во элементов
# возвести в квадрат каждый нечетный элемент иначе вернуть ноль для каждого элемента в списке sp
print( {i : sp[i] for i in range(len(sp))} ) 
print( {sp[i] for i in range(len(sp))} )