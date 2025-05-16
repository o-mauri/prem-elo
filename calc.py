import math
import pandas as pd
import matplotlib.pyplot as plt

K_FACTOR = 50
SENSITIVITY = 0.75


SEASONEND = 2023
MODE = 1

def scoreCoef(teamA, teamB):
    difference = (teamA - teamB)*SENSITIVITY
    actual = 1/(1 + math.exp(-difference))
    return actual

def basicScore(teamA, teamB):
    if teamA == teamB:
        return 0
    if teamA > teamB:
        return 1
    else: 
        return -1


def eloChange(eloA, eloB, scoreA, scoreB):
    diff = eloB - eloA
    x = (10**(diff/400)) + 1
    expected = 1/x
    if MODE == 1:
      change = (scoreCoef(scoreA,scoreB)-expected)*K_FACTOR
    else:
        change = (basicScore(scoreA,scoreB)-expected)*K_FACTOR
    return change

def getELO(teamname, leagueDF):
    return leagueDF.loc[leagueTable['Team'] == teamname, 'ELO'].iloc[0]

def sortLeague(league):
    league = league.sort_values(by='ELO', ascending=False)
    return league

def updateELO(teamname, newvalue, leagueDF):
    leagueDF.loc[leagueTable['Team'] == teamname, 'ELO'] = newvalue

df = pd.read_csv("./premier-league-matches.csv")
seasonDf = df[df['Season_End_Year'] == SEASONEND]

competingTeams = seasonDf["Home"].unique().tolist()
startingElos = [1000 for _ in range(20)]

data = {"Team" : competingTeams,
        "ELO" : startingElos}

leagueTable = pd.DataFrame(data)

#### START LOOP
dfs = [pd.DataFrame(data)]
for gameweek in range(1,39):
    weekMatches = seasonDf[seasonDf['Wk']== gameweek]
    for index, row in weekMatches.iterrows():
        print(f"Week {gameweek}: {row['Home']} {row['HomeGoals']}-{row['AwayGoals']} {row['Away']}")
        homeElo = getELO(row['Home'], leagueTable)
        awayElo = getELO(row['Away'], leagueTable)
        homeChange = eloChange(homeElo, awayElo, row['HomeGoals'], row['AwayGoals'])
        awayChange = -homeChange
        print("---------------------------------------------------------")
        print(f"{row['Home']} - EloChange: {homeChange}")
        print(f"{row['Away']} - EloChange: {awayChange}")
        print(" ")
        newHome = homeElo + homeChange
        newAway = awayElo + awayChange
        updateELO(row['Home'], newHome, leagueTable)
        updateELO(row['Away'], newAway, leagueTable)
    dfs.append(leagueTable)
    leagueTable = sortLeague(leagueTable)
    print("               ")
    print(f"GAMEWEEK {gameweek}")
    print(leagueTable)
    #input("Press enter to continue...")

teamname = ["Arsenal", "Manchester City"]
x = range(0,39)
teams = {}
for team in seasonDf["Home"].unique().tolist():
    if team in teamname or len(teamname) == 0:
        teams[team] = []

for i in x:
    datatable = dfs[i]
    for t in teams.keys():
        teams[t].append(getELO(t,datatable))


for j in teams.keys():
    plt.plot(x,teams[j], label= j)

plt.legend(loc="upper center", ncol=6, fancybox=True)
plt.show()