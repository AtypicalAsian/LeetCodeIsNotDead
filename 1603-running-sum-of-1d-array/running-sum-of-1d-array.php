class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function runningSum($nums) {
        $currSum = 0;
        $runningSumArr = [];
        for ($i = 0; $i < count($nums); $i++) {
            $currSum += $nums[$i];
            $runningSumArr[] = $currSum;
        }
        return $runningSumArr;
    }
}