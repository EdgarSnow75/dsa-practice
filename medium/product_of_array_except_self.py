# LeetCode 238

# Prefix * Suffix solution
def product_except_self(nums: list[int]) -> list[int]:
    prefix_products = [1]
    suffix_products = [1 for _ in range(len(nums))]
    current_prefix_product = 1
    current_suffix_product = 1
    for i in range(1, len(nums)):
        current_prefix_product *= nums[i - 1]
        prefix_products.append(current_prefix_product)
    for l in range(len(nums) - 2, -1, -1):
        current_suffix_product *= nums[l + 1]
        suffix_products[l] = current_suffix_product
    answer = []
    for k in range(len(nums)):
        product = prefix_products[k] * suffix_products[k]
        answer.append(product)
    return answer


# Divison
def product_except_self_divi(nums: list[int]) -> list[int]:
    total_product = 1
    for i in range(len(nums)):
        if nums[i] == 0:
            return [0 for _ in range(len(nums))]
        total_product *= nums[i]
    answer = []
    for i in range(len(nums)):
        answer.append(int(total_product / nums[i]))
    return answer
