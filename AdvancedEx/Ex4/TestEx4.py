# Testing Ex4: cố định phép nhân (randoms) và thời gian trả lời (times)
from test_helper import run_program, check

results = []
# 5 câu như sách: randoms có cặp chứa số 5 để kiểm tra bảng 5 bị bỏ qua
results.append(check("Test - 5 câu, có cặp (5, 7) phải bị bỏ qua",
                run_program("Ex4.py", ["5", "12", "35", "64", "20", "81"],
                    randoms=[3, 4, 5, 7, 7, 5, 6, 7, 8, 8, 4, 6, 9, 9],
                    times=[0, 3, 10, 12, 20, 21, 30, 38, 40, 41]),
                ["3 X 4?", "6 X 7?", "8 X 8?", "4 X 6?", "9 X 9?",
                "total response 5, correct 3 times"],
                ["5 X 7?", "7 X 5?"]))
# Debug
results.append(check("Debug 1 - nhập số câu -1 / chữ phải hỏi lại (trước đây lặp vô hạn)",
                run_program("Ex4.py", ["-1", "abc", "1", "12"], randoms=[3, 4], times=[0, 2]),
                ["total response 1, correct 1 times"]))
results.append(check("Debug 2 - trả lời bằng chữ tính là sai, không crash",
                run_program("Ex4.py", ["1", "hai muoi"], randoms=[4, 6], times=[0, 2]),
                ["Wrong! 4 X 6 = 24", "total response 1, correct 0 times"]))
print("=" * 70)
print("TONG KET: %d/%d test case PASS" % (results.count(True), len(results)))
