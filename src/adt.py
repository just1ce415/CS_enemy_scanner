"""
Module with realization of ADT's.
"""

import re
import requests
import json
from bs4 import BeautifulSoup
import cloudscraper

from arrays import Array


class RecomendationADT:
    """
    Initializing ADT RecomendationADT, which, based on users input, chooses the best tip.
    """
    def __init__(self, map, enemy_side):
        """
        Initialize new obj of class RecomendationADT.

        :type map: string
        :param map: Name of the map, on which you will be playing.

        :type enemy_side: string
        :param enemy_side: Defines if your enemies are CT or TT
        """
        self.data = Array(11)
        self.data[5] = {
            1: (300, 240),
            2: (420, 1000),
            3: (660, 2590),
            4: (420, 3200),
            5: (260, 4660)
        }
        self.data[7] = 4000
        self.data[8] = 0
        self.data[9] = map
        self.data[10] = enemy_side
        self.lose_dict = {
            0: 0,
            1: 1400,
            2: 1900,
            3: 2400,
            4: 2900,
            5: 3400,
        }
    
    def process(self, win_lose, round_end, bomb_planted, enemies_alive,
            mates_alive, last_round_buy, knife_kill):
        """
        Works with user's input so it becomes easier to make a summary and give a tip.

        :type win_lose: bool
        :param win_lose: Did your team win or loose

        :type round_end: int
        :param round_end: It defines how did the round end.
        Depending on how it ended enemy will gain different amount of $.

        :type bomb_planted: bool
        :param bomb_planted: Defines if bomb was planted or not.

        :type enemies_alive: int
        :param enemies_alive: Defines, how many enemies were lucky to remain alive.

        :type mates_alive: int
        :param mates_alive: Defines, how many allies were lucky to remain alive.

        :type last_ronud_buy: int
        :param last_round_buy: Your subjective opinion about enemies' buy from previous round.

        :type knife_kill: int
        :param knife_kill: Amount of kills with knife from previous round.
        """
        self.data[0] = win_lose
        self.data[1] = round_end
        self.data[2] = bomb_planted
        self.data[3] = enemies_alive
        self.data[4] = mates_alive
        self.data[6] = knife_kill
        kill_money = self.data[5][last_round_buy][0]*(5 - mates_alive) + 1500*knife_kill
        money_lost = -self.data[5][last_round_buy][1]*(5 - enemies_alive)
        self.data[7] += kill_money + money_lost
        if self.data[0]:
            self.data[8] = 0
            if self.data[1] == 1 or self.data[1] == 2:
                self.data[7] += 3250*5
            elif self.data[1] == 3 or self.data[1] == 4:
                self.data[7] += 3500*5 + 300
        else:
            self.data[8] += 1
            if self.data[8] > 5:
                self.data[8] = 5
            if self.data[1] == 1:
                self.data[7] += self.lose_dict[self.data[8]]*5
                if self.data[10] == "TT" and self.data[2]:
                    self.data[7] += 4300
            elif self.data[1] == 2:
                pass
            elif self.data[1] == 3:
                self.data[7] += self.lose_dict[self.data[8]]*5 + 4300
            elif self.data[1] == 4:
                self.data[7] += self.lose_dict[self.data[8]]*5
        if self.data[7] < 0:
            self.data[7] = 7500
        if self.data[7] > 80000:
            self.data[7] = 80000
                
    def advice(self):
        """
        Based on user's input chooses among tips for the best one in this situation.
        """
        money_per_enemy = self.data[7] // 5
        current_map = self.data[9]
        if current_map == "mirage":
            if money_per_enemy <= 1000:
                advice = f"Enemy team has luck of money, approximately {money_per_enemy} per head, so brobably they woudn't buy anything. High chance of full eco round. Be carefully at tight places of this map, like palace, underpass or b apartments."
            elif money_per_enemy <= 2000:
                advice = f"Enemy team has a little money, approximately {money_per_enemy} per head, so brobably they will make eco round, but there is a chance to play against 1-2 smgs. Moderate chance of full eco round, low chance of force-buy. Be carefully at tight places of this map, like palace, underpass or b apartments. They can also push this spots."
            elif money_per_enemy <= 3000:
                advice = f"Enemy team has some money, approximately {money_per_enemy} per head, so brobably they will make force-buy round, but there is a chance of semi-full-buy round. High chance of force-buy round, low chance of semi-buy round. They can push some spots, like middle or underpass, so be carefull and play slowly."
            elif money_per_enemy <= 4000:
                advice = f"Enemy team has enough money, approximately {money_per_enemy} per head, so brobably they will make full-buy round, but there is a low chance to play against 1-2 smgs and rifles and a moderate chance of awp. High chance of full-buy round, low chance of semi-full-buy. Maybe its good decision to play slow round if your team has rifles, or fast if only smgs."
            else:
                advice = f"Enemy team has a lot of money, approximately {money_per_enemy} per head, so surely they will make full-buy round. Be aware of awper in middle, jungle, stairs and cat."

        elif current_map == "inferno":
            if money_per_enemy <= 1000:
                advice = f"Enemy team has luck of money, approximately {money_per_enemy} per head, so brobably they woudn't buy anything. High chance of full eco round. Be carefully at tight places of this map, like banana, apartments. Be carefully while pushing."
            elif money_per_enemy <= 2000:
                advice = f"Enemy team has a little money, approximately {money_per_enemy} per head, so brobably they will make eco round, but there is a chance to play against 1-2 smgs. Moderate chance of full eco round, low chance of force-buy. Be carefully at tight places of this map, especially at banana. Giving control over this spot can cause lose of the round."
            elif money_per_enemy <= 3000:
                advice = f"Enemy team has some money, approximately {money_per_enemy} per head, so brobably they will make force-buy round, but there is a chance of semi-full-buy round. High chance of force-buy round, low chance of semi-buy round. They can push some spots, like banana or middle, so be carefull and play slowly."
            elif money_per_enemy <= 4000:
                advice = f"Enemy team has enough money, approximately {money_per_enemy} per head, so brobably they will make full-buy round, but there is a low chance to play against 1-2 smgs and rifles, and a moderate chance of awp. High chance of full-buy round, low chance of semi-full-buy. It can be too dangerous to retake banana yet, if you lose it."
            else:
                advice = f"Enemy team has a lot of money, approximately {money_per_enemy} per head, so surely they will make full-buy round. Be aware of awper in the middle and banana."

        elif current_map == "dust_2":
            if money_per_enemy <= 1000:
                advice = f"Enemy team has luck of money, approximately {money_per_enemy} per head, so brobably they woudn't buy anything. High chance of full eco round. Be carefully at tight places of this map, like long doors, cat, lower and tunnel."
            elif money_per_enemy <= 2000:
                advice = f"Enemy team has a little money, approximately {money_per_enemy} per head, so brobably they will make eco round, but there is a chance to play against 1-2 smgs. Moderate chance of full eco round, low chance of force-buy. Be carefully at tight places of this map, like long doors, cat, lower and tunnel. They can also push this spots."
            elif money_per_enemy <= 3000:
                advice = f"Enemy team has some money, approximately {money_per_enemy} per head, so brobably they will make force-buy round, but there is a chance of semi-full-buy round. High chance of force-buy round, low chance of semi-buy round. They can push some spots, like mid doors, long or B plant(if TT), so be carefull and play slowly."
            elif money_per_enemy <= 4000:
                advice = f"Enemy team has enough money, approximately {money_per_enemy} per head, so brobably they will make full-buy round, but there is a low chance to play against 1-2 smgs and rifles and a moderate chance of awp. High chance of full-buy round, low chance of semi-full-buy. Maybe its good decision to play slow round if your team has rifles, or fast if only smgs. There can be awper on the long."
            else:
                advice = f"Enemy team has a lot of money, approximately {money_per_enemy} per head, so surely they will make full-buy round. Be aware of awper in the CT middle, long, car, back plat (if CT)."

        elif current_map == "overpass":
            if money_per_enemy <= 1000:
                advice = f"Enemy team has luck of money, approximately {money_per_enemy} per head, so brobably they woudn't buy anything. High chance of full eco round. Be carefully at tight places of this map, like lower tunnels, toilets, water."
            elif money_per_enemy <= 2000:
                advice = f"Enemy team has a little money, approximately {money_per_enemy} per head, so brobably they will make eco round, but there is a chance to play against 1-2 smgs. Moderate chance of full eco round, low chance of force-buy. Be carefully at tight places of this map, like lower tunnels, toilets, water."
            elif money_per_enemy <= 3000:
                advice = f"Enemy team has some money, approximately {money_per_enemy} per head, so brobably they will make force-buy round, but there is a chance of semi-full-buy round. High chance of force-buy round, low chance of semi-buy round. They can push some spots, like short A, connector, or B plant (if TT), so be carefull and play slowly."
            elif money_per_enemy <= 4000:
                advice = f"Enemy team has enough money, approximately {money_per_enemy} per head, so brobably they will make full-buy round, but there is a low chance to play against 1-2 smgs and rifles and a moderate chance of awp. High chance of full-buy round, low chance of semi-full-buy. Be focused on middle control, because it's important part of overpass. Maybe its good decision to play slow round if your team has rifles, or fast if only smgs."
            else:
                advice = f"Enemy team has a lot of money, approximately {money_per_enemy} per head, so surely they will make full-buy round. Be aware of awper in A middle, train, long A and party."

        elif current_map == "train":
            if money_per_enemy <= 1000:
                advice = f"Enemy team has luck of money, approximately {money_per_enemy} per head, so brobably they woudn't buy anything. High chance of full eco round. Be carefully at tight places of this map, like A main, alley, heaven."
            elif money_per_enemy <= 2000:
                advice = f"Enemy team has a little money, approximately {money_per_enemy} per head, so brobably they will make eco round, but there is a chance to play against 1-2 smgs. Could be SSG 008, so be carefull at spacious spots, like alley, B plant, heaven. Moderate chance of full eco round, low chance of force-buy."
            elif money_per_enemy <= 3000:
                advice = f"Enemy team has some money, approximately {money_per_enemy} per head, so brobably they will make force-buy round, but there is a chance of semi-full-buy round. High chance of force-buy round, low chance of semi-buy round. They can push some spots, like B ramp, B plant, A main or alley."
            elif money_per_enemy <= 4000:
                advice = f"Enemy team has enough money, approximately {money_per_enemy} per head, so brobably they will make full-buy round, but there is a low chance to play against 1-2 smgs and rifles and a moderate chance of awp. High chance of full-buy round, low chance of semi-full-buy. Maybe its good decision to play fast and push some tight spots, like alley or A main."
            else:
                advice = f"Enemy team has a lot of money, approximately {money_per_enemy} per head, so surely they will make full-buy round. Be aware of awper in the heaven, A plant, connector and B plant between trains."

        elif current_map == "nuke":
            if money_per_enemy <= 1000:
                advice = f"Enemy team has luck of money, approximately {money_per_enemy} per head, so brobably they woudn't buy anything. High chance of full eco round. Be carefully at tight places of this map, like ramp, lobby and squeaky."
            elif money_per_enemy <= 2000:
                advice = f"Enemy team has a little money, approximately {money_per_enemy} per head, so brobably they will make eco round, but there is a chance to play against 1-2 smgs. Moderate chance of full eco round, low chance of force-buy. Be carefully, they can push lobby or outside (CT), A plant or vents (TT)."
            elif money_per_enemy <= 3000:
                advice = f"Enemy team has some money, approximately {money_per_enemy} per head, so brobably they will make force-buy round, but there is a chance of semi-full-buy round. High chance of force-buy round, low chance of semi-buy round. They can push some spots, like lobby or ramp, so be carefull and play slowly."
            elif money_per_enemy <= 4000:
                advice = f"Enemy team has enough money, approximately {money_per_enemy} per head, so brobably they will make full-buy round, but there is a low chance to play against 1-2 smgs and rifles and a moderate chance of awp. High chance of full-buy round, low chance of semi-full-buy. Maybe its good decision to play slow round if your team has rifles, or fast if only smgs."
            else:
                advice = f"Enemy team has a lot of money, approximately {money_per_enemy} per head, so surely they will make full-buy round. Be aware of outside if you have luck of money, awper on heaven."
        else:
            if money_per_enemy <= 1000:
                advice = f"Enemy team has luck of money, approximately {money_per_enemy} per head, so brobably they woudn't buy anything. High chance of full eco round. Be carefully at tight places of this map, like B stairs, T mid, both plants."
            elif money_per_enemy <= 2000:
                advice = f"Enemy team has a little money, approximately {money_per_enemy} per head, so brobably they will make eco round, but there is a chance to play against 1-2 smgs. Moderate chance of full eco round, low chance of force-buy. Be carefully of tight places pushing, like like B stairs, T mid, both plants."
            elif money_per_enemy <= 3000:
                advice = f"Enemy team has some money, approximately {money_per_enemy} per head, so brobably they will make force-buy round, but there is a chance of semi-full-buy round. High chance of force-buy round, low chance of semi-buy round. They can push some spots, like middle or B stairs, so be carefull and play slowly."
            elif money_per_enemy <= 4000:
                advice = f"Enemy team has enough money, approximately {money_per_enemy} per head, so brobably they will make full-buy round, but there is a low chance to play against 1-2 smgs and rifles and a moderate chance of awp. High chance of full-buy round, low chance of semi-full-buy. Maybe its good decision to play slow round if your team has rifles, or fast if only smgs."
            else:
                advice = f"Enemy team has a lot of money, approximately {money_per_enemy} per head, so surely they will make full-buy round. Be aware of awper on A plant or ramp, heaven or backside B."

        return advice

