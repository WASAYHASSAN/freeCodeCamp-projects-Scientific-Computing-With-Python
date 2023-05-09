from budget import Category

food_category = Category("Food")
food_category.deposit(1000, "initial deposit")
food_category.withdraw(10.15, "groceries")
food_category.withdraw(15.89, "restaurant and more food")
print(food_category.get_balance())
