import pyvisalgo as va

import ch3_2_quick_sort as qs


DATA_FILE = "data/selection.json"

vis = va.visualizer("selection")


def selection(array, rank):
    """array에서 rank번째로 작은 값을 찾는다. rank는 1부터 시작한다."""
    if not 1 <= rank <= len(array):
        raise ValueError("rank는 배열 길이 안의 1 이상인 값이어야 합니다.")

    # 첫 탐색 범위는 배열 전체입니다.
    return selection_range(array, 0, len(array) - 1, rank)


if __name__ == "__main__":
    while va.running():
        data = va.next_data(__file__, data_file=DATA_FILE)
        array = list(data.array)

        vis.setup(data)
        print("선택 전:", array)
        print(f"찾을 순위: {data.n}번째")
        vis.wait()
