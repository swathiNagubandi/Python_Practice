# Returns the sum of series
def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i

    return sum

#calling method in two ways with main and  without main

# 1 Method
n = 5
print(sumOfSeries(n))

# 2 Method
if __name__=='__main__':
    sum=sumOfSeries(6)
    print(sum)
