# Create a function that calculates the final price after applying a discount.
# The function parameters are the original price (price) and the discount percentage (discount_percent).
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.

# Without lambda function
def calculate_discount(price, discount_percentage): #function to be used
    finalPrice = price - price * discount_percentage / 100
    if discount_percentage >= 20: #condition to be checked
        return finalPrice #the price with a discount
    else:
        return price #the original price
# User to enter the price and discount percentage
price = int(input('Enter the original price: '))
discount_percentage = int(input('Enter the discount percentage: '))
print(calculate_discount(price, discount_percentage)) #calling the function


# With lambda function
calculate_discount = lambda price, discount_percentage : price - price * discount_percentage / 100 if discount_percentage >= 20 else price
#User to input the price and discount percentage
price = int(input('Enter the original price: '))
discount_percentage = int(input('Enter the discount percentage: '))
print(calculate_discount(price, discount_percentage)) #calling the function
# finalPrice is not used because you cannot use the assignment operator (=) inside a lambda expression.