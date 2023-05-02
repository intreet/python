a = (int(input("введите значение cтроны а триугольника ")))
b = (int(input("введите значение cтроны b триугольника ")))
c = (int(input("введите значение cтроны c триугольника ")))
h = (int(input("введите значение высоты триугольника ")))

triangle_perimetr = a + b + c
triangle_area = 0,5 * (a * h)

print("периметр треугольника = ",triangle_perimetr)
print("площядь триугольника = ",triangle_area)