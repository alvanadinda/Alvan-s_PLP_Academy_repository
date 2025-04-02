
def calculate_discount(price, discount_percent):
    """Calculate final price after applying discount if 20% or higher."""
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price

# Prompt user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and display the final price
final_price = calculate_discount(price, discount_percent)

print(f"Final price after applying discount: {final_price:.2f}")