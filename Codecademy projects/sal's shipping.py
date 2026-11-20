
print("Welcome to Sal's Shipping Calculator!")

weight = float(input("Enter your package weight in pounds: "))

# Ground Shipping
if weight <= 2:
    cost_ground = weight * 1.50 + 20
elif weight <= 6:
    cost_ground = weight * 3.00 + 20
elif weight <= 10:
    cost_ground = weight * 4.00 + 20
else:
    cost_ground = weight * 4.75 + 20

# Premium Ground Shipping
cost_ground_premium = 125.00

# Drone Shipping
if weight <= 2:
    cost_drone = weight * 4.50
elif weight <= 6:
    cost_drone = weight * 9.00
elif weight <= 10:
    cost_drone = weight * 12.00
else:
    cost_drone = weight * 14.25

print("\n--- Shipping Prices ---")
print("Ground Shipping: $", round(cost_ground, 2))
print("Premium Ground Shipping: $", round(cost_ground_premium, 2))
print("Drone Shipping: $", round(cost_drone, 2))

# Find the cheapest shipping method
cheapest_price = min(cost_ground, cost_ground_premium, cost_drone)

if cheapest_price == cost_ground:
    print("Cheapest option: Ground Shipping")
elif cheapest_price == cost_ground_premium:
    print("Cheapest option: Premium Ground Shipping")
else:
    print("Cheapest option: Drone Shipping")
