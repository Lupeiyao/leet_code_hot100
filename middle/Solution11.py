from typing import List


class Solution11:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_size = len(nums)
        left_product, right_product = [1] * num_size, [1] * num_size
        for i in range(1, len(nums)):
            left_product[i] = nums[i - 1] * left_product[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            right_product[i] = nums[i + 1] * right_product[i + 1]
        result = [left_product[i] * right_product[i] for i in range(num_size)]
        return result


print(Solution().productExceptSelf([1,2,3,4]))



