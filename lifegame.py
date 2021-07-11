count_str = ""
bin_str = ""
dec_str = ""
# 桁揃えに利用
count_width = 2
width = 15

def update_print_number(dec):
    global count_str
    global bin_str
    global dec_str
    global count_width
    global width
    global count

    # めんどくさいんで、２進は文字列で
    count_str = f"{count}"
    bin_str = f"{dec:b}"

    # 桁数の更新
    # めんどくさいんで一気に足すぜ（＾～＾）
    if count_width < len(count_str):
        count_width += 5
    if width < len(bin_str):
        width += 5

    count_str = count_str.rjust(count_width)
    bin_str = bin_str.rjust(width)
    dec_str = str(dec)

    count += 1

def print_number():
    global count_str
    global bin_str
    global dec_str

    print(f"[{count_str}] {bin_str} ({dec})")

# 10進数を入力してください。
print("Please enter a decimal number. Example: 27")

# めんどくさいんで、内部的には10進で計算
dec = int(input())

# 初回表示
print(f"Start {dec:b} ({dec})")

# 計算回数
count = 0

while True:
    # 奇数になるまで２で割るぜ（＾～＾）
    while dec % 2 == 0:
        dec = dec // 2

    # 表示
    update_print_number(dec)
    print_number()

    # 1 だったら抜けるぜ（＾～＾）
    if dec==1:
        break

    # 3x+1 するぜ（＾～＾）
    dec = 3 * dec + 1

print(f"Finished")
