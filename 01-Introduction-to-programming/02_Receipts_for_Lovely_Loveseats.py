# 1. Create a variable called lovely_loveseat_description and assign to it a string.

lovely_loveseat_description = '''
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
'''

# 2. Great, now let’s create a price for the loveseat. Create a variable lovely_loveseat_price and set it equal to 254.00.

lovely_loveseat_price = 254.00

# 3. Let’s extend our inventory with another characteristic piece of furniture! Create a variable called stylish_settee_description and assign to it a description

stylish_settee_description = '''
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
'''
# 4. Create a variable stylish_settee_price and assign it the value of 180.50

stylish_settee_price = 180.50

# 5. Create a new variable called luxurious_lamp_description and assign it a description

luxurious_lamp_description = '''
Luxurious Lamp. Glass and iron. 
36 inches tall. Brown with cream shade.
'''

# 6. Create a variable called luxurious_lamp_price and set it equal to 52.15.

luxurious_lamp_price = 52.15

# 7. Define the variable sales_tax and set it equal to .088. That’s 8.8%.

sales_tax = 0.088

# 8. Our first customer is making their purchase! Let’s keep a running tally of their expenses by defining a variable called customer_one_total.

customer_one_total = 0

# 9. We should also keep a list of the descriptions of things they’re purchasing. Create a variable called customer_one_itemization and set that equal to the empty string ""

customer_one_itemization = ''

# 10. Our customer has decided they are going to purchase our Lovely Loveseat! Add the price to customer_one_total.

customer_one_total += lovely_loveseat_price

# 11. Let’s start keeping track of the items our customer purchased. Add the description of the Lovely Loveseat to customer_one_itemization.

customer_one_itemization += lovely_loveseat_description

# 12. Our customer has also decided to purchase the Luxurious Lamp! Let’s add the price to the customer’s total.

customer_one_total += luxurious_lamp_price

# 13. Add the description of the Luxurious Lamp to our itemization

customer_one_itemization += luxurious_lamp_description

# 14. Create a variable called customer_one_tax and set it equal to customer_one_total times sales_tax.

customer_one_tax = customer_one_total * sales_tax

# 15. Add the sales tax to the customer’s total cost.

customer_one_total += customer_one_tax

# 16. Let’s start printing up their receipt! Begin by printing out the heading for their itemization. Print the phrase "Customer One Items:" 

print('Customer One Items: ')

# 17. Print customer_one_itemization

print(customer_one_itemization)

# 18. Now add a heading for their total cost: Print out "Customer One Total:"

print('Customer One Total: ')

# 19. Now print out their total.
print(customer_one_total)

