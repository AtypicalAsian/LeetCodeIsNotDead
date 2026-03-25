func productExceptSelf(nums []int) []int {
    prefixProd := 1

    // Init 
    n := len(nums)
    res := make([]int, n)
    for i := range n {
        res[i] = 1
    }

    // Calc left prefix arr
    for i,val := range nums[0:n-1] {
        prefixProd *= val
        res[i+1] = prefixProd
    }

    // Calc right suffix arr
    prefixProd = 1
    for i := n-1; i>=1; i-- {
        prefixProd *= nums[i]
        res[i-1] *= prefixProd
    }
    return res

}