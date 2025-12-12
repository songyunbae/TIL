import sys
sys.stdin = open('input.txt')
word = input().strip().upper()
print(word)
l = [word.count(chr(i)) for i in range(ord('A'), ord('Z') +1)]
print(l)
print('?') if l.count(max(l)) > 1 else print(chr(l.index(max(l))+ord('A')))