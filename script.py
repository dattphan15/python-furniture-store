lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

lovely_loveseat_price = 254.00

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price = 52.15

sales_tax = 0.088

customer_one_total = 0

customer_one_itemization = ""

# Customer 1 purchases Lovely Loveseat
customer_one_total += lovely_loveseat_price

# Add Loveseat description to Customer 1 items
customer_one_itemization += lovely_loveseat_description

# Customer 1 purchases Luxurious Lamp
customer_one_total += luxurious_lamp_price

# Add Luxurious Lamp description to Customer 1 items
customer_one_itemization += luxurious_lamp_description

# Calculate sales tax for Customer 1
customer_one_tax = customer_one_total * sales_tax

# Add sales tax to Customer 1's total
customer_one_total += customer_one_tax

# Print Heading for Customer 1 items
print("Customer One Items:")

# Print Customer 1 items
print(customer_one_itemization)

# Print total cost for Customer 1
print("""
Customer One Total:
{}
""".format(customer_one_total))