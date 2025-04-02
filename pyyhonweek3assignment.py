
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


while True:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)

    # Output the result
    if final_price == original_price:
        print(f"No discount was applied. The original price is: {original_price:.2f}")
    else:
        print(f"The final price after applying the discount is: {final_price:.2f}")

    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != 'yes':
        break