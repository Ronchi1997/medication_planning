#!/usr/bin/python3

dict={
        "早饭前":[],
        "早饭时":[],
        "早饭后":[],
        "午饭前":[],
        "午饭时":[],
        "午饭后":[],
        "晚饭前":[],
        "晚饭时":[],
        "晚饭后":[],
        "睡前":[]
        }

while True:
    name = input("药品名称（输入0退出）：")
    if name == "0":
        break;
    freq = input("用药频率（每日x次）：")
    quantity = input("每次药量（x粒/x片，带上量词）：")
    time = input("用药时间（饭前/饭时/饭后）：")

    if freq == "4":
        prefix=["早","午","晚","睡前"]
    elif freq == "3":
        prefix=["早","午","晚"]
    elif freq == "2":
        prefix=["早","晚"]
    elif freq == "1":
        prefix=["睡前"]
    else:
        print("不正常的频率！")
        continue;

    if time not in ("饭前","饭时","饭后"):
        print("非法输入："+time)
        continue;

    for i in prefix:
        if i == "睡前":
            key = i
        else:
            key = i + time
        value = name + quantity
        dict[key].append(value)

for key in dict.keys():
    if dict[key]:
        print(key+"："+"，".join(dict[key]))
