class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        res = 0
        arriveTimes = []
        for i in range(len(dist)):
            arriveTimes.append(math.ceil(dist[i]/speed[i]))
        arriveTimes.sort()
        # arriveTimes is a sorted array of all the times ( in minutes ) it takes each monster to reach the city
        # We can remove one monster a minute, therefore remove the monster which will reach the city first
        # The index of arriveTimes represents the number of minutes we have been playing for
        # If the minute the monster arrives at the city is greater than or equal to the number of minutes weve been playing for, we lose
        for arriveTime, minute in enumerate(arriveTimes):
            if arriveTime<minute:
                res+=1
            else:
                break
        return res
        