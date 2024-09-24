# Python-Week-3
This is the task for Python Week 3 Assignment. The following is the summary of the task:

    Summary of the Program
The code demonstrates two methods for calculating the final price of a product after applying a discount based on a given discount percentage. The function and parameters used are:
    
    1. calculate_discount: the function that calculates the final price after applying a discount.
    
    2. price: the parameter that takes the original price
    
    3. discount_percentage: the parameter that takes the discount percentage.

1. Without Lambda Function:

    1. A function named calculate_discount is defined, which takes two parameters: price and discount_percentage.
    
    2. Inside the function, it calculates the final price by subtracting the discount (calculated as a percentage of the original price) from the original price.
    
    3. If the discount percentage is 20% or higher, it returns the discounted price; otherwise, it returns the original price.
    
    4. The user is prompted to input the original price and the discount percentage, and the function is called to display the resulting price.

2. With Lambda Function:

    1. The same discount calculation logic is implemented using a lambda function assigned to the variable calculate_discount.
    
    2. This lambda function takes the same parameters and performs the discount calculation in a single expression.
    
    3. It uses a conditional expression to determine whether to return the discounted price or the original price based on the discount percentage.
    
    4. Similar to the first snippet, the user is prompted for input, and the lambda function is called to print the resulting price.

Note:
In the lambda version, the intermediate variable finalPrice is not used, as lambda functions do not support assignment statements, that is, the assignment operator (=) cannot be used inside the lambda function. Instead, the calculation is directly returned as part of the lambda expression.
Overall, both snippets achieve the same outcome but illustrate different programming approaches in Python.