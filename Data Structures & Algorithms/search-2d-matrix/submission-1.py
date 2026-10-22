class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found = False
        top, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0])-1
        m = len(matrix)       
        n = len(matrix[0])-1
        while top <= down:
            midr = (top + down) // 2
            if matrix[midr][0] == target:
                found = True
                return found

            #within this row
            elif matrix[midr][0] < target and matrix[midr][n]>=target:
                while left<=right:
                    midc = (left + right) // 2
                    if matrix[midr][midc] == target:
                        found = True
                        return found
                    elif matrix[midr][midc] >= target:
                        right = midc - 1
                    else:
                        left = midc + 1
                break
                

            elif matrix[midr][0] < target and matrix[midr][n]<target:
                top = midr + 1
            
            elif matrix[midr][0] >= target:
                down = midr - 1
        
        return False

            



            

            

