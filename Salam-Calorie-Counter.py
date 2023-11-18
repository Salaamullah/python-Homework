from load_data import load_data

all_meals = load_data("data/meals.json")
all_combos = load_data("data/combos.json")

def calorie_counter(orders):
  meals = all_meals['meals']
  combos = all_combos['combos']

  total = 0

  for order in orders:
    if 'combo' in order:
      for combo in combos:
        if order == combo['name']:
          total += combo_calories_counter(order)
    else:
      for meal in meals:
        if order == meal['name'] or order == meal['id']:
          total += meal['calories']
  return total

def combo_calories_counter(orders):
  combos = all_combos['combos']

  for combo in combos:
    if orders == combo['name']:
      combo_meal_list = combo['meals']

  total = calorie_counter(combo_meal_list)

  return total