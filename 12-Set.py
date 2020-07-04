# Sets and Lists

# set'ы это множества
my_set = {1, 2, 3}

print(my_set)
print(type(my_set))
print(len(my_set))

my_set.add(4)

print(my_set)

# отличие set'ов от list'ов
my_list = [1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5]
s = set(my_list)

print(s)
