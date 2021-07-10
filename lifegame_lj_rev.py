"""
TODO (2021-07-10 sat) ちゃんと作れてるか分かんない（＾～＾）

左寄せ表記（Left justified）
逆順（Reverse）
"""

numbers = set()

# Return code
END_NORMAL = 0
END_DUPURICATE = 1
END_CUTOFF4 = 2
END_CUTOFF7 = 3
END_BI = 4
END_DEPTH = 5

def search(dec, depth, breadth, bi_count):
    """
    Parameters
    ----------
    dec : int
        数
    depth : int
        深さ
    breadth : int
        幅
    bi_count : int
        2倍した回数（＾～＾）

    Returns
    -------
    int
        0: 正常終了
        1: 重複をカット
        2: '4'をカット
        3: '7'をカット
        4: 2倍を終了
        5: 深さが末端
    """

    if depth == 0:
        return END_DEPTH

    # 深さだけインデントしようぜ（＾～＾）？
    indent = ""
    for i in range(0, max_depth-depth):
        indent += "  "

    # 重複した枝とか見たくないんで（＾～＾）
    if dec in numbers:
        print(f"{indent}{dec} is a dupricate")
        return END_DUPURICATE

    numbers.add(dec)

    if dec == 4:
        # 4から1に循環するので終わり（＾～＾）
        print(f"{indent}(4) {4:b} is edge case")
        return END_CUTOFF4

    # 表示
    print(f"{indent}({dec}) {dec:b}")

    #print(f"A ({dec}) {dec:b}")

    # 1 引いて 3 で割れるか調べるぜ（＾～＾）
    if (dec - 1) % 3 == 0:
        # 7 から 1 引いて 3 で割ったら 2 だが、2 から 7 は生えないぜ（＾～＾）？
        if dec == 7:
            # なんだかおかしいから抜けよ（＾～＾）
            print(f"{indent}Edge case: 7 is cutoff")
            return END_CUTOFF7

        # じゃあ 1 引いて 3 で割ったろ（＾～＾）
        dec = (dec - 1 ) // 3
        #print(f"C ({dec}) {dec:b}")

        search(dec=dec, depth=depth-1, breadth=breadth, bi_count = 0)

    # 2倍を何回かやるのも試すぜ（＾～＾）
    if 4 < bi_count:
        # キリが無いので 2倍 するのは終わり（＾～＾）
        # 掘るの終わり
        return END_BI

    # ２倍しようぜ（＾～＾）？
    for i in range(0, breadth):
        dec = dec * 2
        #print(f"D ({dec}) {dec:b}")

        ret_code = search(dec=dec, depth=depth-1, breadth=breadth, bi_count = bi_count+1)
        if ret_code == END_DUPURICATE:
            # 重複の枝なら、さっさと終わろ（＾～＾）
            break

    # 掘るの終わり
    return END_NORMAL

# 10進数、深さと幅を入力してください。
print("Please enter a decimal number, depth and breadth. Example: 8 7 2")

# めんどくさいんで、内部的には10進で計算
dec, max_depth, breadth = input().split()
dec = int(dec) # 10進数
max_depth = int(max_depth) # 打ち止めの深さ
breadth = int(breadth) # 探索の木の幅

# 初回表示
print(f"Start {dec:b} ({dec})")

search(dec=dec, depth=max_depth, breadth=breadth, bi_count = 0)
print(f"Finished")
