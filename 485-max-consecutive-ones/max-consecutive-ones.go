func findMaxConsecutiveOnes(nums []int) int {
    maxCount := 0
    currCount := 0
    for i,_ := range nums {
        if (nums[i] == 1) {
            currCount += 1
        } else {
            currCount = 0
        }
        maxCount = max(currCount,maxCount)
    }
    return maxCount
}