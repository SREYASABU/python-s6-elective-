import statistics
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]

mean = statistics.mean(numbers)
median = statistics.median(numbers)
std_dev = statistics.stdev(numbers)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

