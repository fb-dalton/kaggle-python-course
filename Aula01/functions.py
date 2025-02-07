#definition of function parameters

# *args and **kwargs are the elements of the function. 
# *args is a tuple and **kwargs is a dictionary
# shopping_list is a dictionary and things_to_buy is the keyword argument.
# so, calling add_items(january_groceries, apple=2, banana=3, orange=4)
# generates a january_groceries dictionary with apple=2, banana=3 
# and orange=4 as items;
# function naming uses lowercase and underscores, as indicated in PEP8
# it is a best practice to start the function with a verb.
shoping_list = {
    "Bread": 1,
    "Milk": 3,
    "Chocolate": 1,
    "Butter": 2,
    "Coffee": 2,
}

def add_items(shopping_list, **things_to_buy):
    for item_name, quantity in things_to_buy.items():
        shopping_list[item_name] = quantity
    
    return shopping_list

def show_list(shopping_list):
    for item_name, quantity in shopping_list.items():
        print(f"{quantity}x {item_name}")