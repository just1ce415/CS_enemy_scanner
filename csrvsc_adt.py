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
        self.__head = None
        self.__tail = None
        self.__length = 0

    def add_to_head(self, data):
        """
        Adds data about new match to the start of the list.
        """
        pass

    def add_to_tail(self, data):
        """
        Adds data about new match to the end of the list.
        """
        pass

    def remove_match(self, index: int):
        """
        Removes match with corresonding index.
        """
        pass

    def __getitem__(self, coord_tuple: tuple):
        """
        Gets a particular piece of information about the match.
        coord_tuple - (match, data_unit).
        """
        pass

    def get_match(self, match: int):
        """
        Returns stated match.
        """
        pass

    def get_id(self):
        """
        Returns ADT object's id.
        """
        pass


class Node:
    """
    Node for RecommendationADT.
    """

    def __init__(self, data):
        self._data = Array(0)
        self.next_element = None
