import math

# Method 1 : Brute force using 2 forloops to find every single combination of the area
def max_Area(height : list[int]):
    max_area = -math.inf
    for l in range(len(height)):
        for r in range(l+1,len(height)):
            local_area = 0
            if height[r] < height[l]:
                local_area = height[r] * (r-l)
            else:
                local_area = height[l] * (r-l)
            if local_area > max_area:
                max_area = local_area
            # print(f"[i,j] = [{i},{j}], max_area = {max_area}, local_area = {local_area}")
            
    return max_area

# Method 2 : Use 2 ptrs left and right, find the "area = shorter line between l and r * distance between l and r", move the ptrs for the min height (ex: left ptr up if its height < right height (vice versa))
def max_Area_2(height : list[int]):
    max_area = -math.inf
    left, right = 0, len(height)-1
    
    while left < right:
        area = (right-left) * min(height[left],height[right])
        if area > max_area:
            max_area = area
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
        print(f"area = {area}, left = {left}, right = {right}")
        
    return max_area

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    height_2 = [1,1]
    height_3 = [2,3,4,5,18,17,6]
    print(f"Max_Area is : {max_Area_2(height_3)}")