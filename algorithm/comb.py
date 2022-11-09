# comb sort

# GAPが1になるまでやり、Swap=Falseになるようにする。

from typing import List


def comb_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers
    swapped = True

    while gap != 1 or swapped:  # swappedがTrueの間はやり続ける。gapが1かつ、swappedがFalseになるまで実行。
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1

        swapped = False
    for i in range(0, len_numbers - gap):
        if numbers[i] > numbers[i + gap]:
            numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
            swapped = True  # もしまだ入れ替えていたらswappedをTrueに変える。

    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    print(comb_sort(nums))


