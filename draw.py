# import math
#
#
# class Circle:
#
#     def __init__(self, r):
#         self.r = r
#
#     def gets(self):
#         return math.pi*self.r**2
#
#     def draw(self, c='o'):
#         ss = 0
#         for i in range(int(2 * self.r)):
#             for j in range(int(2 * self.r)):
#                 d = ((self.r - i) ** 2 + (self.r - j) ** 2) ** 0.5
#                 if d <= self.r:
#
#                     print(c, end='')
#                     ss += 1
#                 else:
#                     print(' ', end='')
#             print('')
#         s = math.pi * (self.r ** 2)
#
#
# S1=Circle(5.5)
# S2=Circle(3.5)
#
# print(S1.gets(), S2.gets())
# c=input()
# S1.draw(c)
# S2.draw()
#
# class Rect:
#
#     def __init__(self, a, b):
#         self.a=a
#         self.b=b
#
#     def gets(self):
#         return self.a*self.b
#
#     def draw(self):
#         or i in range(a):
#         for j in range(b):
#
#             if d <= r:
#                 print('o', end='')
#                 ss += 1
#             else:
#                 print(' ', end='')
#         print('')

# class Trng:
#     def __init__(self, a):
#         self.a=a
#
#     def gets(self):
#         return (self.a**2)/2
#
#     def draw(self):
#         for i in range(self.a):
#             for j in range(i+1):
#                 print('o', end='')
#             print('')
# t = Trng(10)
# t.draw()



