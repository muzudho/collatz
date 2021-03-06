"""
左寄せ表記（Left justified）
"""

import os
import numpy as np

# 環境変数
RADIX = int(os.getenv("RADIX", 2))

# 桁揃えに利用。10進数27 を指定したときの見やすさをデフォルトにするぜ（＾～＾）
count_width = 3
count_str = ""
dec_width = 4
dec_str = ""
radix_str = ""
# 表示した数の個数
count = 0

def update_print_number(dec):
    """表示するテキストの更新"""
    global count_width
    global count_str
    global dec_width
    global dec_str
    global radix_str
    global count
    global RADIX

    count_str = f"{count}"

    # 桁数の更新
    if count_width < len(count_str):
        count_width += 1
    if dec_width < len(str(dec)):
        dec_width += 1

    count_str = count_str.rjust(count_width)
    radix_str = str(np.base_repr(dec, RADIX))
    dec_str = str(dec).rjust(dec_width)
    count += 1

def print_number():
    """表示"""
    global count_str
    global dec_str
    global radix_str

    print(f"[{count_str}] ({dec_str}) {radix_str}")

# 数を入力してください。
print(f"RADIX={RADIX}")
print("Please enter a number.")
print("Example 1: 27")
print("Example 2: 0b11011")

# めんどくさいんで、内部的には10進で計算
number_str = input()

if number_str.startswith("0b"):
    radix_str = number_str[2:]
    dec = int(radix_str, 2) # 2進数で入力されたものを10進に変換
else:
    dec = int(number_str) # 10進数

# 初回表示
print(f"Start")
update_print_number(dec)
print_number()

while True:
    # 奇数になるまで２で割るぜ（＾～＾）
    while dec % 2 == 0:
        dec = dec // 2

        # 表示
        # TODO 偶数なんで省くオプションとか欲しい（＾～＾）
        update_print_number(dec)
        print_number()

    # 1 だったら抜けるぜ（＾～＾）
    if dec==1:
        break

    # 3x+1 するぜ（＾～＾）
    dec = 3 * dec + 1

    # 表示
    update_print_number(dec)
    print_number()

print(f"Finished")
