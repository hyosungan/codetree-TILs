MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

class agent:
    def __init__(self,codename,score):
        self.codename=codename
        self.score=score

Agent=[agent(codenames[i],scores[i]) for i in range(MAX_N)]

name=''
minimum=100
for agent in Agent:
    if minimum>=agent.score:
        name=agent.codename
        minimum=agent.score
print(name,minimum)

    

