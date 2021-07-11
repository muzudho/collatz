"""
コラッツ予想を 迷路にしたもの（＾～＾）
"""

# タイトル
print("+----------------+")
print("| COLLATZ'S MAZE |")
print("+----------------+")
print("")

# 現在位置
dec = 4

def print_current(dec):
    """現在位置の表示"""
    dec_str = f"    {dec}    "
    dec_str_width = len(dec_str)
    under_line = "".rjust(dec_str_width, "-")
    print(dec_str)
    print(under_line)
    print("")

def print_next(dec):
    """次の目的地の表示"""
    print("Please enter a left number:")

    number = 1

    if 4 < dec and dec != 7 and ((dec - 1) // 3) % 2 == 1:
        next = (dec - 1 ) // 3
        print(f"{number}: {next}")

    next = dec * 2
    for i in range(0,9):
        print(f"{number}: {next}")
        next *= 2
        number += 1

print_current(dec)
print_next(dec)