# 정렬 구현 단계 실행 기록

- 작업 브랜치: `assignment/sort-follow-1`
- 기준: 로컬 a01의 강의 이력 `4c7ccb2` 다음부터 `f0324d3`까지 146개 커밋.
- 적용 방식: 별도 worktree에서 `git cherry-pick --ff`로 한 커밋씩 적용. 원본 커밋 ID와 순서를 보존했다.
- Bubble Sort에는 별도의 시작 제목 커밋이 없어 용어 및 공통 데이터 준비 커밋부터 포함했다.
- 첫 2개 준비 커밋에는 실행할 정렬 파일이 없다. 이후 각 커밋에서 변경된 정렬 예제 또는 직전의 실행 가능한 정렬 예제를 실행했다.
- 제목만 추가된 커밋에서는 아직 새 알고리즘 파일이 없어 직전 예제를 실행했다.
- 실행 보조 도구는 원본 소스를 runpy로 실행했다. 실제 pygame 시각화 클래스를 사용하되 최고 속도, 화면 갱신 제한, 첫 데이터 실행 후 자동 종료를 적용했다. 정렬 로직은 변경하지 않았다.
- 성능 전용 커밋도 적용했으며 대용량 성능 측정은 생략했다. 성능 전용 파일의 개선은 소스에서 확인했다.
- 결과가 미완성이어도 해당 단계의 정상적인 상태로 기록했다. `finish()` 표시 문구만으로 정렬 성공을 판단하지 않았다.
- 각 최종 시각화 예제의 첫 데이터는 Python의 sorted 결과와 일치했다. 마지막 e~o 비시각화 예제는 원본의 입력 범위 및 정렬 결과 검증을 통과했다.
- 캡처는 실제 pygame 창을 핵심 동작에서 일시정지한 후 Windows 캡처 도구로 촬영했다.
- 전체 stdout 및 종료 코드는 `sort_follow_1_runs.jsonl`에 기록했다.

