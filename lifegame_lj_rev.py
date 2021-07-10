"""
TODO (2021-07-10 sat) ちゃんと作れてるか分かんない（＾～＾）

左寄せ表記（Left justified）
逆順（Reverse）
"""

def search(dec, dec_width, depth, depth_width, bi_count, dec_before_bi):
    """
    dec : int
        数
    dec_width : int
        10進数表示の桁揃え用
    depth : int
        深さ
    depth_width : int
        深さの表示の桁揃え用
    bi_count : int
        2倍した回数（＾～＾）
    dec_before_bi : int
        2倍する前の数（＾～＾）
    """

    if depth == 0:
        return
    
    # めんどくさいんで、２進は文字列で
    count_str = f"{max_depth - depth}"
    bin = f"{dec:b}"

    # 桁数の更新
    # めんどくさいんで一気に足すぜ（＾～＾）
    if depth_width < len(count_str):
        depth_width += 5
    if dec_width < len(str(dec)):
        dec_width += 5

    # 表示
    count_str = count_str.rjust(depth_width)
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
                return

    search(dec=dec, dec_width=dec_width, depth_width=depth_width, depth=depth-1, bi_count = bi_count, dec_before_bi = dec_before_bi)

# 10進数を入力してください。
print("Please enter a decimal number. Example: 16")

# めんどくさいんで、内部的には10進で計算
dec = int(input())

# 初回表示
print(f"Start {dec:b} ({dec})")

# 打ち止めの深さ
max_depth = 20

search(dec=dec, dec_width=2, depth=max_depth, depth_width=2, bi_count = 0, dec_before_bi = 0)
print(f"Finished")
