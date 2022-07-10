# 152
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        out = float("-inf")
        i = 0
        acc = nums[i]
        while i < len(nums):
            if nums[i] < 0:
                # acc is the max if cut off at i
                # if continued, it would be acc*nums[i]*...

                # restmax = self.maxProduct(nums[i+1:])
                # out = max(restmax*nums[i]*acc, acc, out)

                # let rest be the subarray nums[i+1:]
                restmax = self.maxProduct(nums[i+1:])
                # case 1: restmax is positive, then max subarray must have an even number of negatives, meaning we must cut nums[i] and compare out with restmax and return the greatest
                # case 2: restmax is negative, the max subarray is an array with only one negative number, meaning we include nums[i] and continue accumulating
                # case 3: restmax is 0, the max subarray contains only negatives and zeroes:
                # the rest subarray can start with 0, meaning we compare out with nums[i+1] (which is 0), update out, and reset acc
                # the rest subarray can start with a negative number, meaning we accumulate like in case 2
                if restmax > 0:
                    return max(out, restmax)
                elif restmax < 0:
                    acc *= nums[i]
                else:
                    out = max(out, 0)
            elif nums[i] == 0:
                out = max(out, acc)
                acc = nums[i+1]
            else:
                acc *= nums[i]
            i += 1

        return out

    def maxProduct(self, nums: List[int]) -> int:
        out = nums[0]
        acc = nums[0]
        i = 1
        while i < len(nums) - 1:
            if nums[i] > 0:
                acc *= nums[i]
            elif nums[i] == 0:
                out = max(out, acc)
                acc = nums[i+1]
            else:  # nums[i] < 0
                if i == len(nums) - 1:
                    # if nums[i] is the last number there is no point in accumulating it since it's negative
                    return max(out, acc, nums[i])

                restmax = self.maxProduct(nums[i+1:])
                if restmax >= 0:
                    return max(out, acc, restmax)
                # if restmax is negative, nums[i+1:] must only contain one negative number
                else:
                    return max(out, acc*nums[i]*restmax)

            i += 1

        return out
