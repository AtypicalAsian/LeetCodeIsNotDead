func getMinDistance(nums []int, target int, start int) int {
	i := 0
	for ; start+i < len(nums) || start-i >= 0; i++ {
		if (start+i < len(nums) && nums[start+i] == target) || (start-i >= 0 && nums[start-i] == target) {
			break
		}
	}
	return i
}