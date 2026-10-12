import io
import os
import runpy
from contextlib import redirect_stdout
from unittest import mock

FOLDER = os.path.dirname(os.path.abspath(__file__))


def run_program(file_name, inputs, randoms=None, times=None):
    """Chạy chương trình, tự động gõ các giá trị trong inputs thay cho bàn phím.
    randoms: các số mà random.randint sẽ trả về (để test không phụ thuộc may rủi)
    times  : các giá trị mà time.time() sẽ trả về (để giả lập thời gian trả lời)
    Trả về toàn bộ nội dung hiện trên màn hình."""
    screen = io.StringIO()
    answers = iter(inputs)

    def fake_input(prompt=""):
        value = next(answers)
        print(prompt + value)  # in lại giống như người dùng gõ trên console
        return value

    patches = [mock.patch("builtins.input", fake_input)]
    if randoms is not None:
        patches.append(mock.patch("random.randint", side_effect=randoms))
    if times is not None:
        patches.append(mock.patch("time.time", side_effect=times))
    for p in patches:
        p.start()
    try:
        with redirect_stdout(screen):
            runpy.run_path(os.path.join(FOLDER, file_name), run_name="__main__")
    finally:
        for p in patches:
            p.stop()
    return screen.getvalue()


def check(test_name, output, expected, not_expected=()):
    """In kết quả chạy và kết luận PASS / FAIL."""
    ok = all(text in output for text in expected) and \
        not any(text in output for text in not_expected)
    print("=" * 70)
    print(test_name)
    print("-" * 70)
    print(output.rstrip())
    print("-" * 70)
    print("KET QUA:", "PASS" if ok else "FAIL")
    return ok
