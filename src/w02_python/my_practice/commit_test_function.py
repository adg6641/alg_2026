

def square(x):
    return x * x


print("-- define and call function --")
print(square(3))
print(square(10))


def print_score(name, score):
    print(name, ":", score)


print_score("Kim", 91)
print_score("Lee", 84)
print()


print("-- local and global variables --")

message = "global message"


def show_scope():
    message = "local message"
    print("inside function:", message)


show_scope()
print("outside function:", message)
print()


print("-- positional and keyword arguments --")


def describe_student(name, score, passed=True):
    print("name:", name, "score:", score, "passed:", passed)


describe_student("Park", 77)

describe_student(name="Choi", score=95, passed=True)
describe_student(score=62, name="Jung", passed=False)
print()


print("-- return multiple values --")


def find_min_max(values):
    min_value = min(values)
    max_value = max(values)

    return min_value, max_value


numbers = [7, 2, 9, 4]
result = find_min_max(numbers)
smallest, largest = find_min_max(numbers)

print("result tuple:", result)
print("smallest:", smallest)
print("largest:", largest)
