import sys
input = sys.stdin.readline
N, M = map(int, input().split())

keywords = set(input().rstrip() for _ in range(N))
remain = N

for _ in range(M):
    for word in input().rstrip().split(','):
        keywords.discard(word)
        
    print(len(keywords))