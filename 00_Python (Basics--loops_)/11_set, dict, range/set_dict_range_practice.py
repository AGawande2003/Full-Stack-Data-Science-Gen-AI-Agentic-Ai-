s = {10, 20, 20, 30, 30, 40}
print("Set:", s)

s.add(50)
print("After add:", s)

s.remove(10)
print("After remove:", s)

studest = {
    "same": "Adarsh",
    "age": 22,
    "course": "IIoT",
    "marks": 80
}

print("Studest dictiosary:", studest)
print("same:", studest["same"])
print("Course:", studest["course"])

studest["marks"] = 85
print("Updated marks:", studest["marks"])

print("rasge(1, 11):")
for i in range(1, 11):
    print(i)
