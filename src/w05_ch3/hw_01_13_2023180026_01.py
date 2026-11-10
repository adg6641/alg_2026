"""실습 과제 13: Merge Sort, Quick Sort, Selection을 구현한다."""

import random


RANDOM_SEED = "EX_01"
ARRAY_SIZE = 30


def merge_sort(array):
    """array를 오름차순으로 직접 정렬한다."""

    temp = [0] * len(array)

    def merge_sort_range(left, right):
        # left..right는 left와 right index를 모두 포함하는 정렬 범위이다.
        if left >= right:
            return

        mid = (left + right) // 2

        # 왼쪽은 left..mid, 오른쪽은 mid+1..right이며
        # left, mid, right 모두 정렬 범위에 포함된다.
        merge_sort_range(left, mid)
        merge_sort_range(mid + 1, right)

        merge(left, mid, right)

    def merge(left, mid, right):
        # left..mid와 mid+1..right를 병합한다.
        # left, mid, right는 모두 실제 배열 범위에 포함되는 index이다.
        i = left
        j = mid + 1
        k = left

        while i <= mid and j <= right:
            if array[i] <= array[j]:
                temp[k] = array[i]
                i += 1
            else:
                temp[k] = array[j]
                j += 1
            k += 1

        while i <= mid:
            temp[k] = array[i]
            i += 1
            k += 1

        while j <= right:
            temp[k] = array[j]
            j += 1
            k += 1

        # range의 끝 index는 포함되지 않으므로
        # right까지 복사하기 위해 right + 1을 사용한다.
        for index in range(left, right + 1):
            array[index] = temp[index]

    if len(array) > 1:
        merge_sort_range(0, len(array) - 1)


def partition(array, left, right):
    # partition 범위는 left..right이며
    # left와 right index를 모두 포함한다.
    # 반환값은 pivot의 위치가 최종적으로 확정된 index이다.
    pivot = array[right]
    store = left

    # range(left, right)는 right를 포함하지 않는다.
    # right 위치에는 pivot이 있으므로 left..right-1만 비교한다.
    for index in range(left, right):
        if array[index] <= pivot:
            array[store], array[index] = array[index], array[store]
            store += 1

    array[store], array[right] = array[right], array[store]

    return store


def quick_sort(array):
    """array를 오름차순으로 직접 정렬한다."""

    def quick_sort_range(left, right):
        # left..right는 left와 right index를 모두 포함하는 정렬 범위이다.
        if left >= right:
            return

        pivot_index = partition(array, left, right)

        # pivot은 pivot_index 위치가 확정되었으므로
        # left..pivot_index-1과 pivot_index+1..right를 각각 정렬한다.
        quick_sort_range(left, pivot_index - 1)
        quick_sort_range(pivot_index + 1, right)

    if len(array) > 1:
        quick_sort_range(0, len(array) - 1)


def selection(array, n):
    """array에서 n번째로 작은 값을 반환한다. n은 1부터 시작한다."""

    if not 1 <= n <= len(array):
        raise ValueError("n은 1부터 배열 길이 사이의 값이어야 합니다.")

    left = 0
    right = len(array) - 1

    # n은 1부터 시작하지만 배열 index는 0부터 시작한다.
    target_index = n - 1

    while left <= right:
        # partition 범위는 left..right이며 right도 포함된다.
        # 반환된 pivot_index는 pivot이 최종적으로 확정된 배열 index이다.
        pivot_index = partition(array, left, right)

        if pivot_index == target_index:
            return array[pivot_index]

        if target_index < pivot_index:
            # 다음 탐색 범위는 left..pivot_index-1이며
            # 양 끝 index를 포함한다.
            right = pivot_index - 1
        else:
            # 다음 탐색 범위는 pivot_index+1..right이며
            # 양 끝 index를 포함한다.
            left = pivot_index + 1


def make_random_array(randomizer):
    """1부터 99 사이의 값 ARRAY_SIZE 개를 가진 새 배열을 만든다."""
    return [randomizer.randint(1, 99) for _ in range(ARRAY_SIZE)]


if __name__ == "__main__":
    randomizer = random.Random(RANDOM_SEED)

    # 정렬 두 개는 서로 다른 무작위 배열을 사용한다.
    merge_data = make_random_array(randomizer)
    quick_data = make_random_array(randomizer)

    print("Merge Sort")
    print("정렬 전:", merge_data)
    merge_sort(merge_data)
    print("정렬 후:", merge_data)
    print()

    print("Quick Sort")
    print("정렬 전:", quick_data)
    quick_sort(quick_data)
    print("정렬 후:", quick_data)
    print()

    # Selection은 하나의 30개 배열에서 서로 다른 두 순위를 찾는다.
    selection_data = make_random_array(randomizer)
    first_n = randomizer.randint(10, 24)
    second_n = randomizer.randint(10, 24)

    print("Selection")
    print("배열:", selection_data)
    print(f"{first_n}번째로 작은 값은:", selection(selection_data, first_n))
    print(f"{second_n}번째로 작은 값은:", selection(selection_data, second_n))