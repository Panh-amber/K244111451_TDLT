# Testing Ex3: cố định số bí mật bằng randoms để test lặp lại được
from test_helper import run_program, check

results = []
# Test case 1 trong sách: số bí mật 9, đoán theo tìm kiếm nhị phân 15 -> 7 -> 11 -> 9
results.append(check("Test case 1 - đoán theo tìm kiếm nhị phân (số bí mật = 9)",
                run_program("Ex3.py", ["An", "15", "7", "11", "9", "NO"], randoms=[9]),
                ["greater", "less", "after 4 guesses"]))
# Test case 2 trong sách: đoán lung tung 5 lần đều sai
results.append(check("Test case 2 - đoán sai cả 5 lần",
                run_program("Ex3.py", ["An", "1", "2", "3", "4", "5", "NO"], randoms=[20]),
                ["The number of computers is  20"]))
# Debug
results.append(check("Debug 1 - chơi lại phải có SỐ MỚI và lượt giảm còn 4",
                run_program("Ex3.py", ["An", "9", "YES", "9", "25", "NO"], randoms=[9, 25]),
                ["You only have to guess 5 times", "You only have to guess 4 times",
                "The guessed number is less", "after 2 guesses"]))
results.append(check("Debug 2 - thua thì lượt tăng lên 6, gõ 'yes' thường vẫn chơi tiếp",
                run_program("Ex3.py", ["An", "1", "1", "1", "1", "1", "yes", "7", "no"], randoms=[30, 7]),
                ["You only have to guess 6 times"]))
results.append(check("Debug 3 - nhập chữ không bị crash và không mất lượt",
                run_program("Ex3.py", ["An", "abc", "12", "no"], randoms=[12]),
                ["Please enter a number", "after 1 guesses"]))
print("=" * 70)
print("TONG KET: %d/%d test case PASS" % (results.count(True), len(results)))
