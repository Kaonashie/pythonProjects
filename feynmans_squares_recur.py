def count_squares(n):
    if n == 1:
        return 1
    else: 
        return (n * n) + count_squares(n - 1)


def count_squares1a(n, acc=1):
    while True:
        if n == 1:
            return 1 * acc
        return count_squares1a(n - 1, (n * n) + acc)
        break

def count_squares_final(n, acc=1):
    while n != 1:
        (n, acc) = (n - 1, (n * n) + acc)
    return acc

print(count_squares_final(100002))

