s=input("请输入一行字符:")
letter count=0
digit count=0
space count=0
other count=0
for char in s:
  if char.isalpha():
    letter count+=1
  elif char.isdigit():
    digit count+=1
  elif char.isspace():
    space count+=1
  else:
    other count+=1
print("英文字符:",letter count)
print("数字:",digit count)
print("空格:",space count)
print("其他字符:",other count)
