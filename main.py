mass = range(100)
squares = [x**3 for x in mass if x % 3 == 0 and x % 4 == 0]
print(squares)
