# n = int(input("Количество монет:"))
# min = 0
# k = 0
# for i in range(n):
#     x = int(input())
#     if x == 0:
#         k += 1
#         if k > min:
#             min = k
#         else: k = 0
#     if x > 1 or x < 0:
#         print("у монеты всего 2 стороны")
# print("переверните", min)
    


# n = int(input("Введите число:"))
# k = 0
# for i in range(n):
#     x = 2** k
#     k += 1
#     if x < n:
#         print(x)
        


s = int(input("Введите сумму:"))
p = int(input("Введите произведение:"))
x = 0
y = 0
d = 1001
for i in range(d):
    y += 1
    if y * (s - y) == p:
        x = s - y
        print(x, y)
    elif y >= 1002:
        print("Не соответсвует условию")


# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
#     x = int(input())
#     if x == 0:
#         count_zero += 1
#     else:
#         count_one += 1
# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)

    
    
# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1



# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)