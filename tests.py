height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human Height is out of Range")

bmi = weight / height ** 2
print(bmi)