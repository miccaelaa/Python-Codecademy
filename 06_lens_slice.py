# pizza's flavours

toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]

# 1. Your boss wants you to do some research on $2 slices. Count the number of occurrences of 2 in the prices.

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# 2. Find the length of the toppings list

num_pizzas = len(toppings)

# 3. Print the string We sell <num_pizzas> different kinds of pizza!

print(f'We sell {num_pizzas} different kinds of pizza!')

# 4. Create a two-dimensional list of toppings and prices. 

pizza_and_prices = [[2, 'pepperoni'],
                    [6, 'pineapple'],
                    [1, 'cheese'],
                    [3, 'sausage'],
                    [2, 'olives'],
                    [7, 'anchovies'],
                    [2, 'mushrooms']]
print(pizza_and_prices)

# 5. Sort pizza_and_prices so that the pizzas are in the order of increasing price 

pizza_and_prices.sort()

# 6. Store the cheapest and priciest pizzas in two variables

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

# 7. Remove anchovies from the list

pizza_and_prices.pop()
print(pizza_and_prices)

# 8. Since there is no longer an 'anchovies' pizza, you want to add a new topping called 'peppers'

pizza_and_prices.insert(4, [2.5, 'peppers'])
print(pizza_and_prices)

# 9. Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest.

three_cheapest = pizza_and_prices[:3]
print(three_cheapest)

                  
