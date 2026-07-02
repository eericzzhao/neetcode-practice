class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty positions
                if val == ".":
                    continue
                
                # Formula to map the (row, col) to a specific 3x3 box index (0 to 8)
                box_idx = (r // 3) * 3 + (c // 3)
                
                # If the number is already in the current row, column, or box, it's invalid
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False
                
                # Otherwise, add it to our tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        return True