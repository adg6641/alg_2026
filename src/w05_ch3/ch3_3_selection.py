import pyvisalgo as va


DATA_FILE = "data/selection.json"

vis = va.visualizer("selection")


if __name__ == "__main__":
    while va.running():
        data = va.next_data(__file__, data_file=DATA_FILE)
        array = list(data.array)

        vis.setup(data)
        print("선택 전:", array)
        print(f"찾을 순위: {data.n}번째")
        vis.wait()
