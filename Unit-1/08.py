import random

def loop_function(list_length):
    my_list = []
    for x in range(list_length):
        my_list.append(random.randint(0,60))
    return my_list

new_list = loop_function(8)

print("list contains:", new_list)