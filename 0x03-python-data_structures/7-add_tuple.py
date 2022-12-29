#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    temp_a = list(tuple_a)
    temp_b = list(tuple_b)
    temp_c = []
    if(len(temp_a) < 2):
        if len(temp_a) == 1:
            temp_a.append(0)
        if len(temp_a) == 0:
            for idx in range(2):
                temp_a.append(0)
    elif(len(temp_a) > 2):
        temp_a = temp_a[0:2]

    if(len(temp_b) < 2):
        if len(temp_b) == 1:
            temp_b.append(0)
        if len(temp_b) == 0:
            for idx in range(2):
                temp_b.append(0)

    elif(len(temp_b) > 2):
        temp_b = temp_b[0:2]

    for idx in range(len(temp_a)):
        temp_c.append(temp_a[idx] + temp_b[idx]) 

    return tuple(temp_c)


tuple_a = (1, 89, 34, 42)
tuple_b = (88, 11, 53, 53)
new_tuple = add_tuple(tuple_a, tuple_b)
print("--------------------------------------------------------------------")
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))