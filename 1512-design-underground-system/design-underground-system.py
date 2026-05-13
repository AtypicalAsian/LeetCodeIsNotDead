class UndergroundSystem:

    def __init__(self):
        self.checkins = {} # { id -> (station, t) }
        self.route_times = {} # { (start, end) -> (totalTime, count) }

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkinStation, checkinTime = self.checkins[id]
        travelTime = t - checkinTime
        route = (checkinStation, stationName)
        total,count = self.route_times.get(route,(0,0))
        self.route_times[route] = (total + travelTime, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.route_times[(startStation,endStation)]
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)