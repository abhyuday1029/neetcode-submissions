class Solution:
    def topKFrequent(self, nums, k):
        hashmap = {}

        count_lst = [[] for i in range(len(nums) + 1)]
        ret_lst = []

        # Count frequencies
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        # Fill buckets
        for key, val in hashmap.items():
            count_lst[val].append(key)

        # Collect top k
        for i in range(len(count_lst)-1, 0, -1):
            for j in count_lst[i]:
                ret_lst.append(j)
                if len(ret_lst) == k:
                    return ret_lst

        return []