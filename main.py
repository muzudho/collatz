# 10進数を入力してください。
print("Please enter a decimal number. Example: 31")
dec = int(input())

count = 0

# めんどくさいんで、1 になるまでループ（＾～＾）
while dec!=1:
    print(f"[{count}]")

    # めんどくさいんで、内部的には10進で計算
    dec2 = 2*dec
    dec21 = dec2+1
    dec3 = dec2+dec
    dec31 = dec3+1

    # 桁ぞろえが めんどくさいんで、2進数の文字列を生成
    bin31 = f"{dec31:b}"
    width = len(bin31)
    bin21 = f"{dec21:b}".rjust(width)
    bin = f"{dec:b}".rjust(width)
    line = f"".rjust(width,"-")

    # 表示
    print(f"+ {bin} ({dec})")
    print(f"  {bin21} ({dec21})")
    print(f"--{line}")
    print(f"  {bin31} ({dec31})")

    # 奇数になるまで２で割るぜ（＾～＾）
    while dec31 % 2 == 0:
        dec31 = dec31 // 2
    dec = dec31
    
    count += 1

# 最後に 1 を表示するだけ（＾～＾）
print(f"\nFinish {dec:b} ({dec})")
