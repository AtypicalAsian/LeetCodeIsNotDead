func minMoves(nums []int) int {
    var target = maxSlice(nums)
    var totalMoves = 0

    for i := 0; i < len(nums); i++ {
        totalMoves = totalMoves + (target - nums[i])
    }
    return totalMoves
}

// Helper function to find the maximum value in a slice
func maxSlice(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    m := nums[0]
    for _, v := range nums {
        if v > m {
            m = v
        }
    }
    return m
}