"""
TODO (2021-07-10 sat) ちゃんと作れてるか分かんない（＾～＾）
FIXME (2021-07-11 sun) `7 7 2` で探索したら 37 から 12 が生えていておかしい（＾～＾）

左寄せ表記（Left justified）
逆順（Reverse）
"""

import os
import numpy as np

# 環境変数
RADIX = int(os.getenv("RADIX", 2))
BREADTH = int(os.getenv("BREADTH", 4)) # 探索の木の幅
DEPTH = int(os.getenv("DEPTH", 8)) # 探索の木の深さ

numbers = set()

# Return code
END_NORMAL = 0
END_DUPURICATE = 1
END_CUTOFF4 = 2
END_BI = 4
END_DEPTH = 5

# 探索の種類
SEARCH_NORMAL = 0
SEARCH_EVEN = 1

# 表示用
radix_str = ""
dec_str = ""
indent = ""

def update_print_number(dec, depth):
    global radix_str
    global dec_str
    global numbers
    global DEPTH
    global indent

    # 深さだけインデントしようぜ（＾～＾）？
    indent = ""
    for i in range(0, DEPTH-depth):
        indent += "  "

    radix_str = str(np.base_repr(dec, RADIX))

    # 重複した枝とか見たくないんで（＾～＾）
    if dec in numbers:
        radix_str = f"{radix_str} is a dupricate"

    elif dec == 4:
        # 4から1に循環するので終わり（＾～＾）
        radix_str = f"{radix_str} is an edge case"

    elif dec == 7:
        # 7 から 1 引いて 3 で割ったら 2 だが、2 から 7 は生えないぜ（＾～＾）？
        # なんだかおかしいから飛ばそ（＾～＾）
        radix_str = f"{radix_str} is an edge case"

    dec_str = str(dec)

def print_number():
    global radix_str
    global dec_str
    global indent

    print(f"{indent}({dec_str}) {radix_str}")

def search(dec, depth, search_type):
    """
    Parameters
    ----------
    dec : int
        数
    depth : int
        深さ
    search_type: int
        探索の種類（＾～＾）

    Returns
    -------
    int
        0: 正常終了
        1: 重複をカット
        2: '4'をカット
        4: 2倍を終了
        5: 深さが末端
    """

    if depth == 0:
        return END_DEPTH

    # 表示
    update_print_number(dec, depth)
    print_number()

    # 重複した枝とか見たくないんで（＾～＾）
    if dec in numbers:
        return END_DUPURICATE

    numbers.add(dec)

    if dec == 4:
        # 4から1に循環するので終わり（＾～＾）
        return END_CUTOFF4

    #print(f"A ({dec}) {dec:b}")

    # 割り切れることのチェック（＾～＾）
    if (dec - 1) % 3 == 0:
        if dec == 7:
            # 7 から 1 引いて 3 で割ったら 2 だが、2 から 7 は生えないぜ（＾～＾）？
            # なんだかおかしいから飛ばそ（＾～＾）
            pass
        elif ((dec - 1) // 3) % 2 == 1:
            # 奇数であることのチェック（＾～＾）
            # じゃあ 1 引いて 3 で割ったろ（＾～＾）
            dec = (dec - 1 ) // 3
            #print(f"C ({dec}) {dec:b}")

            search(dec=dec, depth=depth-1, search_type=SEARCH_NORMAL)

    if search_type != SEARCH_EVEN:
        for i in range(0, BREADTH):
            # 重複していなければ、２倍しようぜ（＾～＾）？
            if dec * 2 in numbers:
                break

            dec = dec * 2
            #print(f"D ({dec}) {dec:b}")

            ret_code = search(dec=dec, depth=depth, search_type=SEARCH_EVEN)
            if ret_code == END_DUPURICATE:
                # 重複の枝なら、さっさと終わろ（＾～＾）
                break

    # 掘るの終わり
    return END_NORMAL

# 数、深さと幅を入力してください。
print(f"RADIX={RADIX}")
print(f"BREADTH={BREADTH}")
print(f"DEPTH={DEPTH}")
print("Please enter a number.")
print("Example 1: 8")
print("Example 2: 0b1000")

# めんどくさいんで、内部的には10進で計算
number_str = input()

if number_str.startswith("0b"):
    bin_str = number_str[2:]
    dec = int(bin_str, 2) # 2進数で入力されたものを10進に変換
else:
    dec = int(number_str) # 10進数

# 初回表示
print(f"Start {dec:b} ({dec})")

search(dec=dec, depth=DEPTH, search_type=SEARCH_NORMAL)
print(f"Finished")
