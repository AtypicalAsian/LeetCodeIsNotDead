func minSubArrayLen(target int, nums []int) int {
        left := 0
        currSum := 0
        minLen := math.MaxInt
        for right := 0; right < len(nums); right++ {
            currSum += nums[right]
            for currSum >= target {
                minLen = min(minLen, right-left+1)
                currSum -= nums[left]
                left++
            }
        }
        if minLen == math.MaxInt {
            return 0
        }
        return minLen
}