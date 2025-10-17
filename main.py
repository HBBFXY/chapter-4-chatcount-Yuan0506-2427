import string

s = input("请输入一行字符:")
letter_count = 0
digit_count = 0
space_count = 0
other_count = 0

for char in s:
    if char in string.ascii_letters:
        letter_count += 1
    elif char in string.digits:
        digit_count += 1
    elif char.isspace():
        space_count += 1
    else:
        other_count += 1

print("英文字符:", letter_count)
print("数字:", digit_count)
print("空格:", space_count)
print("其他:", other_count)
