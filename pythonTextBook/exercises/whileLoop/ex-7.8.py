sandwich_orders = ["tuna", "beef", "cheese", "chicken"]
finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"I made your {sandwich_order} sandwich")
    finished_sandwiches.append(sandwich_order)

print(f"Your order is ready: {', '.join(finished_sandwiches)}")