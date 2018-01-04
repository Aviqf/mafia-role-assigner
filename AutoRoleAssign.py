import random


print 'How many players are in your game?'
players = int(raw_input())

x=0
PlayerList = []
RoleList = []

while x < players:
    print "Enter a player"
    PlayerName = str(raw_input())
    PlayerList.insert(0, PlayerName)
    x = x+1

x=0

while x < players:
    print "Enter a role (duplicate roles are entered separately)"
    RoleName = str(raw_input())
    RoleList.insert(0, RoleName)
    x = x + 1

x = 0

while x < players:
    random.shuffle(RoleList)
    print PlayerList[x] + ' = ' + RoleList[x]
    x = x + 1


















