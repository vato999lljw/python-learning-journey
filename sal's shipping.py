weight = 8.4
# Ground shipping.
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight >= 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight >= 6 and weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20
print(cost_ground)

cost_ground_premium = 125.00
print("Ground shipping premium", cost_ground_premium)
weight2 = 1.5
# Drone Shipping
if weight2 <= 2:
  cost_drone = weight2 * 4.50
elif weight2 >= 2 and weight2 <= 6:
  cost_drone = weight2 * 9.00
elif weight2 >= 6 and weight2 <= 10:
  cost_drone = weight2 * 12.00
else:
  cost_drone = weight2 * 14.25
print(cost_drone)

