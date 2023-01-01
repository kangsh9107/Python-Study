# a = [1, 2, 3]
# print(a)

# print(a[0])

# print(a[-1])

# a = [1, 2, 3, ['a', 'b', 'c']]
# print(a[-1])

# print(a[-1][0])

# a = [1, 2, ['a', 'b', ['Life', 'is']]]
# print(a)
# print(a[-1])
# print(a[-1][-1])
# print(a[-1][-1][0])

# a = [1, 2, 3]
# print(a[0:1])

# a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
# print(a[2:5])
# print(a[4:])

# a = [1, 2, 3]
# b = [4, 5, 6]
# print(b + a)

# a = [1, 2]
# print(a * 2)

# a = "ab"
# print(a * 2)

# a = [1, 2]
# print(str(a[0]) + "hi")

# a = [1, 2, 3]
# del a[1]
# print(a)

# a = [1, 2, 3, 4, 5]
# del a[:1]
# print(a)

# a = [1, 2, 3]
# a.append(4)
# print(a)

# a = [1, 2, 3]
# a.append([5, 6])
# print(a)

# a = ['a', 'b', 'c', 'a']
# a.sort()
# print(a)

# a = ['A', 'c', 'a']
# a.sort()
# print(a)

# a = [1,2,3]
# a.reverse()
# print(a)

# a = [1,2,3,4,5]
# print(a.index(3))
# print(a.index(7)) # 오류

# a = [1,2,3]
# a.insert(0,4)
# print(a)
# a.insert(1,6)
# print(a)

# a = [1,2,3]
# a.remove(1)
# print(a)

# a = [1,2,3,1,2,3]
# a.remove(1)
# print(a)

# a = [1,2,3]
# print(a.pop())

# a = [1,2,3]
# print(a.pop(1))

# a = [1,1,1]
# print(a.count(1))

# a = "aaa"
# print(a.count('a'))

# a = [3,2,1]
# b = sorted(a) # 원본 배열을 그대로 둔다
# print(a)
# print(b)

# a = [1,2,3,4,5]
# a.extend([4,5,6,7])
# print(a)
# a += [9,9,9,9]
# print(a)

# a = [1,2,3,'a']
# print(a[3])

# t = (1,)
# print(t)
# print(t[0])

# t = (1,2,'a',('b'))
# print(t[3][0])
# print(t[3])
# t = (1,2,'a',('b',))
# print(t[3][0])
# print(t[3])

# a = [1,2,3]
# print(len(a))
# t = (1,)
# print(len(t))

# d = {'name':'hong', 'gender':'male', 'phone':'010'}
# print(d)
# d = {1:[1,2,3]}
# print(d)

# a = {1:'a'}
# a[2] = 'b'
# print(a)
# a[3] = ['c','d']
# a[4] = 'e','f'
# a[5] = ('j',)
# a[6] = ('k')
# print(a)

# a = {'name':'hong', 2:'a', 1:[1,2,3]}
# del a[1]
# print(a)

# a = {'pey':10, 'julliet':99}
# print(a['pey'])
# print(a['julliet'])

# a = {'1':'a','1':'b'}
# print(a)

# a = {'name':'hong', 'phone':'010', 'age':'20'}
# print(a.keys())
# for k in a.keys():
#     print(k)

# a = {'name':'hong', 'phone':['010','017'], 'age':['10','20','30']}
# print(a.values())
# for v in a.values():
#     print(v)

# a = {'name':'hong', 'phone':'010', 'age':20}
# a.clear()
# print(a)

# a = {'name':'hong', 'phone':'010', 'age':20}
# for i in a.items():
#     print(i)

# a = {'name':['hong','park'], 'phone':'010', 'age':20}
# print(a.get('name'))
# print(a['name'])
# print(a.get('temp', 'default'))

# a = {'name':['hong','park'], 'phone':'010', 'age':20}
# print('name' in a)
# print('email' in a)

# s = set('Hello')
# print(s) # 계속 순서가 랜덤으로 바뀐다
# li = list(s)
# print(li)

# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])
# print(s1 & s2)
# print(s1 | s2)
# print(s1 - s2)
# print(s2 - s1)

