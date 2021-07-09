"""
左寄せ表記（Left justified）
"""

# 10進数を入力してください。
print("Please enter a decimal number. Example: 27")

# めんどくさいんで、内部的には10進で計算
dec = int(input())

# 初回表示
print(f"Start {dec:b} ({dec})")

# 計算回数
count = 0
# 桁揃えに利用
count_width = 2
dec_width = 2

while True:
    # 奇数になるまで２で割るぜ（＾～＾）
    while dec % 2 == 0:
        dec = dec // 2

    # めんどくさいんで、２進は文字列で
    count_str = f"{count}"
    bin = f"{dec:b}"

    # 桁数の更新
    # めんどくさいんで一気に足すぜ（＾～＾）
    if count_width < len(count_str):
        count_width += 5
    if dec_width < len(str(dec)):
        dec_width += 5

    # 表示
    count_str = count_str.rjust(count_width)
    dec_str = str(dec).rjust(dec_width)
    print(f"[{count_str}] ({dec_str}) {bin}")

    # 1 だったら抜けるぜ（＾～＾）
    if dec==1:
        break

    # 3x+1 するぜ（＾～＾）
    dec = 3 * dec + 1

    count += 1

print(f"Finished")
