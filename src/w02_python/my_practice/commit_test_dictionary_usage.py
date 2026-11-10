

words = [
    "apple",
    "algorithm",
    "banana",
    "binary",
    "cat",
    "code",
    "data",
]

counts = {}

for word in words:
    first_char = word[0]

    if first_char not in counts:
        counts[first_char] = 0

    counts[first_char] += 1

print("-- count words by first character --")
print(counts)
print()


print("-- iteration order --")

for first_char in counts:
    print(first_char, counts[first_char])
print()


print("-- sorted keys --")

for first_char in sorted(counts.keys()):
    print(first_char, counts[first_char])
print()


print("-- defaultdict --")

from collections import defaultdict

simple_counts = defaultdict(int)

for word in words:
    first_char = word[0]

    simple_counts[first_char] += 1

print(dict(simple_counts))
print()


print("-- items --")

for first_char, count in counts.items():
    print(first_char, "=>", count)
print()


print("-- nested dictionary as graph --")

graph = {
    "A": {"B": 3, "C": 5},
    "B": {"C": 1},
    "C": {"A": 2},
}

for u, adjs in graph.items():
    for v, weight in adjs.items():
        print(u, "->", v, "weight:", weight)
print()


print("-- keys and values --")

for name in graph:
    print("vertex:", name)
print()

for name in graph.keys():
    print("key:", name)
print()

for adjs in graph.values():
    print("adjacent dictionary:", adjs)
print()

for name in sorted(graph.keys()):
    print("sorted key:", name)
