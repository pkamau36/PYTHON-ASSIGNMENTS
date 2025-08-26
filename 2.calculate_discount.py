# function named calculate_discount that uses original price(price) and percentage discount(discount_percent) as parameters.

def calculate_discount(price, discount_percent):
    # check if the percentage discount is 20 or more:
    if discount_percent>= 20:
        # calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        # return the final price after discount
        return final_price
    #if percentage is less than 20, return the original price
    else:
        return price
    
# prompt the user for the original price and discount percentage
print("welcome to the Discount Calculator!")
price = float(input(" Please Enter the original price: "))
discount_percent = float(input("Please Enter the discount percentage: "))


# call the function and print the final price
final_price = calculate_discount(price, discount_percent)
 
if discount_percent >= 20:
    print(f"The final price is: {final_price:.2f}")
else:
    print(f"No discount applied. The final price is: {price:.2f}")

    print("Thank you for using the Discount Calculator!")