| 순서 | 커밋 | 내용 | 실행 결과 |
|---:|---|---|---|
| 1 | `4c40633` | 정렬: 3주차 핵심 용어 정리 추가 | 실행 파일 없음 (준비 단계) |
| 2 | `ca113ed` | 정렬: 기본 정렬 알고리즘 공통 데이터 추가 | 실행 파일 없음 (준비 단계) |
| 3 | `051348e` | 버블정렬: 실행 구조와 시각화 연결 추가 | ch6_1_bubble_sort.py: 중간 구현: 미완성 |
| 4 | `c07e19d` | 버블정렬: 인접 원소 비교 구현 | ch6_1_bubble_sort.py: 중간 구현: 미완성 |
| 5 | `138cd26` | 버블정렬: 조건에 따른 원소 교환 구현 | ch6_1_bubble_sort.py: 정렬 일치 |
| 6 | `b5e9fc8` | 버블정렬: 정렬 완료 구간 표시 추가 | ch6_1_bubble_sort.py: 정렬 일치 |
| 7 | `9a46b37` | 버블정렬: 세로 배치 시각화로 전환 | ch6_1_bubble_sort.py: 정렬 일치 |
| 8 | `7407dd0` | 버블정렬: 세로 배치 예제 파일 복사 | ch6_1_bubble_sort_vertical.py: 정렬 일치 |
| 9 | `fa364a6` | 버블정렬: 가로 예제를 복구하고 세로 예제 변수명 수정 | ch6_1_bubble_sort.py: 정렬 일치<br>ch6_1_bubble_sort_vertical.py: 정렬 일치 |
| 10 | `ec76e74` | 버블정렬: 개선 버전 예제 파일 복사 | ch6_1_bubble_sort_improved.py: 정렬 일치 |
| 11 | `3ef1e48` | 버블정렬: 마지막 교환 위치로 비교 범위 줄이기 | ch6_1_bubble_sort_improved.py: 정렬 일치 |
| 12 | `eef8432` | 정렬: 공통 데이터 순서 조정 | ch6_1_bubble_sort_improved.py: 정렬 일치 |
| 13 | `f25aa1b` | 정렬: 공통 데이터 생성 모듈 추가 | ch6_1_bubble_sort_improved.py: 정렬 일치 |
| 14 | `ebbe993` | 정렬: 성능 측정 모듈 추가 | ch6_1_bubble_sort_improved.py: 정렬 일치 |
| 15 | `47b80a8` | 버블정렬: 성능 측정 예제 파일 복사 | ch6_1_bubble_sort_improved.py: 정렬 일치 |
| 16 | `83a1475` | 버블정렬: 성능 측정 예제에서 시각화 제거 | ch6_1_bubble_sort_improved.py: 정렬 일치 |
| 17 | `f4778fd` | 버블정렬: 성능 측정 모듈로 100개 실행 | ch6_1_bubble_sort_improved.py: 정렬 일치 |
| 18 | `5f4e7e1` | 정렬: 데이터 생성 모듈 실행 코드 추가 | ch6_1_bubble_sort_improved.py: 정렬 일치 |
| 19 | `e49326f` | 버블정렬: 성능 측정 범위를 50000개까지 확대 | ch6_1_bubble_sort_improved.py: 정렬 일치 |
| 20 | `9638463` | 버블정렬: 거의 정렬된 데이터 성능 측정 | ch6_1_bubble_sort_improved.py: 정렬 일치 |
| 21 | `64ad28d` | 버블정렬: 성능 측정 결과 표 확장 | ch6_1_bubble_sort_improved.py: 정렬 일치 |
| 22 | `eab6160` | ---------- Ch6 - 2. Selection Sort 시작 ---------- | ch6_1_bubble_sort_improved.py: 정렬 일치 |
| 23 | `5e8a523` | 선택정렬: 실행 구조와 시각화 연결 추가 | ch6_2_selection_sort.py: 중간 구현: 미완성 |
| 24 | `9a95f4d` | 선택정렬: 첫 pass에서 최소값 후보 찾기 | ch6_2_selection_sort.py: 중간 구현: 미완성 |
| 25 | `69753db` | 선택정렬: 첫 pass에서 찾은 최소값 이동 | ch6_2_selection_sort.py: 중간 구현: 미완성 |
| 26 | `d3a69c8` | 선택정렬: 첫 위치 정렬 완료 표시 추가 | ch6_2_selection_sort.py: 중간 구현: 미완성 |
| 27 | `a213645` | 선택정렬: 두 pass까지 진행 | ch6_2_selection_sort.py: 중간 구현: 미완성 |
| 28 | `52d4d01` | 선택정렬: 모든 위치에 대해 최소값 선택 반복 | ch6_2_selection_sort.py: 정렬 일치 |
| 29 | `701cee1` | 선택정렬: 성능 측정 예제 파일 복사 | ch6_2_selection_sort.py: 정렬 일치 |
| 30 | `503d99a` | 선택정렬: 성능 측정 예제에서 시각화 제거 | ch6_2_selection_sort.py: 정렬 일치 |
| 31 | `5946d03` | 선택정렬: 일반 데이터 성능 측정 | ch6_2_selection_sort.py: 정렬 일치 |
| 32 | `6706a02` | 선택정렬: 거의 정렬된 데이터 성능 측정 | ch6_2_selection_sort.py: 정렬 일치 |
| 33 | `4469cef` | 정렬: 성능 측정 결과 문서 추가 | ch6_2_selection_sort.py: 정렬 일치 |
| 34 | `2de79b2` | 선택정렬: 최소값 보관으로 성능 측정 개선 | ch6_2_selection_sort.py: 정렬 일치 |
| 35 | `30d77db` | ---------- Ch6 - 3. Insertion Sort 시작 ---------- | ch6_2_selection_sort.py: 정렬 일치 |
| 36 | `504a32c` | 삽입정렬: 실행 구조와 시각화 연결 추가 | ch6_3_insertion_sort.py: 중간 구현: 미완성 |
| 37 | `3154ad5` | 삽입정렬: 두 번째 값을 삽입 대상으로 선택 | ch6_3_insertion_sort.py: 중간 구현: 미완성 |
| 38 | `eb7157b` | 삽입정렬: 삽입 대상 값을 왼쪽과 비교 | ch6_3_insertion_sort.py: 중간 구현: 미완성 |
| 39 | `2669d0c` | 삽입정렬: 끝까지 교환하며 왼쪽으로 이동 | ch6_3_insertion_sort.py: 중간 구현: 미완성 |
| 40 | `d467d35` | 삽입정렬: 여러 삽입 대상을 차례로 처리 | ch6_3_insertion_sort.py: 정렬 일치 |
| 41 | `aac88d2` | 삽입정렬: 교환이 필요 없으면 비교 중단 | ch6_3_insertion_sort.py: 정렬 일치 |
| 42 | `a3977e0` | 삽입정렬: 후보 값을 보관하고 큰 값들을 밀기 | ch6_3_insertion_sort.py: 정렬 일치 |
| 43 | `da1c5b4` | 삽입정렬: 성능 측정 예제 파일 복사 | ch6_3_insertion_sort.py: 정렬 일치 |
| 44 | `6dc1124` | 삽입정렬: 성능 측정 예제에서 시각화 제거 | ch6_3_insertion_sort.py: 정렬 일치 |
| 45 | `0013e2a` | 삽입정렬: 일반 데이터 성능 측정 | ch6_3_insertion_sort.py: 정렬 일치 |
| 46 | `90211da` | 삽입정렬: 거의 정렬된 데이터 성능 측정 | ch6_3_insertion_sort.py: 정렬 일치 |
| 47 | `1c20867` | 정렬: 삽입정렬 성능 결과 표에 추가 | ch6_3_insertion_sort.py: 정렬 일치 |
| 48 | `a1f76e0` | 정렬: 성능 측정 데이터 종류를 실행 인자로 선택 | ch6_3_insertion_sort.py: 정렬 일치 |
| 49 | `7d1a322` | 셸 정렬 시각화: gap 전환 때 이전 부분 배열 정렬 구간을 초기화한다 | ch6_3_insertion_sort.py: 정렬 일치 |
| 50 | `41a00a4` | ---------- Ch6 - 4. Shell Sort 시작 ---------- | ch6_3_insertion_sort.py: 정렬 일치 |
| 51 | `a8d9ec0` | 셸 정렬: 데이터와 Shell Sort 시각화를 연결하는 실행 구조를 만든다 | ch6_4_shell_sort.py: 중간 구현: 미완성 |
| 52 | `0755514` | 셸 정렬: gap 3에서 0·3·6·9 부분 배열만 삽입 정렬한다 | ch6_4_shell_sort.py: 중간 구현: 미완성 |
| 53 | `145ec0a` | 셸 정렬: gap 3의 모든 부분 배열을 offset 순서로 삽입 정렬한다 | ch6_4_shell_sort.py: 중간 구현: 미완성 |
| 54 | `31c176d` | 셸 정렬: gap 3과 1을 차례로 적용해 전체 정렬을 완성한다 | ch6_4_shell_sort.py: 정렬 일치 |
| 55 | `5408f0e` | 셸 정렬: 배열 크기에 맞는 gap 목록을 선택하도록 반복을 일반화한다 | ch6_4_shell_sort.py: 정렬 일치 |
| 56 | `f584381` | 셸 정렬: 부분 배열 반복을 전체 원소 순회로 바꿔 3중 루프로 단순화한다 | ch6_4_shell_sort.py: 정렬 일치 |
| 57 | `e05c62f` | 셸 정렬: 성능 측정 예제 파일을 현재 구현에서 복사한다 | ch6_4_shell_sort.py: 정렬 일치 |
| 58 | `f8a3049` | 셸 정렬: 성능 측정 예제에서 시각화 호출을 제거한다 | ch6_4_shell_sort.py: 정렬 일치 |
| 59 | `1245034` | 셸 정렬: 성능 비교용 Hibbard·Ciura·Tokuda gap 수열을 추가한다 | ch6_4_shell_sort.py: 정렬 일치 |
| 60 | `41bb260` | 정렬: Shell sort 성능 측정을 위해 100만 개까지의 입력 크기를 추가한다 | ch6_4_shell_sort.py: 정렬 일치 |
| 61 | `7e972d3` | 셸 정렬: Tokuda gap 수열로 일반 데이터 성능을 측정한다 | ch6_4_shell_sort.py: 정렬 일치 |
| 62 | `0a14687` | 셸 정렬: Tokuda gap 수열로 거의 정렬된 데이터 성능을 측정한다 | ch6_4_shell_sort.py: 정렬 일치 |
| 63 | `5dbb5de` | 정렬: Shell sort와 gap 수열 성능 결과를 문서에 추가한다 | ch6_4_shell_sort.py: 정렬 일치 |
| 64 | `d66713d` | 힙 정렬 시각화: 범례를 우상단으로 옮긴다 | ch6_4_shell_sort.py: 정렬 일치 |
| 65 | `74c2a67` | 시각화 메시지: 단계와 데이터 제목 사이 간격을 넓힌다 | ch6_4_shell_sort.py: 정렬 일치 |
| 66 | `3f5d661` | 힙 정렬 시각화: subtree 테두리에 heap 상태색을 유지한다 | ch6_4_shell_sort.py: 정렬 일치 |
| 67 | `0c708b0` | 힙 정렬 시각화: 교환을 부모와 자식의 이동으로 설명한다 | ch6_4_shell_sort.py: 정렬 일치 |
| 68 | `34c48a7` | ---------- Ch6 - 5. Heap Sort 시작 ---------- | ch6_4_shell_sort.py: 정렬 일치 |
| 69 | `7ab44bd` | 힙 정렬: 데이터와 Heap Sort 시각화를 연결하는 실행 구조를 만든다 | ch6_5_heap_sort.py: 중간 구현: 미완성 |
| 70 | `b9afc83` | 힙 정렬: 배열을 완전 이진 트리로 표시한다 | ch6_5_heap_sort.py: 중간 구현: 미완성 |
| 71 | `2f89978` | 힙 정렬: root와 왼쪽 자식의 값을 비교한다 | ch6_5_heap_sort.py: 중간 구현: 미완성 |
| 72 | `403e212` | 힙 정렬: 자식이 없는 leaf에서 heapify를 끝낸다 | ch6_5_heap_sort.py: 중간 구현: 미완성 |
| 73 | `710726d` | 힙 정렬: 두 자식 중 더 큰 값을 비교 후보로 고른다 | ch6_5_heap_sort.py: 중간 구현: 미완성 |
| 74 | `b173e93` | 힙 정렬: 부모와 더 큰 자식 후보를 비교한다 | ch6_5_heap_sort.py: 중간 구현: 미완성 |
| 75 | `c5f6e69` | 힙 정렬: 더 큰 자식과 부모를 교환해 heap 조건을 회복한다 | ch6_5_heap_sort.py: 중간 구현: 미완성 |
| 76 | `41d41b7` | 힙 정렬: 교환으로 내려간 부모 위치를 재귀적으로 heapify한다 | ch6_5_heap_sort.py: 중간 구현: 미완성 |
| 77 | `ad4fc80` | 힙 정렬: 마지막 부모 subtree부터 max heap을 만든다 | ch6_5_heap_sort.py: 중간 구현: 미완성 |
| 78 | `050376d` | 힙 정렬: 모든 부모 subtree를 아래에서 위로 heapify한다 | ch6_5_heap_sort.py: 중간 구현: 미완성 |
| 79 | `1b18d90` | 힙 정렬: 배열 전체가 Max Heap이 되었음을 표시한다 | ch6_5_heap_sort.py: 중간 구현: 미완성 |
| 80 | `765a2c3` | 힙 정렬: root의 최대값을 heap 마지막 원소와 교환한다 | ch6_5_heap_sort.py: 중간 구현: 미완성 |
| 81 | `3867f77` | 힙 정렬: heap 크기를 줄이고 정렬 완료 구간을 표시한다 | ch6_5_heap_sort.py: 중간 구현: 미완성 |
| 82 | `c45b2dd` | 힙 정렬: 새 root에서 downheap으로 Max Heap을 회복한다 | ch6_5_heap_sort.py: 중간 구현: 미완성 |
| 83 | `0e3582a` | 힙 정렬: 최대값을 하나씩 꺼내 전체 배열을 정렬한다 | ch6_5_heap_sort.py: 정렬 일치 |
| 84 | `5057bb0` | 힙 정렬: 성능 측정 예제를 현재 구현에서 복사한다 | ch6_5_heap_sort.py: 정렬 일치 |
| 85 | `03c66a8` | 정렬: Heap sort 성능 측정과 결과 문서를 추가한다 | ch6_5_heap_sort.py: 정렬 일치 |
| 86 | `80038a7` | 힙 정렬 성능: 재귀 없는 downheap 개선 버전을 추가한다 | ch6_5_heap_sort.py: 정렬 일치 |
| 87 | `21d162f` | 힙 정렬 성능: downheap에서 자식을 밀어 올린다 | ch6_5_heap_sort.py: 정렬 일치 |
| 88 | `5e606e7` | 힙 정렬 성능: 개선 버전의 측정 결과를 기본 구현과 나란히 기록한다 | ch6_5_heap_sort.py: 정렬 일치 |
| 89 | `bd00100` | 정렬: Heap sort의 100만 개 성능 기록을 문서에 추가한다 | ch6_5_heap_sort.py: 정렬 일치 |
| 90 | `2703f4b` | 정렬: 4주차 고급 정렬 용어집을 추가한다 | ch6_5_heap_sort.py: 정렬 일치 |
| 91 | `bb2e973` | ---------- Ch6 - 6. Count Sort 시작 ---------- | ch6_5_heap_sort.py: 정렬 일치 |
| 92 | `27ae8ec` | 계수 정렬: 1~15 범위의 80개 시각화 데이터를 준비한다 | ch6_5_heap_sort.py: 정렬 일치 |
| 93 | `3a10742` | 계수 정렬: 값 범위가 다른 추가 시각화 데이터를 넣는다 | ch6_5_heap_sort.py: 정렬 일치 |
| 94 | `344e105` | 계수 정렬 시각화: 큰 배열의 행 제목이 겹치지 않게 배치한다 | ch6_5_heap_sort.py: 정렬 일치 |
| 95 | `5786190` | 계수 정렬: 실행 구조와 시각화를 연결한다 | ch6_6_count_sort.py: 중간 구현: 미완성 |
| 96 | `1fff768` | 계수 정렬: counts 배열을 초기화하고 시각화 데이터를 정돈한다 | ch6_6_count_sort.py: 중간 구현: 미완성 |
| 97 | `e23e30f` | 계수 정렬: 첫 원소의 등장 횟수를 기록한다 | ch6_6_count_sort.py: 중간 구현: 미완성 |
| 98 | `0a886cf` | 계수 정렬: 모든 값의 등장 횟수를 센다 | ch6_6_count_sort.py: 중간 구현: 미완성 |
| 99 | `29f6d11` | 계수 정렬: counts 배열의 첫 누적합을 계산한다 | ch6_6_count_sort.py: 중간 구현: 미완성 |
| 100 | `f5c7766` | 계수 정렬: counts 배열 전체를 누적합으로 바꾼다 | ch6_6_count_sort.py: 중간 구현: 미완성 |
| 101 | `cb15975` | 계수 정렬: 정렬 결과를 담을 배열을 준비한다 | ch6_6_count_sort.py: 중간 구현: 미완성 |
| 102 | `b5086fa` | 계수 정렬: 마지막 원소를 결과 배열에 배치한다 | ch6_6_count_sort.py: 중간 구현: 미완성 |
| 103 | `42a1be9` | 계수 정렬: 모든 원소를 결과 배열에 배치한다 | ch6_6_count_sort.py: 정렬 일치 |
| 104 | `1aea927` | 계수 정렬: 성능 측정용 구현 파일을 추가한다 | ch6_6_count_sort.py: 정렬 일치 |
| 105 | `07b73cb` | 성능 측정: 입력 배열 생성 시간을 함께 표시한다 | ch6_6_count_sort.py: 정렬 일치 |
| 106 | `6fd2709` | 정렬 데이터: 값 종류를 제한한 난수 생성을 추가한다 | ch6_6_count_sort.py: 정렬 일치 |
| 107 | `0552cbf` | 성능 측정: 대용량 배열을 복사 없이 측정한다 | ch6_6_count_sort.py: 정렬 일치 |
| 108 | `9f1ef47` | 계수 정렬: 1천만 개 이상의 대용량 측정을 추가한다 | ch6_6_count_sort.py: 정렬 일치 |
| 109 | `60059d5` | 계수 정렬: 대용량 성능 측정 결과를 기록한다 | ch6_6_count_sort.py: 정렬 일치 |
| 110 | `7e5dd72` | ---------- Ch6 - 7. Radix Sort: LSD 시작 ---------- | ch6_6_count_sort.py: 정렬 일치 |
| 111 | `ee0a4e6` | 기수 정렬 LSD: 전용 데이터와 시각화 실행 구조를 추가한다 | ch6_7_radix_lsd.py: 중간 구현: 미완성 |
| 112 | `82a2235` | 기수 정렬 LSD: 1의 자리 기준 계수 정렬을 구현한다 | ch6_7_radix_lsd.py: 중간 구현: 미완성 |
| 113 | `f2936de` | 기수 정렬 LSD: 10의 자리 기준 정렬을 추가한다 | ch6_7_radix_lsd.py: 중간 구현: 미완성 |
| 114 | `aa68fb3` | 기수 정렬 LSD: 모든 자리수 정렬을 반복한다 | ch6_7_radix_lsd.py: 정렬 일치 |
| 115 | `d2854a2` | 기수 정렬 LSD: 성능 측정용 파일을 현재 버전으로 복사한다 | ch6_7_radix_lsd.py: 정렬 일치 |
| 116 | `0ef873a` | 기수 정렬 LSD: 시각화 없이 성능을 측정한다 | ch6_7_radix_lsd.py: 정렬 일치 |
| 117 | `139654a` | 기수 정렬 LSD: 5천만 개까지 대용량 측정을 추가한다 | ch6_7_radix_lsd.py: 정렬 일치 |
| 118 | `19b8339` | 기수 정렬 LSD: 5천만 개까지 성능 측정 결과를 기록한다 | ch6_7_radix_lsd.py: 정렬 일치 |
| 119 | `bee8a69` | ---------- Ch6 - 8. Radix Sort: MSD 시작 ---------- | ch6_7_radix_lsd.py: 정렬 일치 |
| 120 | `6f2eb55` | 기수 정렬 MSD: 단어 데이터와 시각화 실행 구조를 추가한다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 121 | `49f7032` | 기수 정렬 MSD: 전체 단어 구간을 재귀 스택에 넣는다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 122 | `6200f33` | 기수 정렬 MSD: 첫 글자 bucket의 개수 배열을 준비한다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 123 | `497c8d0` | 기수 정렬 MSD: 첫 단어를 첫 글자 bucket에 기록한다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 124 | `0e42b5a` | 기수 정렬 MSD: 전체 단어의 첫 글자 bucket을 센다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 125 | `fbe8ca3` | 기수 정렬 MSD: bucket 개수를 누적합 인덱스로 바꾼다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 126 | `3fb6003` | 기수 정렬 MSD: 단어를 옮길 임시 배열을 준비한다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 127 | `b269714` | 기수 정렬 MSD: 마지막 단어 하나를 임시 배열에 배치한다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 128 | `f80ba7d` | 기수 정렬 MSD: 모든 단어를 첫 글자 bucket에 배치한다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 129 | `6123052` | 기수 정렬 MSD: 첫 글자 기준 순서를 원래 배열에 복사한다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 130 | `b1a10bb` | 기수 정렬 MSD: e bucket을 다음 depth 재귀 구간으로 표시한다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 131 | `f9ca8af` | 기수 정렬 MSD: e 구간의 둘째 글자 bucket을 준비한다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 132 | `cf442ef` | 기수 정렬 MSD: e 구간의 둘째 글자 bucket을 모두 센다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 133 | `686c398` | 기수 정렬 MSD: e 구간의 둘째 글자 bucket을 누적합으로 바꾼다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 134 | `87da0f9` | 기수 정렬 MSD: e 구간을 배치할 임시 배열을 준비한다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 135 | `d4397b5` | 기수 정렬 MSD: e 구간을 둘째 글자 bucket에 배치한다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 136 | `2b6e631` | 기수 정렬 MSD: 둘째 글자 기준 e 구간을 원래 배열에 복사한다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 137 | `5670c5b` | 기수 정렬 MSD: 한 구간을 정렬하는 공통 함수를 만든다 | ch6_8_radix_msd.py: 중간 구현: 미완성 |
| 138 | `14b1d28` | 기수 정렬 MSD: 같은 글자 bucket을 다음 depth에서 재귀 정렬한다 | ch6_8_radix_msd.py: 정렬 일치 |
| 139 | `890d69f` | 기수 정렬 MSD: 재귀 구간을 pop하고 전체 정렬을 완료한다 | ch6_8_radix_msd.py: 정렬 일치 |
| 140 | `06f1795` | 기수 정렬 MSD: 재귀 호출이 임시 배열 하나를 공유한다 | ch6_8_radix_msd.py: 정렬 일치 |
| 141 | `ac6a96b` | 기수 정렬 MSD: 깊은 공통 prefix 단어 320개를 추가한다 | ch6_8_radix_msd.py: 정렬 일치 |
| 142 | `08ae6b9` | 기수 정렬 MSD: e~o 전용 비시각화 파일을 복사한다 | ch6_8_radix_msd_e_to_o.py: 정렬 일치 |
| 143 | `30a20b5` | 기수 정렬 MSD: e~o 전용 단어 데이터셋을 분리한다 | ch6_8_radix_msd_e_to_o.py: 정렬 일치 |
| 144 | `8e6685d` | 기수 정렬 MSD: e~o 버전에서 시각화 의존성을 제거한다 | ch6_8_radix_msd_e_to_o.py: 정상 종료 (stdout 참조) |
| 145 | `da71732` | 기수 정렬 MSD: e~o 범위로 bucket을 일반화한다 | ch6_8_radix_msd_e_to_o.py: 정상 종료 (stdout 참조) |
| 146 | `f0324d3` | 기수 정렬 MSD: e~o 입력 범위와 정렬 결과를 검증한다 | ch6_8_radix_msd_e_to_o.py: 정상 종료 (stdout 참조) |
