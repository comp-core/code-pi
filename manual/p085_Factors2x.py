# Example from Pi Educational Manual v1.0 P. 85
# Provided under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License
for number in range(1, 51):
    factors = 0
    print number,
    for divisor in range(1, number+1):
        if number%divisor == 0:
            print divisor,
            factors+=1
    if (factors == 2):
        print "and is a prime number"
    else:
        print
