from math import pi

print("==================")
print("Area Calculater 📐")
print("==================")
print("")
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")
print("")

shape = int(input('Which shape: '))
print("")

if shape == 1:
  base = int(input('Base: '))
  height = int(input('Height: '))
  print("")
  area = base * height / 2
elif shape == 2 or shape == 3:
  base = int(input('Base: '))
  height = int(input('Height: '))
  print("")
  area = base * height
elif shape == 4:
  radius = int(input('Radius: '))
  p = pi()
  area = p * radius * radius
else:
  exit()

print(f"The area is {area}")



  
