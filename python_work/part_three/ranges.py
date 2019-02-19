for value in range (1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)


squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
small = min(digits)
big = max(digits)
bigger = sum(digits)

print(small)
print(big)
print(bigger)

squares = [value**3 for value in range(1,11)]
print(squares)
