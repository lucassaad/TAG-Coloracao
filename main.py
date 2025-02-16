import random
# ESTRUTURAS - cada vértice é um jogo e jogos são adjacentes se possuem times em comum
Graph:dict[tuple : list[tuple]] = dict()                # Graph: [game:incompatible games]
class Vertex:
    def __init__(self, teams:tuple, color=None):
        self.teams = teams
        self.color = color
def main():
    # TIMES
    teams = ['DFC', 'TFC', 'AFC', 'LFC', 'FFC', 'OFC', 'CFC']
    

    # JOGOS
    games = []
    for i in range(len(teams)-1):
        for j in range(i+1, len(teams)):
            games.append(Vertex((teams[i], teams[j])))
            games.append(Vertex((teams[j], teams[i])))
    for game in games:
        print(game.teams)
    

    for game1 in games:                         # Add [game:incompatible games] to the graph
        if game1 not in Graph:
            Graph[game1] = []
        for game2 in games:
            if (game1.teams[0] in game2.teams or game1.teams[1] in game2.teams) and game1 != game2:
                Graph[game1].append(game2)
    
    # COLORAÇÃO - Greedy algorithm
    
    all_colors=[0]
    game = games.pop()
    game.color = 0
    while games:
        game = games.pop()
        if game.color == None:
            colors = []
            for incompatible in Graph[game]:
                if (incompatible.color != None) and (incompatible.color not in colors):
                    colors.append(incompatible.color)                  
                    if incompatible.color not in all_colors:
                        all_colors.append(incompatible.color)
            for i in range(len(all_colors) + 2):
                if i not in colors:
                    game.color = i
                    break                       

main()