
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Step 2: Ask the user for input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Step 3: Call the function and store the result
final_price = calculate_discount(original_price, discount)

# Step 4: Show the result
if discount >= 20:
    print(f"Discount applied! You only need to pay: R{final_price:.2f}")
else:
    print(f"No discount applied. You need to pay: R{original_price:.2f}")
