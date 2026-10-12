# Testing Ex5: cố định phép nhân (randoms) và thời gian trả lời (times)
from test_helper import run_program, check

results = []
results.append(check("Test case 1 - trả lời đúng nhưng quá 45 giây -> tính sai",
                run_program("Ex5.py", ["1", "42"], randoms=[6, 7], times=[0, 50]),
                ["You took long time", "total response 1, correct 0 times"]))
results.append(check("Test case 2 - phép nhân bị trùng (3 X 4) phải sinh lại",
                run_program("Ex5.py", ["3", "12", "12", "63"],
                    randoms=[3, 4, 3, 4, 4, 3, 9, 7],
                    times=[0, 2, 5, 9, 10, 12]),
                ["3 X 4?", "4 X 3?", "9 X 7?", "total response 3, correct 3 times"]))
# Debug
results.append(check("Debug 1 - nhập 40 câu (> 36 phép nhân) phải hỏi lại",
                run_program("Ex5.py", ["40", "1", "16"], randoms=[4, 4], times=[0, 1]),
                ["(1-36)", "total response 1, correct 1 times"]))
# Hỏi đủ 36 câu: chương trình phải kết thúc, không treo
pairs = [(a, b) for a in (3, 4, 6, 7, 8, 9) for b in (3, 4, 6, 7, 8, 9)]
randoms, answers, times = [], ["36"], []
for k, (a, b) in enumerate(pairs):
    randoms += [a, b]
    answers.append(str(a * b))
    times += [k * 10, k * 10 + 1]
results.append(check("Debug 2 - hỏi đủ 36 phép nhân khác nhau rồi kết thúc",
                run_program("Ex5.py", answers, randoms=randoms, times=times)[-60:],
                ["total response 36, correct 36 times"]))
print("=" * 70)
print("TONG KET: %d/%d test case PASS" % (results.count(True), len(results)))
