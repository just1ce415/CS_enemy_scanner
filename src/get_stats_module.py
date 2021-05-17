"""
This module gets player's stats.
"""

from arrays import Array, Array2D
from adt import PlayerStats
from copy import deepcopy

def start(link, map):
    """
    Receives player's stats.

    :type link: string
    :param link: Palyers link.

    :type map: string
    :param map: Name of the current map.
    """
    enemy = PlayerStats(link)
    stats = Array(10)
    site_stats = enemy.soup_get_other_stats()
    if enemy.steam_data != "-":
        stats[3] = enemy.steam_get_kd
        best_weapons = enemy.steam_get_weapon_list()
        stats[6] = deepcopy(best_weapons)
        stats[7] = enemy.steam_add_accuracy(best_weapons)
    else:
        stats[3] = site_stats[1]
        stats[6] = None
        stats[7] = enemy.soup_get_weapon_list()
    stats[0] = enemy.soup_get_nickname
    stats[1] = enemy.soup_get_rank
    stats[2] = site_stats[0]
    stats[4] = site_stats[4]
    stats[5] = site_stats[2]
    stats[8] = site_stats[3]
    stats[9] = map
    return stats
        

# if __name__ == "__main__":
#     print(start("https://steamcommunity.com/profiles/76561198880579276/", "mirage"))