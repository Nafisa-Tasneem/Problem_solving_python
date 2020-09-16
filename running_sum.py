
#problem in leetcode
#cumulative sum
def runningSum(self, nums: List[int]) -> List[int]:
    summation = 0
    output = []
    for i in nums:
        summation = summation + int(i)
        output.append(summation)

    return output
