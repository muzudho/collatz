# 10進数を入力してください。
print("Please enter a decimal number. Example: 31")

# めんどくさいんで、内部的には10進で計算
dec = int(input())

# 初回表示
print(f"Start")

# 計算回数
count = 0
# 桁揃えに利用
width = 10

while True:
    # 奇数になるまで２で割るぜ（＾～＾）
    while dec % 2 == 0:
        dec = dec // 2

    # めんどくさいんで、２進は文字列で
    bin = f"{dec:b}"

    # 桁数の更新
    if width < len(bin):
        # めんどくさいんで一気に足すぜ（＾～＾）
        width += 5

    # 表示
    bin = bin.rjust(width)
    print(f"[{count}] {bin} ({dec})")

    # 1 だったら抜けるぜ（＾～＾）
    if dec==1:
        break

    # 3x+1 するぜ（＾～＾）
    dec = 3 * dec + 1

    count += 1

print(f"Finished")
