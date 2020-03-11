n = int(input())
a = list(map(int, input().split()))


def has_duplicates(seq):
    return len(seq) != len(set(seq))


if has_duplicates(a):
    print("NO")
else:
    print("YES")
