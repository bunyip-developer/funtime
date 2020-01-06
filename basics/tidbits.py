import operator

if __name__ == '__main__':

    a = 3
    b = 4

    # For common operations like multiplication, use the functions from the operator module
    # instead of lambda functions.
    ab = operator.mul(a, b)  # Don't do this... ab = lambda x, y: x * y
