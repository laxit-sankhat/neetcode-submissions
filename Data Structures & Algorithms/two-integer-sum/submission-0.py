class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        value_to_index = {}

        for current_index, current_num in enumerate(nums):

            complement = target - current_num

            if complement in value_to_index:
                return [value_to_index[complement], current_index]

            value_to_index[current_num] = current_index