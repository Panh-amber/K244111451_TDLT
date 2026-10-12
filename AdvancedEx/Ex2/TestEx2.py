# Testing Ex2: test case theo mô tả trong sách + test case debug
from test_helper import run_program, check

results = []
results.append(check("Test 1 - menu tự sinh theo list, chọn 1 món, trả đúng tiền",
                run_program("Ex2.py", ["1", "2", "no", "5000"]),
                ["1    Americano", "6    Grapefruit", "[1-6]",
                "The total amount is: 5000", "Paid is successfully!"],
                ["Change is"]))
results.append(check("Test 2 - chọn ngoài 1..6 / chữ / số lượng 0 -> phải hỏi lại",
                run_program("Ex2.py", ["9", "abc", "0", "2", "0", "x", "3", "no", "9000"]),
                ["Café Latte", "The total amount is: 9000"]))
results.append(check("Test 3 - nhiều món, trả thiếu rồi trả dư (giống ví dụ sách: thối 500)",
                run_program("Ex2.py", ["1", "1", "yes", "2", "2", "yes", "4", "1", "no","10000", "13000"]),
                ["The total amount is: 12500", "Not enough money",
                "Paid is successfully!", "Change is 500"]))
results.append(check("Test 4 - nhập tiền không hợp lệ (chữ, số âm)",
                run_program("Ex2.py", ["4", "1", "no", "abc", "-5", "4000"]),
                ["abc  is not valid", "-5  is not valid", "Paid is successfully!"]))
# Debug
results.append(check("Debug 1 - gõ 'No' viết hoa phải dừng chọn món",
                run_program("Ex2.py", ["1", "2", "No", "5000"]),
                ["The total amount is: 5000"]))
out = run_program("Ex2.py", ["1", "2", "yes", "1", "1", "no", "7500"])
results.append(check("Debug 2 - chọn Americano 2 lần phải gộp thành 1 dòng số lượng 3",
                out, ["Americano       2500         3      7500"]))
print("=" * 70)
print("TONG KET: %d/%d test case PASS" % (results.count(True), len(results)))
