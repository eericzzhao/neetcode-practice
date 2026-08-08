class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # rows is calculated by the number of sub-lists, columns is calculated by the number of values inside each sub-list
        rows, cols = len(matrix), len(matrix[0])
        # t, b = how we calculate our middle as we iterate throughout the rows
        top, bottom = 0, rows - 1

        # we iterate through top to bottom 
        while top <= bottom:
            # middle ropw
            row = (top + bottom) // 2

            # our target value is bigger than the last value of the middle row 
            if target > matrix[row][-1]:
                # increment on the middle row 
                top = row + 1
            # our target value is smaller than the first value in the middle row
            elif target < matrix[row][0]:
                bottom = row - 1
            # it matches
            else:
                # we're in the correct row
                break

        if not (top <= bottom):
            return False
        
        # rerrun the binary search
        row = (top + bottom) // 2 # we need to rerun it to get to right row
        # setup the left and right pointers
        l, r = 0, cols - 1
        while l <= r:
            # set up the middle pointer
            m = (l + r) // 2
            # middle value in the correc t row
            # middle value is smaller than target
            if target > matrix[row][m]:
                l = m + 1
            # middle value is bigger than the target
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
                

