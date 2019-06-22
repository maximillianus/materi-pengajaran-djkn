# Function is useful to collect a group of codes

# Function with parameters
def pythagoras(a, b):
    # Use a & b to find c
    c = (a * a + b * b) ** 0.5
    return c

a = 3
b = 4
c = pythagoras(a,b)
print('Value of c when a is %d and b is %d :', (a, b, c))