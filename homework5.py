immutable_var = 1, 2, 'rej', True
print(immutable_var)
#immutable_var[1] = 5
# Изменение элементов в кортеже не возможно. это особенность кортежа.
mutable_list = ["her", 4, 46, False]
print(mutable_list)
mutable_list[0] = 'but'
mutable_list[2] = 'dog'
print(mutable_list)