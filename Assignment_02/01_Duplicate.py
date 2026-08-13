def containsDuplicate(nums):
   
    nums.sort()
    
    
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True  
            
    return False  

nums1 = [1, 2, 3, 1]
print("Array 1:", nums1)
print("Contains Duplicate?:", containsDuplicate(nums1))

nums2 = [1, 2, 3, 4]
print("Array 2:", nums2)
print("Contains Duplicate?:", containsDuplicate(nums2))