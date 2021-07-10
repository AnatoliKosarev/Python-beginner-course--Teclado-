sandwich_orders = ["tuna", "beef", "pastrami", "cheese", "pastrami", "pastrami", "chicken"]
finished_sandwiches = []

print("Pastrami not available")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"Your {order} sandwich is ready")
    finished_sandwiches.append(order)

print(f"Here's the list of complete orders: {', '.join(finished_sandwiches)}")