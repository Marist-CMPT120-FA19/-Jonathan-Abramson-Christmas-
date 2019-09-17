#A Program to make you jolly
#Designed by Jon

n = int(input("Describe your tree size:\t"))
for i in range(n):
    for x in range(n-i):
        print(' ', end='')
    print('\b', end='')
    for k in range(i+n-x):
        print('#', end='')
    print('')
print((n-1)*" "+"#")