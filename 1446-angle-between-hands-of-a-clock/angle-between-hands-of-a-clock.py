class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute = minutes * 6
        hourHand = (hour % 12) * 30 + (minutes * 0.5)

        diff = abs(hourHand - minute)

        return min(diff, 360 - diff)