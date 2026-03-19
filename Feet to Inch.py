# 1. Ask the user for the number of feet
# We use float() because feet can have decimals (like 5.5)
feet = float(input("Enter distance in feet: "))

# 2. Do the math
inches = feet * 12

# 3. Print the result
print(f"{feet} feet is equal to {inches} inches.")
