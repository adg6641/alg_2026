

print("-- build list with loop --")

numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
    squares.append(number * number)

print("numbers:", numbers)
print("squares:", squares)
print()


print("-- list comprehension --")

squares2 = [number * number for number in numbers]

print("squares2:", squares2)
print()


print("-- map --")


def square(number):
    return number * number


mapped_squares = map(square, numbers)
print("mapped_squares:", mapped_squares)
print()


print("-- convert map to list --")

mapped_squares = map(square, numbers)
print("list(mapped_squares):", list(mapped_squares))
print()


print("-- lambda --")

lambda_squares = list(map(lambda number: number * number, numbers))
print("lambda_squares:", lambda_squares)
print()


print("-- sorted with key --")

edges = [
    ("A", "B", 7),
    ("A", "C", 2),
    ("B", "C", 5),
]

sorted_edges = sorted(edges, key=lambda edge: edge[2])
print("sorted by weight:", sorted_edges)

points = [(3, 4), (1, 7), (2, 1)]
sorted_by_y = sorted(points, key=lambda point: point[1])
print("sorted by y:", sorted_by_y)
print()


print("-- two dimensional list --")

rows = 3
cols = 4

table = [[0 for _ in range(cols)] for _ in range(rows)]
table[1][2] = 9

for row in table:
    print(row)
print()


print("-- two dimensional list aliasing pitfall --")

bad_table = [[0] * cols] * rows
bad_table[1][2] = 9

for row in bad_table:
    print(row)
print()


print("-- class constructor with map --")


class Point:
    def __init__(self, pair):
        self.x = pair[0]
        self.y = pair[1]

    def length_from_origin(self):
        return (self.x * self.x + self.y * self.y) ** 0.5


pairs = [(3, 4), (5, 12), (8, 15)]

points = list(map(Point, pairs))

for point in points:
    print(point.x, point.y, point.length_from_origin())
