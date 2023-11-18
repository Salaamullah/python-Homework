from load_data import load_data

all_meals = load_data("data/meals.json")
all_combos = load_data("data/combos.json")

# Create dictionaries with meal/combo names as keys and prices as values
meals_dict = {meal['name']: meal['price'] for meal in all_meals['meals']}
combos_dict = {combo['name']: combo['price'] for combo in all_combos['combos']}

def price_counter(orders):
 total = 0

 for order in orders:
  total += meals_dict.get(order, 0)
  total += combos_dict.get(order, 0)

 return total
