

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

indices = range(10)

print("-- list vs range --")
print(numbers)
print(indices)
print()


print("-- for loop over list --")
for value in numbers:
    print(value, end=" - ")
print("//")

print("-- for loop over range --")
for value in indices:
    print(value, end=" - ")
print("//")
print()


print("A", end=" ")
print("B", end=" ")
print("C")
print()


print("-- len of list / range --")
print(len(numbers))
print(len(indices))
print("first:", numbers[0])
print("last:", numbers[len(numbers) - 1])
print()


print("-- range to list --")
print(list(indices))
print()


print("-- value loop vs index loop --")

for score in [82, 91, 77]:
    print("score:", score)

scores = [82, 91, 77]
for i in range(len(scores)):
    print("index:", i, "score:", scores[i])
print()


print("-- enumerate --")

for i, score in enumerate(scores):
    print("index:", i, "score:", score)
print()


print("-- list update / append / pop --")

scores = [82, 91, 77]
print("before:", scores)

scores[2] = 88
print("after update:", scores)

scores.append(95)
print("after append:", scores)

last_score = scores.pop()
print("popped:", last_score)
print("after pop:", scores)