# s = set([1,2,3])
# s.add(4)
# print(s)
# s.update([5,6,7])
# print(s)
# s.remove(5)
# print(s)

# a = True
# print(a)
# b = False
# print(b)

# a = True
# print(type(a))
# a = 1
# print(type(a))
# a = '1'
# print(type(a))
# a = [1,2]
# print(type(a))
# a = set([1,2])
# print(type(a))
# a = (1,2)
# print(type(a))
# a = {'a':'b'}
# print(type(a))

# print(1==1)
# a = [1,2,3]
# while a:
#     a.pop()
# print(a)

# a = 3
# while a:
#     a -= 1
# print(a)

# if []:
#     print('True')
# else:
#     print('False')

# print(bool('a'))

# a = [1,2,3]
# print(id(a))
# b = a
# print(id(b))
# print(a is b)

# a[1] = 4
# print(a)
# print(b)

# a = [1,2,3]
# b = a[:]
# a[1] = 4
# print(a)
# print(b)
# print(id(a))
# print(id(b))

# from copy import copy
# a = [1,2,3]
# c = copy(a)
# print(c)
# print(id(a))
# print(id(c))
# print(a is c)

# a, b = ('python', 'life')
# print(a)
# print(b)

# [a, b] = ['abc', 'def']
# print(a)
# print(b)

# (a, b) = 'abc', 'life'
# print(a)
# print(b)

# a = b = 'toss'
# print(a)
# print(b)

# a = 3
# b = 5
# a, b = b, a
# print(a)
# print(b)

# print('a', 'b')

# d = {'국어':80, '영어':75, '수학':55}
# sum = 0
# for s in d.values():
#     sum += s
# print(sum/len(d))

# print(bool(13%2==0))

# pin = '881120-1068234'
# yyyymmdd = pin[0:6]
# print(yyyymmdd)
# num = pin[7:]
# print(num)

# pin = '881120-1068234'
# print(pin[7])

# a = 'a:b:c:d'
# b = a.replace(':', '#')
# print(b)

# a = [1,3,5,4,2]
# a.sort()
# a.reverse()
# print(a)

# a = ['Life', 'is', 'too', 'short']
# result = ' '.join(a)
# print(result)

# a = (1,2,3)
# a += (4,)
# print(a)

# a = dict()
# print(a)
# a['name'] = 'python'
# print(a)
# a[('a',)] = 'python'
# print(a)
# a[250] = 'python'
# print(a)
# a[[1]] = 'python'
# print(a)

# a = {'A':90, 'B':80, 'C':70}
# result = a['B']
# print(result)

# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# aSet = set(a)
# print(aSet)

# a = b = [1,2,3]
# a[1] = 4
# print(b)

# if True:
#     print(1)
#     print(2)
#         print(3)

# pocket = ['paper', 'cellphone']
# card = True
# if 'money' in pocket:
#     print('택시 타고 간다')
# elif card:
#     print('카드가 있네')
# else:
#     print('걸어가자')

# treeHit = 0
# while treeHit < 10:
#     treeHit += 1
#     print("나무를 %d번 찍었습니다." % treeHit)

#     if treeHit == 10:
#         print("나무가 넘어갑니다.")

# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee -= 1
#     print("남은 커피의 양은 %d개 입니다." % coffee)

#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

# a = 0
# while a < 10:
#     a += 1

#     if a%2 == 0:
#         continue

#     print(a)

# a = 0
# while a < 11:
#     a += 1
#     if a%3 == 0:
#         continue
#     if a < 11:
#         print(a)

# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a:
#     print(first, last)

# marks = [90, 25, 67, 45, 80]
# number = 0
# for m in marks:
#     number += 1
#     if(m > 60):
#         print("%d번 학생은 합격입니다." % number)
#     else:
#         print("%d번 학생은 불합격입니다." % number)

# for r in range(5, 10):
#     print(r)

# sum = 0
# for r in range(101):
#     sum += r
# print(sum)

# for i in range(2,10):
#     print("%d단" % i)
#     for j in range(1,10):
#         print("%d * %d = %d" % (i, j, i*j))

# a = [1,2,3]
# result = []
# for n in a:
#     result.append(n * 3)
# print(result)

# a = [1,2,3]
# result = [n * 3 for n in a]
# print(result)

