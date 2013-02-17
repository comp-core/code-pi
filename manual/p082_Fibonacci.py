# Example from Pi Educational Manual v1.0 P. 82
# Provided under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

first = 0
print(first, end=" ")
second = 1
while (first < 100):
     print(second, end=" ")
     third = first + second
     first = second
     second = third