class PlayerStats:
    """
    Initialize ADT PlayerStats which contains data about enemies.
    """
    def __init__(self, steam_link):
        """
        Initialize new obj of class PlayerStats, which will contain enemy's stats.
        """
        self.link = steam_link
        steam_json, player_id = self.__steam_get_jsondata(self.link)
        link = f"https://csgostats.gg/player/{player_id}"
        self.steam_data = steam_json
        self.soup = self.__site_parsing(link)

    def __site_parsing(self, link: str):
        '''
        Represents it's data on webpage.

        :type link: string
        :param link: It is a link of player.
        '''
        scraper = cloudscraper.create_scraper()
        with open("cache/site.html", "wb", ) as file:
            file.write(scraper.get(link).content)
        with open("cache/site.html") as file:
            soup = BeautifulSoup(file, features="html.parser")
        return soup

    def __steam_get_jsondata(self, profile_link: str):
        """ 
        Returns json object with data from Steam Api.

        :type profile_link: string
        :param profile_link: It is a link of player.
        """
        base_url = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/"
        api_key = "6E41E51BEEC90F4A0A537907C62C7D35"
        appid = 730
        playerid = profile_link.split("/")[-2]
        search_url = f"{base_url}?appid={appid}&key={api_key}&steamid={playerid}&format=json"
        response = requests.get(search_url)
        if str(response) == "<Response [200]>":
            json_response = response.json()
        else:
            json_response = "-"
        return (json_response, playerid)

    def soup_get_nickname(self):
        '''
        Returns player's nickname.
        '''
        title_lst = str(self.soup.title).split(" ")
        nickname = " ".join(title_lst[15:-12])
        return nickname

    def soup_get_rank(self):
        '''
        Returns player's rank.
        '''
        try:
            rank_str = str(list(self.soup.find_all('img'))[1])
            rank = rank_str.split("/")[5]
            if rank == "images":
                rank_str = str(list(self.soup.find_all('img'))[2])
                rank = rank_str.split("/")[5][:2]
            else:
                rank = rank[:2]
            if rank[-1] == ".":
                rank = rank[0]
            try:
                if not (1 <= int(rank) <= 18):
                    rank = 0
            except:
                rank = 0
            return rank
        except IndexError:
            return 19

    def soup_get_other_stats(self):
        '''
        Returns other player's stats.
        '''
        info_str = str(self.soup.find_all("meta", property="og:description"))
        try:
            info = info_str.split(">")[0].split(" ")[1:-1]
            win_rate = info[0][-3:]
            kpd = info[1][-4:]
            hltv_kpd = info[2][-4:]
            hs_rate = info[3][-3:]
            adr = ''
            param = 0
            for i in range(len(info[4])):
                if (info[4][i] == ':') and (not param):
                    param = 1
                elif info[4][i] == "\\":
                    break
                elif param:
                    adr += info[4][i]
            return (win_rate, kpd, hltv_kpd, hs_rate, adr)
        except IndexError:
            return (0, 0, 0, 0, 0)

    def soup_get_weapon_list(self):
        '''
        Returns list of guns and accuracy with them.
        '''
        weapons_list = []
        try:
            for i in range(3):
                info_str = str(self.soup.find_all("tr", "p-row")[i]).split("\n")
                weapon = re.search(r'/[a-z0-9_]+\.png+', info_str[2]).group(0)[1:-10]
                accuracy = int(re.search(r'[0-9]+', info_str[10]).group(0)) / 100
                weapons_list.append([accuracy, weapon])
            return weapons_list
        except IndexError:
            return [[0, 42], [0, 42], [0, 42]]

    def steam_get_kd(self):
        """
        Returns your kd in game.
        """
        total_kills = self.steam_data["playerstats"]['stats'][0]['value']
        total_death = self.steam_data["playerstats"]['stats'][1]["value"]
        total_kill_death = round(total_kills/total_death, 2)
        return total_kill_death

    def steam_get_adr(self):
        """
        Returns your ADR.
        """
        total_damage_done = 0
        total_rounds_played = 0
        counter = 0
        for i in self.steam_data["playerstats"]['stats']:
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

    def steam_get_weapon_list(self):
        """
        Returns 3 best weapons and their accuracy.
        """
        list_of_weapons_kills = []
        for i in self.steam_data["playerstats"]['stats']:
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

    def steam_add_accuracy(self, list_of_weapons):
        """
        Returns weapons' accuracy.

        :type list_of_weapons: list
        :param list_of_weapons: List of best weapons and their accuracy of this player.
        """
        total_kills = self.steam_data["playerstats"]['stats'][0]['value']
        for i in list_of_weapons:
            i[0] = round(i[0] / total_kills, 2)
        return list_of_weapons
