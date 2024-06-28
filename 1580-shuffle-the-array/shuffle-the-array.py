class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        myList = []
        for i in range(0,n):
            myList.append(nums[i])
            myList.append(nums[i + n])

        return myList

        