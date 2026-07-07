import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first do I have to validate the nums
        #or k
        #ex assume k is at least k>=0
        
        #[1,2,2,3,3,3] k = 2
        #return 2,3 or 3,2
        #[1,1,1,-1] k =1
        #return [1]

        #First thought is to create a hashmap tracking all
        #all of the occurences of all the numbers in nums
        #sort the combinations based on the occruences 
        #return the first k elements

        #common pitfalls would be that it's inefficent to sort again
        #after calcuating the occurences as opposed to having a running list

        #my next thought is a max heap, in combination with a hashmap
        #as we iterate over numerates. Adding the occurences and num to 
        #the top. If it's an older duplicate of a number populated before than
        #skip it

        # max_heap = []
        # occurences = defaultdict(int)
        # for num in nums:
        #     occurences[num] += 1
        #     heapq.heappush_max(max_heap, (occurences[num], num))
        # results= []
        # for i in range(k):
        #     occurence, num = heapq.heappop_max(max_heap)
        #     while occurences[num] != occurence:
        #         occurence, num = heapq.heappop_max(max_heap)

        #     results.append(num)
        # return results

        #better approch still uses heap
        #count frequencies of occurences for the whole list
        #construct a heap to occurences and values to sort the list
        #popping when exceeding the k amount
        count = Counter(nums)
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]

