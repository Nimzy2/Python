my_dict = {"APPLE": 2, "BANANA": 1, "GRAPES": 2, "KIWI" : 3}

# def get_value(my_tupple):
#     return my_tupple[1]


# def get_key(my_tupple):
#     return my_tupple[0]


print(dict(sorted(list(my_dict.items()), key=lambda my_tupple:my_tupple[1] ,reverse= False)))


# print(get_value(("APPLE", 2)))




# my_dict2 = dict( [ ("APPLE", 2), ("BANANA", 1), ("GRAPES", 2) ] )
# print(my_dict2)
# print(len(my_dict2))
# print(type(my_dict2))
