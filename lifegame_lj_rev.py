"""
TODO (2021-07-10 sat) ちゃんと作れてるか分かんない（＾～＾）

左寄せ表記（Left justified）
逆順（Reverse）
"""

def search(dec, depth, breadth, bi_count):
    """
    dec : int
        数
    depth : int
        深さ
    breadth : int
        幅
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
        indent += "  "

    # 表示
    print(f"{indent}({dec}) {bin}")

    #print(f"A ({dec}) {dec:b}")

    if dec == 4:
        # 4から1に循環するので終わり（＾～＾）
        return

    # 1 引いて 3 で割れるか調べるぜ（＾～＾）
    if (dec - 1) % 3 == 0:
        # じゃあ 1 引いて 3 で割ったろ（＾～＾）
        dec = (dec - 1 ) // 3
        #print(f"C ({dec}) {dec:b}")
        search(dec=dec, depth=depth-1, breadth=breadth, bi_count = 0)

    # 2倍を何回かやるのも試すぜ（＾～＾）
    if 4 < bi_count:
        # キリが無いので 2倍 するのは終わり（＾～＾）
        # 掘るの終わり
        return

    # ２倍しようぜ（＾～＾）？
    for i in range(0, breadth):
        dec = dec * 2
        #print(f"D ({dec}) {dec:b}")

        search(dec=dec, depth=depth-1, breadth=breadth, bi_count = bi_count+1)

    # 掘るの終わり
    return

# 10進数、深さと幅を入力してください。
print("Please enter a decimal number, depth and breadth. Example: 8 4 6")

# めんどくさいんで、内部的には10進で計算
dec, max_depth, breadth = input().split()
dec = int(dec) # 10進数
max_depth = int(max_depth) # 打ち止めの深さ
breadth = int(breadth) # 探索の木の幅

# 初回表示
print(f"Start {dec:b} ({dec})")

search(dec=dec, depth=max_depth, breadth=breadth, bi_count = 0)
print(f"Finished")
