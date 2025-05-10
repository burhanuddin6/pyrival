# https://leetcode.com/problems/trapping-rain-water/
# beats 50%
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        sum_sol = 0
        left = 0
        right = len(height) - 1
        leftmax = left
        rightmax = right
        t = []
        while left < right:
            if height[left] <= height[right]:
                #process left
                if height[left] > height[leftmax]:
                    t = [(height[leftmax] - height[j]) if ( (height[leftmax] - height[j]) > 0 ) else 0 for j in range(leftmax, left)]
                    sum_sol += sum(t)
                    leftmax = left
                left += 1
            else:
                if height[right] > height[rightmax]:
                    t = [(height[rightmax] - height[j]) if ( (height[rightmax] - height[j]) > 0 ) else 0 for j in range(right, rightmax)]
                    sum_sol += sum(t)
                    rightmax = right

                right -= 1  

        if height[right] > height[rightmax]:
            t = [(height[rightmax] - height[j]) if ( (height[rightmax] - height[j]) > 0 ) else 0 for j in range(right, rightmax)]
            sum_sol += sum(t)
            rightmax = right
        if height[left] > height[leftmax]:
            t = [(height[leftmax] - height[j]) if ( (height[leftmax] - height[j]) > 0 ) else 0 for j in range(leftmax, left)]
            sum_sol += sum(t)
            leftmax = left
        
        if height[leftmax] > height[rightmax]:
            t = [(height[rightmax] - height[j]) if ( (height[rightmax] - height[j]) > 0 ) else 0 for j in range(leftmax, rightmax)]
        else:
            t = [(height[leftmax] - height[j]) if ( (height[leftmax] - height[j]) > 0 ) else 0 for j in range(leftmax, rightmax)]     
        sum_sol += sum(t)

        return sum_sol
        