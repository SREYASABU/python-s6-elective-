def largest(*nums):
    nums1=list(nums)
    nums1.sort(reverse=True)
    return nums1[0]

print(f'largest of 3,4,2,9,22,32: {largest(3,4,2,9,22,32)}')