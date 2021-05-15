win = 91

# 1 heap
def play19_1(s, c):
    global win
    if s >= win and c == 2:
        return True
    elif s < win and c == 2:
        return False
    return play19_1(s + 1, c + 1) or play19_1(s * 4, c + 1)

def play20_1(s, c):
    global win
    if s >= win and c == 3:
        return True
    elif (s< win and c == 3) or s >= win:
        return False
    elif c % 2 == 0:
        return play20_1(s + 1, c + 1) or play20_1(s * 4, c + 1)
    return play20_1(s + 1, c + 1) and play20_1(s * 4, c + 1)

def play21_1(s, c):
    global win
    if s >= win and (c == 4 or c == 2):
        return True
    elif (s < win and c == 4) or s >= win:
        return False
    elif c % 2 == 1:
        return play21_1(s + 1, c + 1) or play21_1(s * 4, c + 1)
    return play21_1(s + 1, c + 1) and play21_1(s * 4, c + 1)


# 2 heaps
def play19_2(h, s, c):
    global win
    if s + h >= win and c == 2:
        return True
    elif s + h < win and c == 2:
        return False
    return play19_2(h, s + 1, c + 1) or play19_2(h, s * 4, c + 1) or play19_2(h + 1, s, c + 1) or play19_2(h * 4, s, c + 1)

def play20_2(h, s, c):
    global win
    if s + h >= win and c == 3:
        return True
    elif (s + h < win and c == 3) or s + h >= win:
        return False
    elif c % 2 == 0:
        return play20_2(h, s + 1, c + 1) or play20_2(h, s * 4, c + 1) or play20_2(h + 1, s, c + 1) or play20_2(h * 4, s, c + 1)
    return play20_2(h, s + 1, c + 1) and play20_2(h, s * 4, c + 1) and play20_2(h + 1, s, c + 1) and play20_2(h * 4, s, c + 1)

def play21_2(h, s, c):
    global win
    if s + h >= win and (c == 4 or c == 2):
        return True
    elif (s + h < win and c == 4) or s + h >= win:
        return False
    elif c % 2 == 1:
        return play21_2(h, s + 1, c + 1) or play21_2(h, s * 4, c + 1) or play21_2(h + 1, s, c + 1) or play21_2(h * 4, s, c + 1)
    return play21_2(h, s + 1, c + 1) and play21_2(h, s * 4, c + 1) and play21_2(h + 1, s, c + 1) and play21_2(h * 4, s, c + 1)    


# Example for 2 heaps
mins, maxs = 1, 85
h1 = 5

for i in range(mins, maxs):
    if play19_2(h1, i, 0):
        print(i)
        break
print()

cnt = 2
for i in range(mins, maxs):
    if play20_2(h1, i, 0):
        print(i)
        cnt -= 1
        if cnt == 0:
            break
print()

for i in range(mins, maxs):
    if play21_2(h1, i, 0):
        print(i)
        break    
