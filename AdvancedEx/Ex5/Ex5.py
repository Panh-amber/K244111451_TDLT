# Exercise 5 - Multiplication table game machine (improve)
# Coder: Hoang Phuong Anh - K244111451
#
# Cải tiến Ex4:
#  - Không hỏi lại phép nhân đã hỏi (lưu a, b đã ra vào 2 list)
#  - Trả lời quá 45 giây thì tính là sai
import random
import time

correctAns = 0       # số câu đúng
wrongAns = 0         # số câu sai
duplicateListA = []  # các số a đã ra
duplicateListB = []  # các số b đã ra (cùng vị trí với a)
limitTime = 45       # giới hạn thời gian trả lời (giây)

# [Debug] chỉ có 6 x 6 = 36 phép nhân khác nhau (a, b thuộc 3,4,6,7,8,9)
# nếu hỏi hơn 36 câu thì không thể sinh câu mới -> trước đây bị lặp vô hạn
maxQuestion = 36
count = 0
while count <= 0 or count > maxQuestion:
    strCount = input("How many times should I do?(1-%d)" % maxQuestion)
    if strCount.isdigit():
        count = int(strCount)
    else:
        count = 0

while count != 0:
    a = random.randint(3, 9)
    b = random.randint(3, 9)
    if a == 5 or b == 5:
        continue
    # kiểm tra phép nhân a x b đã hỏi chưa
    isDuplicated = False
    for i in range(len(duplicateListA)):
        if duplicateListA[i] == a and duplicateListB[i] == b:
            isDuplicated = True
            break
    if isDuplicated == True:
        continue  # đã hỏi rồi -> sinh số khác
    else:
        duplicateListA.append(a)
        duplicateListB.append(b)

    count = count - 1
    print("%d X %d?" % (a, b))
    startTime = time.time()
    strProduct = input()
    endTime = time.time()
    calculateTime = endTime - startTime
    print("I answered in seconds %1.f " % calculateTime)
    if calculateTime > limitTime:
        print("You took long time to answer, limit time is ", limitTime,
              " second you answered in %1.f second" % calculateTime)

    # [Debug] nhập chữ thì tính là sai (trước đây bị crash)
    isRight = strProduct.strip().isdigit() and int(strProduct) == a * b
    if isRight and calculateTime <= limitTime:
        correctAns = correctAns + 1
        print("Right!\n")
    else:
        wrongAns = wrongAns + 1
        print("Wrong! %d X %d = %d\n" % (a, b, a * b))

print("total response %d, correct %d times"
      % (correctAns + wrongAns, correctAns))
