a = input("请输入数字：")
print(a)
if a.isdigit():
    d = int(a)
    print(d**2)
else:
    print("您输入的不是数字，请输入数字！")
    