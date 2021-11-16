#!/usr/bin/python3

for i in range(1, 101):
    if i < 10:
        print("0" + str(i) + ", ", end="")
    else:
        if i < int(str(i % 10) + str(i // 10)) and i != 89:
            print(str(i) + ", ", end="")
        if i == 89:
            print("89")
