import numpy as np


class PercentileRank:
    def __init__(self, valueArray):
        self.valueArray = np.array(valueArray)
        self.valueArrayLength = len(valueArray)

    def getScore(self, value):
        try:
            score = sum(self.valueArray < value) / float(self.valueArrayLength) * 100
        except (TypeError, KeyError, ZeroDivisionError):
            score = 0.0
        return score

