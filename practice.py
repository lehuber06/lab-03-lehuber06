names = ["Michael", "Cooper", "Meghan", "Jack", "Caleb", "Jackie", "Lee"]
print(names)

del names[-1]
print(names)

names.append("James Bond")
print(names)

for name in names:
    print(f"{name} is on my table!")

names.sort(reverse=True)
print(names)
