import requests
import json

def get_data_from_steam(profile_link: str):
    """ 
    Returns json object with data from Steaam Api
    """
    base_url = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/"
    api_key = "your key"
    appid = 730
    playerid = profile_link.split("/")[-2]
    search_url = f"{base_url}?appid={appid}&key={api_key}&steamid={playerid}&format=json"
    response = requests.get(search_url)
    json_response = response.json()
    return (json_response, playerid)

def kill_death(json_data):
    """
    Returns your kd in game
    """
    total_kills = json_data["playerstats"]['stats'][0]['value']
    total_death = json_data["playerstats"]['stats'][1]["value"]

    total_kill_death = round(total_kills/total_death, 2)

    return total_kill_death

def average_damage_per_round(json_data):
    """
    Returns your ADR
    """

    total_damage_done = 0
    total_rounds_played = 0

    counter = 0

    for i in json_data["playerstats"]['stats']:
        if i['name'] == 'total_damage_done':
            total_damage_done = i['value']
            counter += 1

        if i['name'] == 'total_rounds_played':
            total_rounds_played = i['value']
            counter += 1
        
        if counter == 2:
            break
    

    total_adr = round(total_damage_done/total_rounds_played,2)

    return total_adr

def best_weapons_and_total_kills(json_data):
    """
    Returns 3 best weapons and their accuracy
    """
    list_of_weapons_kills = []

    for i in json_data["playerstats"]['stats']:
        if i['name'][:12] == "total_kills_"\
        and i['name'] != "total_kills_hegrenade"\
        and i['name'] != 'total_kills_knife'\
        and i['name'] != 'total_kills_headshot'\
        and i['name'] != 'total_kills_enemy_weapon'\
        and i['name'] != 'total_kills_enemy_blinded'\
        and i['name'] != 'total_kills_knife_fight'\
        and i['name'] != 'total_kills_against_zoomed_sniper'\
        and i['name'] != 'total_kills_molotov'\
        and i['name'] != 'total_kills_taser'\
        and i['name'] != 'total_kills_enemy_weapon':

            list_of_weapons_kills.append([i['value'], i['name'][12:]])

    list_of_weapons_kills = sorted(list_of_weapons_kills)[-3:]

    return list_of_weapons_kills

def accuracy(json_data, list_of_weapons):
    """
    """
    total_kills = json_data["playerstats"]['stats'][0]['value']

    for i in list_of_weapons:
        i[0] = round(i[0] / total_kills,2)

    return list_of_weapons

if __name__ == "__main__":
    
    data = get_data_from_steam("https://steamcommunity.com/profiles/76561198880579276/")
    # print(data)
    bb = best_weapons_and_total_kills(data[0])
    print(accuracy(data[0],bb))
