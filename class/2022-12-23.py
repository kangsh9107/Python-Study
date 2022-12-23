# a = "Life is too short, you need python"
# if "wife" in a:
#     print("wife")
# elif "python" in a and "you" not in a:
#     print("python")
# elif "shirt" not in a:
#     print("shirt")
# elif "need" in a:
#     print("need")
# else:
#     print("none")

# result = 0
# i = 0
# while i < 1000:
#     i += 1
#     if i % 3 == 0:
#         result += i
# print(result)

# a = '*'
# i = 0
# while i < 5:
#     i += 1
#     print(a * i)

# for i in range(1, 101):
#     print(i)

# a = [70,60,55,75,95,90,80,80,85,100]
# sum = 0
# for s in a:
#     sum += s
# print(sum/len(a))

# numbers = [1,2,3,4,5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)

# print(result)

# result = [n*2 for n in numbers if n%2 == 1]
# print(result)

# def say():
#     return 'Hi'
# a = say()
# print(a)

# def add(a, b):
#     print("%d, %d의 합은 %d입니다." % (a, b, a+b))
# add(3, 4)
# add(b=4, a=3)

# def say():
#     print('Hello')
# say()

# def add_many(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
# print(add_many(1,2,3,4,5))

# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result += i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result += i
#     return result
# print(add_mul('add', 1,2,3,4,5))
# print(add_mul('mul', 1,2,3,4,5))

# def print_kwargs(**kwargs):
#     print(kwargs)
# print_kwargs(a=1)
# print_kwargs(name='temp', age=3)

# def say_myself(old, man=True, name='홍'):
#     print("나의 이름은 %s입니다." % name)
#     print("나이는 %d살입니다." % old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")
# say_myself(20)
# say_myself(20, False)

# print("단을 입력하세요", end="")
# dan = int(input())
# i = 1
# while i < 10:
#     r = dan * i
#     print("%d * %d = %d" % (dan, i, r))
#     print(f"{dan} * {i} = {r}")
#     print("{0} * {1} = {2}".format(dan, i, r))
#     i += 1

# a = 1
# def test(a):
#     a += 1
# test(a)
# print(a)

# a = 1
# def test(a):
#     a += 1
#     return a
# a = test(a)
# print(a)

# a = 1
# def test():
#     global a
#     a += 1
# test()
# print(a)

# add = lambda a, b: a+b
# result = add(3, 4)
# print(result)

# a = input()
# print("a" + a)

# for i in range(10):
#     print(i, end=",")

# def is_odd(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# print(is_odd(3))

# def avg(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result/len(args)
# print(avg(1,2,3))

# input1 = input("첫번째 숫자를 입력하세요:")
# input2 = input("두번째 숫자를 입력하세요:")
# total = float(input1) + float(input2)
# print("두 수의 합은 %s 입니다." % total)

# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result

# a = FourCal()
# a.setdata(4, 2)
# b = FourCal()
# b.setdata(4, 3)
# print(id(a.first))
# print(id(b.first))
# print(id(a.second))
# print(id(b.second))
# print(a.add())

# class FourCal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result

# a = FourCal(1, 2)
# print(a.add())

# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result
# b = MoreFourCal(3, 4)
# print(b.add())
# print(b.pow())

# class SafeFourCal(FourCal):
#     def add(self):
#         if self.second == 0:
#             return "0으로 나눌 수 없습니다."
#         else:
#             return self.first + self.second
# c = SafeFourCal(1, 0)
# print(c.add())
# print(a.add())

# class Family:
#     lastname = "김"
# print(Family.lastname)
# a = Family()
# print(a.lastname)

# Family.lastname = "박"
# print(Family.lastname)
# print(a.lastname)

# print(abs(-1))
# print(chr(48))

# print(dir([1,2,3]))

# print(divmod(7, 3))

# def positive(x):
#     return x > 0
# print(list(filter(positive, [1,-3,2,0,-5,6])))

# import time
# for i in range(10):
#     print(i)
#     time.sleep(1)

# import calendar
# print(calendar.calendar(2022))
# print(calendar.weekday(2015,12,31))

# import random
# print(random.random())
# print(random.randint(1, 10))
# print(random.randint(1, 2))

