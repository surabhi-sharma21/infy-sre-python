from statistics import mean, median, mode, stdev, variance

pointers = [4, 5, 10, 2, 3, 5, 4, 3, 2, 5, 1, 0]
print('Mean: {0}'.format(mean(pointers)))
print('Median: {0}'.format(median(pointers)))
print('Mode: {0}'.format(mode(pointers)))

print('Std: {0}'.format(stdev(pointers)))
print('Variance: {0}'.format(variance(pointers)))

