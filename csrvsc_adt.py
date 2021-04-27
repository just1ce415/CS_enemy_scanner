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

    def write_kd(self, player: int):
        """
        Writes KD to the ADT.
        """
        pass

    def write_adr(self, player: int):
        """
        Writes ADR to the ADT.
        """
        pass

    def write_dev_aim(self, player: int):
        """
        Writes (Device, AIM) to the ADT.
        """
        pass

    def write_rank(self, player: int):
        """
        Writes rank to the ADT.
        """
        pass

    def write_hours(self, player: int):
        """
        Writes hours spent in CS to the ADT.
        """
        pass

    def write_winrate(self, player: int):
        """
        Writes player's winrate to the ADT.
        """
        pass

    def get_id(self):
        """
        Returns ADT's id.
        """
        pass

    def get_kd(self, player: int):
        """
        Returns KD from the ADT.
        """
        pass

    def get_adr(self, player: int):
        """
        Returns ADR from the ADT.
        """
        pass

    def get_dev_aim(self, player: int):
        """
        Returns (Device, AIM) from the ADT.
        """
        pass

    def get_rank(self, player: int):
        """
        Returns rank from the ADT.
        """
        pass

    def get_hours(self, player: int):
        """
        Returns hours spent in CS from the ADT.
        """
        pass

    def get_winrate(self, player: int):
        """
        Returns player's winrate from the ADT.
        """
        pass


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
        pass

    def get_winlose(self):
        """
        Returns if there is win or lose.
        True - win
        False - loss.
        """
        pass

    def get_bombpln(self):
        """
        Returns if the bomb was planted.
        True - win
        False - loss.
        """
        pass

    def get_enemies_alive(self):
        """
        Returns how many enemies alive.
        """
        pass

    def get_teammate_alive(self):
        """
        Returns how many teammates alive.
        """
        pass

    def get_enemies_buy(self):
        """
        Returns values from 0 to 5:
        0 - "raw pistols"
        5 - "full buy"
        """
        pass

    def get_mid_sum(self):
        """
        Returns the middle sum of the money per player of the
        enemy's team.
        """
        pass

    def set_winlose(self):
        """
        Sets if there is win or lose.
        True - win
        False - loss.
        """
        pass

    def set_bombpln(self):
        """
        Sets if the bomb was planted.
        True - win
        False - loss.
        """
        pass

    def set_enemies_alive(self):
        """
        Sets how many enemies alive.
        """
        pass

    def set_teammate_alive(self):
        """
        Sets how many teammates alive.
        """
        pass

    def set_enemies_buy(self):
        """
        Sets values from 0 to 5:
        0 - "raw pistols"
        5 - "full buy"
        """
        pass

    def set_mid_sum(self):
        """
        Sets the middle sum of the money per player of the
        enemy's team.
        """
        pass


if __name__ == '__main__':
    pass
