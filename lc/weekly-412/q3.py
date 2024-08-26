from sortedcontainers import SortedList
import math


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        order = SortedList()
        for i, element in enumerate(nums):
            order.add((element, i))

        print(order)


        index_to_num_times = defaultdict(int)

        for i in range(1, len(order)):
            prev_val, prev_index = order[i-1]
            curr_val, curr_index = order[i]
            index_to_num_times[prev_index] = math.ceil(math.log(curr_val/prev_val, multiplier))


        print(index_to_num_times)


        ops = 0
        for index, num_times in index_to_num_times.items():
            ops += num_times
            if ops > k:
                break
            nums[index] = nums[index] * pow(multiplier, num_times, 10**9 + 7)

        print(nums)

        remaining = k - ops

        print(remaining)

        if remaining > 0:

            all_hit = remaining // len(nums)

            for i, element in enumerate(nums):
                nums[i] = element * pow(multiplier, num_times, 10**9 + 7)


            remaining_2 = remaining % len(nums)

            for i in range(remaining_2):
                _, index = order[i]
                nums[index] = nums[index] * multiplier

        modded = [e % (10**9 + 7) for e in nums]

        return modded

        