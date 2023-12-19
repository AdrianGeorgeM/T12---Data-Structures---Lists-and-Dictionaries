# Step 1: Create a list of menu items
menu = ["Coffee", "Tea", "Cake", "Marijuana Brownie"]

# Step 2: Create dictionaries for stock and prices
stock = {"Coffee": 30, "Tea": 20, "Cake": 15, "Marijuana Brownie": 10}
price = {"Coffee": 2.5, "Tea": 2.0, "Cake": 3.0, "Marijuana Brownie": 5.0}

# Step 3: Calculate the total stock worth
total_stock_worth = 0
for item in menu:
    item_value = (stock[item] * price[item])
    total_stock_worth += item_value

# Step 4: Print the total stock worth
print("Total stock worth in my cafe:", total_stock_worth)
