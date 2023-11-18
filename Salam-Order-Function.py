from load_data import load_data
from order_checker import order_checker

def order_func():
 print("The menu is here: ")

 all_meals = load_data("data/meals.json")

 meals = all_meals['meals']

 for meal in meals:
   print(meal['name'] + ',', end=' ')

 all_combos = load_data("data/combos.json")

 combos = all_combos['combos']
 total_combos = len(combos)

 for index, combo in enumerate(combos):
   if index == total_combos-1:
     print('and', combo['name'])
   else:
     print(combo['name'] + ',', end=' ')

 print("Please enter the names of your orders here separating them with a ',': ")

 order = input()

 result = order_checker(order)

 return result
