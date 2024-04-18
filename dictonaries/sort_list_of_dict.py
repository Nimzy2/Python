# create a list of dictonaries
grocery_list = [
    {"name": "Kiwi", "quantity": 2, "price": 50},
    {"name": "Apple", "quantity": 1, "price": 30},
    {"name": "Banana", "quantity": 2, "price": 10},
    {"name": "Grapes", "quantity": 4, "price": 100},
    {"name": "Orange", "quantity": 2, "price": 20}
]
# sorted_list = sorted(grocery_list, key=lambda grocery: (grocery['name']))

# for item in sorted_list:
#     print(item)

def get_price(dictonary):
    return dictonary["price"]
def get_name(dictonary):
    return dictonary["name"]
def get_quantity(dictonary):
    return dictonary["quantity"]
grocery_list_sorted = sorted(grocery_list, key=get_quantity, reverse= False)
print(grocery_list_sorted[0]["name"])

for grocery in grocery_list_sorted:
    print(grocery["name"], grocery["quantity"],grocery["price"] )
 