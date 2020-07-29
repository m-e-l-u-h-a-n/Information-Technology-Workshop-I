def harmonic_sum(n):
    if n<2:
        return 1
    return 1/n+harmonic_sum(n-1)
x=int(input('enter a number greater than two: '))
print(harmonic_sum(x-1))