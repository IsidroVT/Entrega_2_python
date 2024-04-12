def set_player_dictionary(names, goals, goals_avoided, assists):
    """This function returns a dictionary of tuples where the keys are the names of the players, each assigned a tuple with their respective stats"""
    dic_players = {}
    index = 0
    names_list = names.split(",")
    for name in names_list:
        dic_players[name] = (goals[index], goals_avoided[index], assists[index]) 
        index += 1
    return dic_players

def get_max_goalscorer(dic):
    """This function recieves the player dictionary and returns the player who scored the most goals and the number of goals"""
    max_scorer, max_goals = max(dic.items(), key = lambda x: x[1][0])
    return max_scorer, max_goals[0]