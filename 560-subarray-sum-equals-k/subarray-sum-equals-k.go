func subarraySum(nums []int, k int) int {
    prefixSumMap := make(map[int]int)
    prefixSumMap[0] = 1

    currSum := 0
    count :=0
    for _, num := range nums {
        currSum += num
        if freq, ok := prefixSumMap[currSum-k]; ok {
            count += freq
        }
        prefixSumMap[currSum]++
    }
    return count
}