

letters = ["a", "b", "c", "d", "e", "f"]

print("-- original list --")
print(letters)
print()


print("-- basic slicing --")

print("letters[1:4] =", letters[1:4])

print("letters[:3] =", letters[:3])

print("letters[3:] =", letters[3:])
print()


print("-- negative index --")

print("letters[-1] =", letters[-1])
print("letters[-3:] =", letters[-3:])
print()


print("-- reference vs slicing copy --")

original = [10, 20, 30]

copied_name = original
copied_name[0] = 99
print("after copied_name[0] = 99")
print("original:", original)
print("copied_name:", copied_name)

sliced_copy = original[:]
sliced_copy[1] = 77
print("after sliced_copy[1] = 77")
print("original:", original)
print("sliced_copy:", sliced_copy)
