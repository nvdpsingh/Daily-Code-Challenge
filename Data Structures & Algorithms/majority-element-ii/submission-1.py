class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = Counter(nums)

        return [num for num, count in counts.items() if count > n / 3]