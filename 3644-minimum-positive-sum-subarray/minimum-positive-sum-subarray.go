
func minimumSumSubarray(nums []int, l int, r int) int {
	var cur_len int = len(nums)
	var prefix_sum []int = make([]int, cur_len+1)
	var res int = 1<<31 - 1
	for i := 0; i < cur_len; i++ {
		prefix_sum[i+1] = prefix_sum[i] + nums[i]
		if i >= l-1 {
			for pre := i - l + 1; pre >= 0 && i-pre+1 <= r; pre-- {
				cur_sum := prefix_sum[i+1] - prefix_sum[pre]
				if cur_sum > 0 {
					res = min(res, cur_sum)
				}
			}
		}
	}
	if res == 1<<31-1 {
		return -1
	}
	return res
}