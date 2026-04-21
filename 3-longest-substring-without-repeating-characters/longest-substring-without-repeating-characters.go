func lengthOfLongestSubstring(s string) int {
    maxLen := 0
    left := 0
    charFreqMap := make(map[byte]int)
    for i := range(len(s)){
        value,ok := charFreqMap[s[i]]
        if (ok) {
            //prevent left pointer from going backwards
            left = max(left,value+1)
        }
        charFreqMap[s[i]] = i
        maxLen = max(maxLen, i - left + 1)
    }
    return maxLen

}