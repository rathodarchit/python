#Array

cars = ["Nano","NanoXL"]
cars[0] = "XYZ"
print(cars[0])
print(len(cars))
cars.append("Homda")
cars.append("Honda1")
cars.pop(0)
cars.remove("Honda1")
for x in cars:
    print(x)