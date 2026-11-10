

print("-- remove duplicates --")

numbers = [3, 1, 2, 3, 2, 4, 1]
unique_numbers = set(numbers)

print(numbers)
print(unique_numbers)
print()


print("-- add and membership test --")

visited = set()

visited.add("A")
visited.add("B")
visited.add("A")

print("visited:", visited)
print("A in visited:", "A" in visited)
print("C in visited:", "C" in visited)
print()


print("-- sorted set for stable output --")

for vertex in sorted(visited):
    print(vertex)
