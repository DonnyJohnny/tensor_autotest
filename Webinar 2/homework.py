# Задание 1
a = 5  # Сторона квадрата
print("Задание №1")
print("Сторона квадрата = ", a)
print("Периметр квадрата = ", 4 * a)
print("Площадь квадрата = ", a ** 2)
print("Диагональ квадрата = ", (2 * a ** 2) ** 0.5)
print()

# Задание 2. ax^2 + bx + c = 0
a = 2
b = 5
c = -7

d = b ** 2 - 4 * a * c

x1 = (-1 * b - d ** 0.5) / (2 * a)
x2 = (-1 * b + d ** 0.5) / (2 * a)

print("Задание №2")
print("Корни кв. уравнения ax^2 + bx + c = 0, где a = {}, b = {}, c = {}".format(a, b, c))
print("x1 = ", x1)
print("x2 = ", x2)
print()

# Задание 3
s1 = "123456"
s2 = "qwerty"

print("Задание №3")
print("Исходные строки:")
print(s1)
print(s2)

s1, s2 = s2[:2] + s1[2:], s1[:2] + s2[2:]

print("Результат:")
print(s1 + " " + s2)
print()

# Задание 4
path = r"C:\Users\DonnyJohnny\Desktop\Education\Tensor.Autotest\Webinar 2\homework.py"

t = path.split("\\")
file_name = t[-1].split(".")[0]

print("Задание №4")
print("Абсолютный путь: ", path)
print("Название файла: ", file_name)
print("Диск: ", t[0][:-1])
print("Корневая папка: ", t[1])
print()

# Задание 5
a = 5
b = 8
c = a * b

print("Задание №5")
print("{} + {} = {}".format(a, b, a + b))
print(f"{a} * {b} = {c}")
print()

# Задание 6
s = "1q2w3e4r5t6y7u8i9o0p"

print("Задание №6")
print("Исходная строка: ", s)
print("Результат: ", s[1::2])  # Индексацию начинал как в жизни с 1, а не с 0
print()

# Задание 7
first_string = "wtf"
second_string = "brick quz jmpy veldt whangs fox"

print("Задание №7")
print("Первая строка: ", first_string)
print("Вторая строка: ", second_string)

i1 = second_string.find(first_string[0])
i2 = second_string.find(first_string[1])
i3 = second_string.find(first_string[2])

print("Результат:")
print(second_string[min(i1, i2, i3): max(i1, i2, i3) + 1])
