# Exercise 4 - Multiplication table game machine
# Coder: Hoang Phuong Anh - K244111451
#
# Máy ra phép nhân ngẫu nhiên (bỏ bảng 2 và 5, nên lấy số từ 3 đến 9 trừ 5),
# đo thời gian trả lời bằng time.time(), đếm số câu đúng/sai.
import random
import time

correctAns = 0  # số câu đúng
wrongAns = 0    # số câu sai

# [Debug] số câu phải > 0 (trước đây nhập -1 thì vòng while count!=0 chạy mãi)
count = 0
while count <= 0:
    strCount = input("How many times should I do?")
    if strCount.isdigit():
        count = int(strCount)

while count != 0:
    # sinh 2 số từ 3 đến 9
    a = random.randint(3, 9)
    b = random.randint(3, 9)
    # gặp bảng 5 thì sinh lại (continue quay về đầu vòng lặp)
    if a == 5 or b == 5:
        continue

    count = count - 1
    print("%d X %d?" % (a, b))
    startTime = time.time()  # bắt đầu đo thời gian
    strProduct = input()
    endTime = time.time()
    print("I answered in seconds %1.f " % (endTime - startTime))

    # [Debug] nhập chữ thì tính là sai (trước đây bị crash)
    if strProduct.strip().isdigit() and int(strProduct) == a * b:
        correctAns = correctAns + 1
        print("Right!\n")
    else:
        wrongAns = wrongAns + 1
        print("Wrong! %d X %d = %d\n" % (a, b, a * b))

print("total response %d, correct %d times"
      % (correctAns + wrongAns, correctAns))
