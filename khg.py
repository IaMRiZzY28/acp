
def add_numbers(a, b):
    return a + b
def multiply_numbers(a, b):
    return a * b
def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))  
    sum_result = add_numbers(num1, num2)
    product_result = multiply_numbers(num1, num2)  
    print(f"The sum of {num1} and {num2} is: {sum_result}")
    print(f"The product of {num1} and {num2} is: {product_result}")
if __name__ == "__main__":
    main()
