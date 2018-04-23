"""The statistics module calculates basic statistical
properties (the mean, median, variance, etc.) of numeric data:"""
import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print("data", data)
print("statistics.mean(data)", statistics.mean(data))

print("statistics.median(data)", statistics.median(data))

print("statistics.variance(data)", statistics.variance(data))
