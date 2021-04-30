#As usual, Tom and Jerry are fighting. Tom has strength TS and Jerry has strength JS. You are given TS and your task is to find the number of possible values of JS such that Jerry wins the following game.

#The game consists of one or more turns. In each turn:

#If both TS and JS are even, their values get divided by 2 and the game proceeds with the next turn.
#If both TS and JS are odd, a tie is declared and the game ends.
#If TS is even and JS is odd, Tom wins the game.
#If TS is odd and JS is even, Jerry wins the game.
#Find the number of possible initial values of JS such that 1≤JS≤TS, there is no tie and Jerry wins the game.
"""
Example Input
2
1
11
Example Output
0
5
"""
# cook your dish here
def div(d):
    while(d%2==0):
        d//=2
    return d
for i in range(int(input())):
    ts = int(input())
    if (ts==1):
        print(0)
    else:
        for js in range(1,ts+1):
            if (ts%2==0):
                if (js%2==0):
                    s = div(ts)
                    print (s//2)
                    break
            else:
                if (js%2==0):
                    print (ts//2)
                    break
