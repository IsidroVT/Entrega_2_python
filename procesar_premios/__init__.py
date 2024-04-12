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

def get_most_influent_player(dic):
    """This function recieves the player dictionary and returns the most influent player"""
    influence_list = [(name, (stats[0] * 1.5 + stats[1] * 1.25 + stats[2])) for name, stats in dic.items()]
    most_influent = max(influence_list, key = lambda x: x[1])
    return most_influent[0]

def get_average_goals(goals):
    """This function recieves the number of goals and returns the average per match value"""
    average_goals = sum(goals) / 25
    return average_goals