from random import choice

#members = ['Rabin', 'Sampi', 'Aman', 'Arman', 'Atish', 'Prabin']

members = []
file = open('players.txt','r')
members = file.read().splitlines()

teamA = []
teamB = []

while len(members)>0:
    playerA = choice(members)
    teamA.append(playerA)
    members.remove(playerA)

    if members == []:
        break

    playerB = choice(members)
    teamB.append(playerB)
    members.remove(playerB)

print(teamA)
print(teamB)
