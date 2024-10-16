nums1 = []
m = len(nums1)
nums2 = [1]
n = len(nums2)


def merging(nums1, nums2):
    for i in nums2:
        nums1.append(i)


merging(nums1=nums1, nums2=nums2)
nums1.sort()
print(nums1)
