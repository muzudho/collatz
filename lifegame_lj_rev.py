"""
TODO (2021-07-10 sat) ちゃんと作れてるか分かんない（＾～＾）

左寄せ表記（Left justified）
逆順（Reverse）
"""

# 10進数を入力してください。
print("Please enter a decimal number. Example: 16")

# めんどくさいんで、内部的には10進で計算
dec = int(input())

# 初回表示
print(f"Start {dec:b} ({dec})")

# 計算回数
count = 0
# 桁揃えに利用
count_width = 2
dec_width = 2

# 2倍した回数（＾～＾）
bi_count = 0
# 2倍する前の数（＾～＾）
dec_before_bi = 0

while count < 20:

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

    #print(f"A ({dec}) {dec:b}")

    if dec % 2 == 1:
        # 奇数なら２倍するぜ（＾～＾）
        dec = dec * 2
        #print(f"B ({dec}) {dec:b}")
    else:
        # 偶数なら 1 引いて 3 で割れるか調べるぜ（＾～＾）
        if (dec - 1) % 3 == 0:
            # じゃあ 1 引いて 3 で割ったろ（＾～＾）
            dec = (dec - 1 ) // 3
            #print(f"C ({dec}) {dec:b}")
        else:
            # ダメなら また、２倍しようぜ（＾～＾）？
            if bi_count == 0:
                dec_before_bi = dec

            if bi_count < 4:
                dec = dec * 2
                #print(f"D ({dec}) {dec:b}")
                bi_count += 1
            else:
                # キリが無いので 2倍 するのは終わり（＾～＾）
                bi_count = 0
                dec = dec_before_bi
                break

    count += 1

print(f"Finished")
