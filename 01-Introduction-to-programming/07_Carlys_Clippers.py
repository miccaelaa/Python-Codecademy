hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# 1. Find the average price of a cut.

total_price = 0

for price in prices:
  total_price += price

average_price = total_price / len(prices)

print('Average Haircut Price:', average_price)

# 2. Cut all the prices by 5 dollars.

new_prices = [price - 5 for price in prices]
print(new_prices)

# 3. Find the revenue

total_revenue = 0

for i in range(len(hairstyles)):
  # price * number of people who got a haircut
  total_revenue += prices[i] * last_week[i]

print('Total Revenue:', total_revenue)

# 4. Find the average daily revenue

average_daily_revenue = total_revenue / 7

# 5. Create a list with the hairstyles under $30.

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30)
