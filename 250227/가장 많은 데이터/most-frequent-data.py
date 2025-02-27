from collections import defaultdict

dictionary=defaultdict(int)

n = int(input())
words = [input() for _ in range(n)]

for i,word in enumerate(words):
    dictionary[word]+=1
    
print(max(dictionary.values()))
