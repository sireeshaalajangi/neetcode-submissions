class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for num in nums:
            if num not in hashmap:
                hashmap[num]=0
            else:
                hashmap[num] += 1
        sorted_items=sorted(hashmap.items(),key=lambda x:x[1], reverse=True)
        res=[]
        for i in range(k):
            res.append(sorted_items[i][0])
        return res