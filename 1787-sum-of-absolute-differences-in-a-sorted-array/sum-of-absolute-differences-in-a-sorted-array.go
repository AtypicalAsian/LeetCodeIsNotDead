import "fmt"

func getSumAbsoluteDifferences(nums []int) []int {
    n := len(nums)
    prefixLeft := make([]int, n)
    prefixRight := make([]int, n)
    res := make([]int, n)

    currSum := 0
    // Create left prefix sum array
    for i:=0;i<n;i++{
        prefixLeft[i] = currSum
        currSum += nums[i]
    }

    currSum = 0
    // Create right prefix sum array
    for i:=n-1; i>=0; i-- {
        prefixRight[i] = currSum
        currSum += nums[i]
    }

    val_at_i := 0
    for i:=0; i < n; i++ {
        val_at_i = (nums[i] * i - prefixLeft[i]) + (prefixRight[i] - nums[i] * (len(nums)-i-1))
        res[i] = val_at_i
    }

    return res
}