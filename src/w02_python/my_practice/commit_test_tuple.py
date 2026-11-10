

print("-- create tuple --")

point = (10, 20)
record = 1, "Kim", 91

print(point)
print(record)
print()


print("-- unpacking --")

x, y = point
number, name, score = record

print("x:", x)
print("y:", y)
print("name:", name)
print("score:", score)
print()


print("-- tuple is immutable, list is mutable --")

tuple_point = (100, 200)
list_point = [100, 200]

try:
    tuple_point[1] = 250
except TypeError as error:
    print("tuple update error:", error)

list_point[1] = 250

print("tuple_point:", tuple_point)
print("list_point:", list_point)
print()


print("-- convert tuple and list --")

fixed_point = (3, 4)

editable_point = list(fixed_point)
editable_point[0] = 30

changed_point = tuple(editable_point)

print("fixed_point:", fixed_point)
print("editable_point:", editable_point)
print("changed_point:", changed_point)
