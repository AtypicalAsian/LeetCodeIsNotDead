func minOperations(nums []int) int {
	n := len(nums)
	
	shift := 0
	for i, v := range nums {
		if v == 0 {
			shift = i
			break
		}
	}

	ring := func(k int) int {
		return nums[(shift+k)%n]
	}

	isForward := true
	for k := 0; k < n; k++ {
		if ring(k) != k {
			isForward = false
			break
		}
	}
	if isForward {
		return min(shift, n-shift+2)
	}

	isReverse := true
	for k := 0; k < n; k++ {
		if ring(k) != (n-k)%n {
			isReverse = false
			break
		}
	}
	if isReverse {
		return min(shift+2, n-shift)
	}

	return -1
}
