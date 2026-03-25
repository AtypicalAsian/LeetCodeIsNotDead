func productExceptSelf(nums []int) []int {
    prefixProd := 1

    // Init left prefix + right suffix arr
    n := len(nums)
    leftPrefix := make([]int, n)
    rightSuffix := make([]int, n)
    for i := range leftPrefix {
        leftPrefix[i] = 1
        rightSuffix[i] = 1
    }

    // Calc leftPrefix
    for i,val := range nums[0:n-1] {
        prefixProd *= val
        leftPrefix[i+1] = prefixProd
    }
    // return leftPrefix

    // Calc rightSuffix
    prefixProd = 1
    for i := n-1; i>=1; i-- {
        prefixProd *= nums[i]
        rightSuffix[i-1] = prefixProd
    }

    result := make([]int, n)
    for i := range n {
        result[i] = leftPrefix[i] * rightSuffix[i]
    }
    return result

}