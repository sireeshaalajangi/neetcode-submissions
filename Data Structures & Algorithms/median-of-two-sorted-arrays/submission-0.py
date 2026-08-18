class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m =len(nums1);
        n =len(nums2);
        k=m+n;
        arr = [0]*(k);
        arr = nums1+nums2;
        arr.sort()
        if(k%2==0):
            ele = (arr[k//2-1]+arr[k//2])/2;
        else:
            ele = arr[k//2];
        return ele