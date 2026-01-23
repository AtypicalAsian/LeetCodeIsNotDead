class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> seen_num = new HashMap<>();
        int diff = 0;
        for (int i=0; i<nums.length; i++){
            diff = target-nums[i];
            if (seen_num.containsKey(diff)) return new int[] {i,seen_num.get(diff)};
            seen_num.put(nums[i],i);
        }
        return new int[]{};
    }
}