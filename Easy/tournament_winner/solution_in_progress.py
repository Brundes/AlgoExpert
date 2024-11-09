def tournamentWinner(competitions, results):
    idx = 0
    teamsScore = {}
    
    while idx < len(results):
        
        if results[idx] == 0:
            curWin = competitions[idx][1]
        else:
            curWin = competitions[idx][0]
            
        if curWin in teamsScore:
            teamsScore[curWin] += 3
        else:
            teamsScore[curWin] = 3
 
        idx += 1
        
    return max(teamsScore, key=teamsScore.get)

competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
]
results = [0, 0, 1]

print(tournamentWinner(competitions, results))