class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height *(i - index))
                start = index

            stack.append((start, h)) 

        n = len(heights)

        for index, height in stack:
            max_area = max(max_area, height * (n-index))

        return max_area
