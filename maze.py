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

# 得点
score = 0

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def print_score():
    global score
    print(f"SCORE: {score}")
    print("")

def print_current(dec):
    """現在位置の表示"""
    dec_str = f"    {dec}    "
    dec_str_width = len(dec_str)
    under_line = "".rjust(dec_str_width, "-")
    print(dec_str)
    print(under_line)
    print("")

def choice_next():
    """次の目的地の表示"""

    global dec
    global score

    while True:
        print("Please enter a left number:")

        next_list = [0]

        if dec != 4 and dec != 7:
            next = (dec - 1 ) // 3
            if next != 1 and next != 4 and next != 7 and next % 2 == 1:
                next_list.append(next)
                end = len(next_list)
                print(f"{end-1}: {next_list[end-1]}")

            next = dec * 2
            for i in range(0,9):
                next *= 2
                next_list.append(next)
                end = len(next_list)
                print(f"{end-1}: {next_list[end-1]}")

        print(f"g: goal")
        print("")

        choice = input()
        if is_integer(choice):
            choice = int(choice)
            if 1 <= choice and choice < 10:
                dec = next_list[choice]

                # 奇数なら得点
                if dec % 2 == 1:
                    score += 1

                break

while True:
    print_score()
    print_current(dec)
    choice_next()
