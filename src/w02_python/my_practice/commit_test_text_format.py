

name = "Kim"
score = 91
average = 87.625

print("-- percent formatting --")

print("%s scored %d points" % (name, score))
print("average: %.2f" % average)
print()


print("-- format function --")

print("{} scored {} points".format(name, score))

print("{1} points were scored by {0}".format(name, score))

print("{student}: {points}".format(student=name, points=score))
print()


print("-- f-string --")

print(f"{name} scored {score} points")
print(f"average: {average:.2f}")

bonus = 5
print(f"after bonus: {score + bonus}")
