// finding two numbers that add up to a given number

def check(n):
    for i in range(1, n):
        for j in range(i, n):
            if i + j == n:
                print(i, j)
                return True
    return False