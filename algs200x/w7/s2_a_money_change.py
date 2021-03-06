"""
Money Change

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 7 - final exam - greedy algorithms

Assume that you have an unlimited number of coins with denominations 1, 3, 9, and 27.
What is the minimum number of coins needed to change 100?
"""
DENOMINATIONS = [27, 9, 3, 1]  # safe choice, keeping bigger to smaller order


def solution(total):
    leftover = total
    result = 0

    for coin in DENOMINATIONS:
        counter = leftover // coin
        if counter > 0:
            result += counter
            leftover %= coin

        if leftover == 0:
            break

    return result


if __name__ == '__main__':
    print(solution(100))
