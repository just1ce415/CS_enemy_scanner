"""
"""

from arrays import Array, Array2D
from adt import Player, RecomendationADT
from copy import deepcopy


def start(link_1, link_2, link_3, link_4, link_5):
    """
    """
    enemy_1 = Player(link_1)
    enemy_2 = Player(link_2)
    enemy_3 = Player(link_3)
    enemy_4 = Player(link_4)
    enemy_5 = Player(link_5)
    enemy_team = Array(5)
    stats = Array2D(5, 9)
    for index in range(5):
        enemy_team[index] = eval(f"enemy_{index+1}")
        site_stats = enemy_team[index].get_kd_adr()
        if enemy_team[index].steam_data != "-":
            stats[index, 3] = enemy_team[index].get_kd_steam()
            best_weapons = enemy_team[index].get_bw_and_tk_steam()
            stats[index, 6] = deepcopy(best_weapons)
            stats[index, 7] = enemy_team[index].get_accuracy_steam(best_weapons)
        else:
            stats[index, 3] = site_stats[1]
            stats[index, 6] = enemy_team[index].most_kills()
            stats[index, 7] = enemy_team[index].most_kills()
        stats[index, 0] = enemy_team[index].get_nickname()
        stats[index, 1] = enemy_team[index].get_rank()
        stats[index, 2] = site_stats[0]
        stats[index, 4] = site_stats[4]
        stats[index, 5] = site_stats[2]
        stats[index, 8] = site_stats[3]
    return stats
        
def predictor():
    pass

if __name__ == "__main__":
    print(start("https://steamcommunity.com/profiles/76561198880579276/",
            "https://steamcommunity.com/profiles/76561199023828691/",
            "https://steamcommunity.com/profiles/76561198298923874/",
            "https://steamcommunity.com/profiles/76561198383858545/",
            "https://steamcommunity.com/profiles/76561198346444741/"))