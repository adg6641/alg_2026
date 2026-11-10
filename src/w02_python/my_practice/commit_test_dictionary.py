

scores = {
    "Kim": 91,
    "Lee": 84,
    "Park": 77,
}

print("-- dictionary --")
print(scores)
print()


print("-- lookup by key --")
print("Kim:", scores["Kim"])
print("Lee:", scores["Lee"])
print()


scores["Park"] = 88
print("-- update value --")
print(scores)
print()


print("-- missing key raises KeyError --")

try:
    print(scores["Choi"])
except KeyError as error:
    print("KeyError:", error)
print()


print("-- check key before lookup --")

name = "Choi"
if name in scores:
    print(name, scores[name])
else:
    print(name, "is not in scores")
print()


print("-- get with default value --")

print("Kim:", scores.get("Kim", 0))
print("Choi:", scores.get("Choi", 0))
print("after get:", scores)

name = "Kim"
if name in scores:
    print(name, scores[name])
else:
    print(name, "is not in scores")
