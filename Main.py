# a = 1
# b = 2
# print(a+b)

# str = "Python"
# print(str)

# if a > 1:
#     print(a)
# else:
#     print(b)

# for c in [1,2,3,4,5]:
#     print(c)

# i = 0
# while i < 3:
#     i = i + 1
#     print(i)

# def add(x, y):
#     return x + y

# print(add(3, 4))

"""
주석주석주석
"""

# a = 10
# a = 2.24E3
# print(a)
# print(3**2)
# print(7/4)
# print(7//4)
# print(7%4)
# print("""ok""")
# print("""aaaa
# bbbb
# cccc""")
# print("a\tb")
# print("a"*2)
# print("a"+"b")
# print("-"*50)

# name = "black"
# print(len(name))

# str = "abc"
# print(len(str))

# print(len("12345"))

# a = "Life is too short, You need Python"
# print(a[27])
# print(a[-1])
# print(a[8:11])
# print(a[-1:])
# print(a[5:])
# print(a[:17])
# print(a[:])
# print(a[19:-7])

# a = "20010331Rainy"
# date = a[:8]
# weather = a[8:]
# print(date)
# print(weather)

# year = a[:4]
# day = a[4:8]
# weather = a[8:]
# print(year)
# print(day)
# print(weather)

# a = "pithon"
# print(a)
# print(a[0] + "y" + a[2:])

# print("I eat %d apples." % 3)
# print("I eat %s apples." % "five")
# number = 3
# print("I eat %d apples." % number)

# number = 10
# day = "three"
# print("I ate %d apples. so I was sick for %s days." % (number, day))
# print("Error is %d%%." % 98)
# print("%10s" % "hi")
# print("%-10sjane" % "hi")
# print("%10.4f" % 3.42134234)

# number = 10
# day = "three"
# print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
# print("I ate {su} apples. so I was sick for {nal} days.".format(su=5, nal=2))
# print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))

# print("{0:>10}".format("hi"))
# print("{0:<10}".format("hi"))
# print("{0:^10}".format("hi"))

# print("{0:=^10}".format("hi"))
# print("{0:!<10}".format("hi"))
# print("{0:!>10}".format("hi"))

# y = 3.42134234
# print("{0:0.4f}".format(y))
# print("{0:10.4f}".format(y))
# print("{0:<10.4f}".format(y))

# print("{{ and }}".format())

# name = "홍길동"
# age = 30
# print(f"나의 이름을 {name}입니다. 나이는 {age}입니다.")
# print(f"나는 내년이면 {age+1}살이 된다.")

# d = {'name' : '이몽룡', 'age' : 30}
# print(d["name"])
# print(f"나의 이름은 {d['name']}입니다. 나이는 {d['age']}입니다.")
# print(f"{'hi':>10}")
# print(f"{'hi':^10}")

# print(f"{'hi':@>10}")
# y = 3.42134234
# print(f"{y:0.4f}")
# print(f"{y:10.4f}")
# print(f"{{ and }}")

# a = "hobby"
# print(a.count("b"))

# a = "Python is the best choice"
# print(a.find('b'))
# print(a.find('k'))
# print(a.index('b'))

print(",".join('abcd'))
a = "total"
b = ".".join(a)
print(b)

print(",".join(["a", "b", "c"]))