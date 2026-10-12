# Exercise 3 - Number guessing game machine
# Coder: Hoang Phuong Anh - K244111451
#
# Máy sinh số ngẫu nhiên 1..30, người chơi đoán trong giới hạn số lần.
# Đoán đúng trong giới hạn -> giới hạn giảm 1 (khó hơn), đoán sai hết lượt -> tăng 1.
import random

print("Let's play a number guessing game with me\n")
print("What's your name?\n")
playerName = input()
limit = 5          # giới hạn số lần đoán của ván đầu
playAgain = 'YES'  # trạng thái chơi tiếp
print("Nice to meet you, " + playerName + ", I have a number between 1 and 30. Guess it\n")

while playAgain == 'YES':
    # [Debug] sinh số mới cho MỖI ván (trước đây chỉ sinh 1 lần ngoài vòng lặp)
    ansNumber = random.randint(1, 30)
    count = 1
    guessNumber = -1
    # [Debug] in đúng số lượt hiện tại (trước đây luôn in "5 times")
    print("You only have to guess", limit, "times")
    while count <= limit and guessNumber != ansNumber:
        strGuess = input("Please enter the guessed number->")
        # [Debug] nhập chữ thì hỏi lại, không tính lượt (trước đây bị crash)
        if not strGuess.isdigit():
            print("Please enter a number between 1 and 30.")
            continue
        guessNumber = int(strGuess)
        if guessNumber == ansNumber:
            break  # đoán đúng -> thoát vòng while bên trong
        elif guessNumber < ansNumber:
            print("The guessed number is less than the number with the computer.")
        else:
            print("The guessed number is greater than the number with the computer.")
        count = count + 1

    if guessNumber == ansNumber:
        print("Congratulations! You got it right after", count, "guesses\n")
        if limit > 1:
            limit = limit - 1
    else:
        print("The number of computers is ", ansNumber)
        limit = limit + 1

    # [Debug] chấp nhận 'yes', 'Yes', 'YES'
    playAgain = input("Shall we play the game again?(YES or NO)\n").strip().upper()
