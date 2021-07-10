"""
TODO (2021-07-10 sat) ちゃんと作れてるか分かんない（＾～＾）

左寄せ表記（Left justified）
逆順（Reverse）
"""

def search(dec, depth, bi_count):
    """
    dec : int
        数
    depth : int
        深さ
    bi_count : int
        2倍した回数（＾～＾）
    """

    if depth == 0:
        return
    
    # めんどくさいんで、２進は文字列で
    bin = f"{dec:b}"

    # 深さだけインデントしようぜ（＾～＾）？
    indent = ""
    for i in range(0, max_depth-depth):
        indent += " "

    # 表示
    print(f"{indent}({dec}) {bin}")

    #print(f"A ({dec}) {dec:b}")

    # 偶数なら 1 引いて 3 で割れるか調べるぜ（＾～＾）
    if (dec - 1) % 3 == 0:
        # じゃあ 1 引いて 3 で割ったろ（＾～＾）
        dec = (dec - 1 ) // 3
        #print(f"C ({dec}) {dec:b}")
        search(dec=dec, depth=depth-1, bi_count = 0)

    else:
        # キリが無いので 2倍 するのは終わり（＾～＾）
        if 4 < bi_count:
            # 掘るの終わり
            return

        # ダメなら ２倍しようぜ（＾～＾）？
        dec = dec * 2
        #print(f"D ({dec}) {dec:b}")

        search(dec=dec, depth=depth-1, bi_count = bi_count+1)

        # ４倍して探索してもいいのでは（＾～＾）？
        dec = dec * 2
        #print(f"E ({dec}) {dec:b}")

        search(dec=dec, depth=depth-1, bi_count = bi_count+1)

    # 掘るの終わり
    return

# 10進数を入力してください。
print("Please enter a decimal number. Example: 8")

# めんどくさいんで、内部的には10進で計算
dec = int(input())

# 初回表示
print(f"Start {dec:b} ({dec})")

# 打ち止めの深さ
max_depth = 5

search(dec=dec, depth=max_depth, bi_count = 0)
print(f"Finished")
