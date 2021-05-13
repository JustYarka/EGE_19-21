win = 91

def play19(h, s, c):
    global win
    if s + h >= win and c == 2:
        return True
    elif s + h < win and c == 2:
        return False
    return play19(h, s + 1, c + 1) or play19(h, s * 4, c + 1) or play19(h + 1, s, c + 1) or play19(h * 4, s, c + 1)

def play20(h, s, c):
    global win
    if s + h >= win and c == 3:
        return True
    elif (s + h < win and c == 3) or s + h >= win:
        return False
    elif c % 2 == 0:
        return play20(h, s + 1, c + 1) or play20(h, s * 4, c + 1) or play20(h + 1, s, c + 1) or play20(h * 4, s, c + 1)
    return play20(h, s + 1, c + 1) and play20(h, s * 4, c + 1) and play20(h + 1, s, c + 1) and play20(h * 4, s, c + 1)

def play21(h, s, c):
    global win
    if s + h >= win and (c == 4 or c == 2):
        return True
    elif (s + h < win and c == 4) or s + h >= win:
        return False
    elif c % 2 == 1:
        return play21(h, s + 1, c + 1) or play21(h, s * 4, c + 1) or play21(h + 1, s, c + 1) or play21(h * 4, s, c + 1)
    return play21(h, s + 1, c + 1) and play21(h, s * 4, c + 1) and play21(h + 1, s, c + 1) and play21(h * 4, s, c + 1)    

mins, maxs = 1, 85
h1 = 5

for i in range(mins, maxs):
    if play19(h1, i, 0):
        print(i)
        break
print()

cnt = 2
for i in range(mins, maxs):
    if play20(h1, i, 0):
        print(i)
        cnt -= 1
        if cnt == 0:
            break
print()

for i in range(mins, maxs):
    if play21(h1, i, 0):
        print(i)
        break    