"""
"""

from steam_api import get_data_from_steam
from soup import site_parsing
from arrays import Array, Array2D


class RecomendationADT:
    """
    """
    def __init__(self, map):
        self.data = Array(10)
        self.data[5] = {
            1: (300, 240),
            2: (420, 1200),
            3: (660, 2590),
            4: (420, 3200),
            5: (260, 4660)
        }
        self.data[7] = 4000
        self.data[8] = 0
        self.data[9] = map
        self.lose_dict = {
            1: 1400,
            2: 1900,
            3: 2400,
            4: 2900,
            5: 3400,
        }
    
    def process(self, win_lose, round_end, bomb_planted, enemies_alive,
            mates_alive, last_round_buy, knife_kill):
        """
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
            if self.data[1] == 1:
                pass

        
            pass
                
        
    def advice(self):
        """
        """
        pass


class Player:
    """
    """
    def __init__(self, steam_link):
        self.link = steam_link
        data_from_steam = get_data_from_steam(self.link)
        link = f"https://csgostats.gg/player/{data_from_steam[1]}"
        self.steam_data = data_from_steam[0]
        self.soup = site_parsing(link)

    def get_nickname(self):
        '''
        '''
        title_lst = str(self.soup.title).split(" ")
        nickname = " ".join(title_lst[15:-12])
        return nickname

    def get_rank(self):
        '''
        '''
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

    def get_kd_adr(self):
        '''
        '''
        info_str = str(self.soup.find_all("meta", property="og:description"))
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

    def most_kills(self):
        '''
        '''
        info_str = str(self.soup.find_all("tr", "p-row"))
        # implement
        pass

    def get_kd_steam(self):
        """
        Returns your kd in game
        """
        total_kills = self.steam_data["playerstats"]['stats'][0]['value']
        total_death = self.steam_data["playerstats"]['stats'][1]["value"]
        total_kill_death = round(total_kills/total_death, 2)
        return total_kill_death

    def get_adr_steam(self):
        """
        Returns your ADR
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

    def get_bw_and_tk_steam(self):
        """
        Returns 3 best weapons and their accuracy
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

    def get_accuracy_steam(self, list_of_weapons):
        """
        """
        total_kills = self.steam_data["playerstats"]['stats'][0]['value']
        for i in list_of_weapons:
            i[0] = round(i[0] / total_kills,2)
        return list_of_weapons

if __name__ == "__main__":
    a = Player("https://steamcommunity.com/profiles/76561198880579276/")
    a.get_rank()