def find_triplets(nums, targets):
    nums.sort()
    triplets=[]
    n = len(nums)
    for i in range(n-2):
        left = i+1
        right =n-1
        while left<right:
            current_sume =nums[i]+nums[left]+nums[right]
            if current_sume==targets:
                triplets.append((nums[i], nums[left], nums[right]))
                left+=1
                right -=1
            elif current_sume<targets:
                left+=1
            else:
                right-=1
    return triplets

results = find_triplets([1,2,3,4,5,6,0,-1,8],9)
print(results)




