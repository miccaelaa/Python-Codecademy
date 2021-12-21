# weight in lb
weight = 41.5

# Ground shipping(Pounds)
if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

print('Ground Shipping $', cost_ground)

# Premium Ground Shipping
cost_ground_premium = 125.00

print('Ground Shipping Premium $', cost_ground_premium)

# Drone Shipping
if weight <= 2:
  cost_ground_drone = weight * 4.50 
elif weight <= 6:
  cost_ground_drone = weight * 9
elif weight <= 10:
  cost_ground_drone = weight * 12
else:
  cost_ground_drone = weight * 14.25

print('Drone Shipping $', cost_ground_drone)

# Find cheapest shipping
cheapest_shipping = min([cost_ground, cost_ground_premium, cost_ground_drone])

print(cheapest_shipping)

