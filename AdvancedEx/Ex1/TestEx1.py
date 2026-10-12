# Testing Ex1: chạy lại 3 test case trong sách + 2 test case debug
from test_helper import run_program, check

results = []
# Test case trong đề: 2 Americano, 2 Latte, 1 Cappuccino, trả 15000 -> thối 1000
results.append(check("Tình huống đề bài (trả 15000)",
                run_program("Ex1.py", ["2", "2", "1", "15000"]),
                ["The total amount is: 14000", "Change is 1000"]))
results.append(check("Test case 1 - tiền trả lớn hơn hoá đơn",
                run_program("Ex1.py", ["2", "2", "1", "24000"]),
                ["The total amount is: 14000", "Change is 10000"]))
results.append(check("Test case 2 - tiền trả nhỏ hơn hoá đơn",
                run_program("Ex1.py", ["3", "4", "2", "23540"]),
                ["The total amount is: 25500", "Not enough money."]))
results.append(check("Test case 3 - tiền trả bằng hoá đơn",
                run_program("Ex1.py", ["1", "2", "3", "17500"]),
                ["The total amount is: 17500", "Change is 0"]))
# Debug
results.append(check("Debug 1 - nhập chữ 'hai' thay vì số",
                run_program("Ex1.py", ["hai"]),
                ["Invalid input"]))
results.append(check("Debug 2 - nhập số ly âm",
                run_program("Ex1.py", ["-2", "1", "1"]),
                ["must not be negative"], ["The total amount"]))
print("=" * 70)
print("TONG KET: %d/%d test case PASS" % (results.count(True), len(results)))
