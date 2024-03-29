def solution(n):
    col = [0] * n
    answer = queen(0, n, col)
    return answer


def queen(x, n, col):
    if x == n:
        return 1

    count = 0
    for y in range(n):
        if possible(x, y, col):
            col[x] = y
            count += queen(x + 1, n, col)

    return count


def possible(x, y, col):
    for i in range(x):
        if y == col[i] or abs(y - col[i]) == x - i:
            return False

    return True
