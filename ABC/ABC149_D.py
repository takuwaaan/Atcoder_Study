n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

def janken_win(vs):
    if vs == "r":
        return p
    elif vs == "s":
        return r
    elif vs == "p":
        return s
