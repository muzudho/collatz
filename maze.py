"""
コラッツ予想を 迷路にしたもの（＾～＾）
"""

# タイトル
print("+----------------+")
print("| COLLATZ'S MAZE |")
print("+----------------+")
print("")

# 現在位置
dec = 1

# ツリー・パス
tree_path = [dec]

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def print_tree_path():
    global tree_path

    for i, dec in enumerate(tree_path):
        print(f"{dec}", end="")
        if i<len(tree_path):
            print(f"--", end="")

    print("")
    print("")

# def print_current(dec):
#     """現在位置の表示"""
#     dec_str = f"    {dec}    "
#     dec_str_width = len(dec_str)
#     under_line = "".rjust(dec_str_width, "-")
#     print(dec_str)
#     print(under_line)
#     print("")

def choice_next():
    """次の目的地の表示"""

    global dec

    while True:
        next_list = [0]
        next_width = 0

        if dec != 4 and dec != 7:
            next = (dec - 1 ) // 3
            if next != 1 and next != 4 and next != 7 and next % 2 == 1:
                # 「３で割って１足す」の逆方向へ（＾～＾）
                next_list.append(next)
                next_width = max(next_width, len(str(next)))
            else:
                # 「半分」の逆方向へ（＾～＾）
                next = dec
                for i in range(0,10 - len(next_list)):
                    next *= 2
                    next_list.append(next)
                    next_width = max(next_width, len(str(next)))

        print("Please enter a left number:")
        for i, next in enumerate(next_list):
            if i!=0:
                next_str = str(next_list[i]).rjust(next_width)
                print(f"{i}: {next_str}")

        print(f"g: goal")
        print("")

        choice = input()
        print("")

        if choice == "g":
            # 終わり
            return
        elif is_integer(choice):
            choice = int(choice)
            if 1 <= choice and choice < len(next_list):
                dec = next_list[choice]
                tree_path.append(dec)
                break

while True:
    print_tree_path()
    choice_next()
