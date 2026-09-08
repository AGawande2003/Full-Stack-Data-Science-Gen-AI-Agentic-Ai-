l = ["Python", "Java", "SQL", "IoT", "Math"]

print("Original list:", l)

l.append("AI")
print("After append:", l)

l.insert(1, "C")
print("After insert:", l)

l.remove("Math")
print("After remove:", l)

print("Length:", len(l))
print("First subject:", l[0])
print("Last subject:", l[-1])
print("First three l:", l[:3])

copied_l = l.copy()
print("Copied list:", copied_l)

l.clear()
print("After clear:", l)
