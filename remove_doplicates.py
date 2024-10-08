class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.final_list = []
        self.k = 0
        for i in nums:
            if i not in self.final_list:
                self.final_list.append(i)
                self.k += 1
                
        return f'{self.k}, nums = {self.final_list}'

print(Solution(rotate([1,1,2,3,3,3,3,4,5,6,7])))
