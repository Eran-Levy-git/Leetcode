def calculate_product_array(nums):
    n = len(nums)
    product_array = [1] * n

    # Calculate the product of all elements to the left of each index
    left_product = 1
    for i in range(n):
        product_array[i] *= left_product
        left_product *= nums[i]

    # Calculate the product of all elements to the right of each index
    right_product = 1
    for i in range(n - 1, -1, -1):
        product_array[i] *= right_product
        right_product *= nums[i]

    return product_array


# Example usage
input_array = [2, 3, 4, 5]
result_array = calculate_product_array(input_array)
print(result_array)  # Output: [60, 40, 30, 24]
