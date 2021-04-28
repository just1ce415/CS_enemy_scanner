"""
Abstract Data Types for CS Rival Scanner:
PlayerADT and RecommendationADT
"""
from arrays import Array, Array2D


class PlayerADT:
    """
    ADT for preserving information about 5 (maximum) players.
    """
    def __init__(self, adtid=0):
        self.__id = adtid
        self.__data = Array2D(5, 6)  # SIX PARAMS FOR EACH PLAYER

    def write_kd(self, player: int, value: float):
        """
        Writes KD to the ADT.
        """
        self.__data[player, 0] = value

    def write_adr(self, player: int, value: float):
        """
        Writes ADR to the ADT.
        """
        self.__data[player, 1] = value

    def write_dev_aim(self, player: int, value):
        """
        Writes (Device, AIM) to the ADT.
        """
        self.__data[player, 2] = value

    def write_rank(self, player: int, value: str):
        """
        Writes rank to the ADT.
        """
        self.__data[player, 3] = value

    def write_hours(self, player: int, value: int):
        """
        Writes hours spent in CS to the ADT.
        """
        self.__data[player, 4] = value

    def write_winrate(self, player: int, value: float):
        """
        Writes player's winrate to the ADT.
        """
        self.__data[player, 5] = value

    def get_id(self) -> int:
        """
        Returns ADT's id.
        """
        return self.__id

    def get_kd(self, player: int) -> float:
        """
        Returns KD from the ADT.
        """
        return self.__data[player, 0]


    def get_adr(self, player: int) -> float:
        """
        Returns ADR from the ADT.
        """
        return self.__data[player, 1]

    def get_dev_aim(self, player: int):
        """
        Returns (Device, AIM) from the ADT.
        """
        return self.__data[player, 2]

    def get_rank(self, player: int) -> str:
        """
        Returns rank from the ADT.
        """
        return self.__data[player, 3]

    def get_hours(self, player: int) -> int:
        """
        Returns hours spent in CS from the ADT.
        """
        return self.__data[player, 4]

    def get_winrate(self, player: int) -> float:
        """
        Returns player's winrate from the ADT.
        """
        return self.__data[player, 5]


class RecommendationADT:
    """
    Class for preserving data about matches to give recommendations.
    """
    def __init__(self, adtid=0):
        self.__id = adtid
        self.__data = Array(6)

    def get_id(self):
        """
        Returns the ADT's id.
        """
        return self.__id

    def get_winlose(self) -> bool:
        """
        Returns if there is win or lose.
        True - win
        False - loss.
        """
        return self.__data[0]

    def get_bombpln(self) -> bool:
        """
        Returns if the bomb was planted.
        True - win
        False - loss.
        """
        return self.__data[1]

    def get_enemies_alive(self) -> int:
        """
        Returns how many enemies alive.
        """
        return self.__data[2]

    def get_teammate_alive(self) -> int:
        """
        Returns how many teammates alive.
        """
        return self.__data[3]

    def get_enemies_buy(self) -> int:
        """
        Returns values from 0 to 5:
        0 - "raw pistols"
        5 - "full buy"
        """
        return self.__data[4]

    def get_mid_sum(self) -> int:
        """
        Returns the middle sum of the money per player of the
        enemy's team.
        """
        return self.__data[5]

    def set_winlose(self, value: bool):
        """
        Sets if there is win or lose.
        True - win
        False - loss.
        """
        self.__data[0] = value

    def set_bombpln(self, value: bool):
        """
        Sets if the bomb was planted.
        True - win
        False - loss.
        """
        self.__data[1] = value

    def set_enemies_alive(self, value: int):
        """
        Sets how many enemies alive.
        """
        self.__data[2] = value

    def set_teammate_alive(self, value: int):
        """
        Sets how many teammates alive.
        """
        self.__data[3] = value

    def set_enemies_buy(self, value: int):
        """
        Sets values from 0 to 5:
        0 - "raw pistols"
        5 - "full buy"
        """
        self.__data[4] = value

    def set_mid_sum(self, value: int):
        """
        Sets the middle sum of the money per player of the
        enemy's team.
        """
        self.__data[5] = value


if __name__ == '__main__':
    players = PlayerADT()
    recommendations = RecommendationADT()
    # Write down information in players.
    players.write_kd(0, 1.6)
    players.write_adr(0, 234)
    players.write_dev_aim(0, {"glock": 73})
    players.write_rank(0, "silver_2")
    players.write_hours(0, 2000)
    players.write_winrate(0, 50.0)
    # Get info from players.
    players.get_kd(0)
    players.get_adr(0)
    players.get_dev_aim(0)
    players.get_rank(0)
    players.get_hours(0)
    players.get_winrate(0)
    # ---------------------------------
    # Set data for recomendations.
    recommendations.set_winlose(True)
    recommendations.set_bombpln(True)
    recommendations.set_enemies_alive(0)
    recommendations.set_teammate_alive(3)
    recommendations.set_enemies_buy(1)
    recommendations.set_mid_sum(1600)
    # Get that data for recomendations.
    recommendations.get_id()
    recommendations.get_winlose()
    recommendations.get_bombpln()
    recommendations.get_enemies_alive()
    recommendations.get_teammate_alive()
    recommendations.get_enemies_buy()
    recommendations.get_mid_sum()
