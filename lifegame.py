import os
import numpy as np

# 環境変数
RADIX = int(os.getenv("RADIX", 2))

count_str = ""
radix_str = ""
dec_str = ""
# 桁揃えに利用。10進数27 を指定したときの見やすさをデフォルトにするぜ（＾～＾）
count_width = 3
width = 15
# 計算回数
count = 0

def update_print_number(dec):
    global count_str
    global radix_str
    global dec_str
    global count_width
    global width
    global count
    global RADIX

    count_str = f"{count}"
    radix_number = np.base_repr(dec, RADIX)
    radix_str = f"{radix_number}"

    # 桁数の更新
    # めんどくさいんで一気に足すぜ（＾～＾）
    if count_width < len(count_str):
        count_width += 5
    if width < len(radix_str):
        width += 5

    count_str = count_str.rjust(count_width)
    radix_str = radix_str.rjust(width)
    dec_str = str(dec)

    count += 1

def print_number():
    global count_str
    global radix_str
    global dec_str

    print(f"[{count_str}] {radix_str} ({dec_str})")

# 10進数を入力してください。
print(f"RADIX={RADIX}")
print("Please enter a decimal number. Example: 27")

# めんどくさいんで、内部的には10進で計算
dec = int(input())

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
