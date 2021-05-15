"""
"""

from arrays import Array, Array2D
from adt import Player, RecomendationADT
from copy import deepcopy


def start(link, map):
    """
    """
    enemy = Player(link)
    stats = Array(10)
    site_stats = enemy.get_kd_adr()
    if enemy.steam_data != "-":
        stats[3] = enemy.get_kd_steam()
        best_weapons = enemy.get_bw_and_tk_steam()
        stats[6] = deepcopy(best_weapons)
        stats[7] = enemy.get_accuracy_steam(best_weapons)
    else:
        stats[3] = site_stats[1]
        stats[6] = enemy.most_kills()
        stats[7] = enemy.most_kills()
    stats[0] = enemy.get_nickname()
    stats[1] = enemy.get_rank()
    stats[2] = site_stats[0]
    stats[4] = site_stats[4]
    stats[5] = site_stats[2]
    stats[8] = site_stats[3]
    stats[9] = map
    return stats
        
def predictor():
    pass

if __name__ == "__main__":
    print(start("https://steamcommunity.com/profiles/76561198880579276/"))