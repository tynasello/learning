from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.valToFreq = defaultdict(int)
        self.freqToVals = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.valToFreq[val] += 1
        freq = self.valToFreq[val]
        self.maxFreq = max(self.maxFreq, freq)
        self.freqToVals[freq].append(val)

    def pop(self) -> int:
        if len(self.freqToVals) == 0:
            return -1

        highestVal = self.freqToVals[self.maxFreq].pop()
        if len(self.freqToVals[self.maxFreq]) == 0:
            self.freqToVals.pop(self.maxFreq)
            self.maxFreq -= 1

        self.valToFreq[highestVal] -= 1

        return highestVal
