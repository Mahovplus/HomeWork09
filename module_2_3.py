my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while True:
 for a in my_list:
    if my_list.__len__() < a:
        print(a)
    continue
 break

