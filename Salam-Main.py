import json
from order_func import order_func
from order import Order

result = order_func()

if isinstance(result, list):
 order = Order(result)
 print('*'*50)
 print(f"Your order id is: {order.order_id}")
 print(f"Your order was made on: {order.date}")
 print(f"Your order contains: {order.items}")
 print(f"Your order has {order.calories} calories")
 if order.order_accepted:
   print("Your order has been accepted!")
   print(f"Your order costs {order.price} euros")
 else:
   print("Your order has been refused!")
   print(f"Reason: {order.order_refused_reason}")

 order_dict = {
   'order_id': order.order_id,
   'order_accepted': order.order_accepted,
   'order_refused_reason': order.order_refused_reason,
   'date': order.date.strftime("%Y-%m-%d"),
   'items': order.items,
   'calories': order.calories,
   'price': order.price
 }

 try:
   with open('data/all_orders.json', 'r') as json_file:
     data = json.load(json_file)
 except (FileNotFoundError, json.decoder.JSONDecodeError):
   data = []

 data.append(order_dict)

 with open('data/all_orders.json', 'w') as json_file:
   json.dump(data, json_file, indent=2)

else:
 print(result)
