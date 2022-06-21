# -*- coding: utf-8 -*-
"""
Class to contain the information needed to describe an ultimate point.

Author: Kevin Fiedler
Date Created: 5/30/22
Date Last Modified: 5/30/22
"""

class Point:
    lorax_score = False #Whether we scored the point or not.
    lorax_pull = False #Whether we started on O or D.
    assist = "" #Name of player
    goal = "" #Name of player
    male_players = [] #list of names
    female_players = [] #list of names
    
    
    def __init__(self, lorax_score=False, lorax_pull=False, assist="", goal="", male_players=[], female_players=[]):
        self.lorax_score = lorax_score
        self.lorax_pull = lorax_pull
        self.assist = assist
        self.goal = goal
        self.male_players = male_players
        self.female_players = female_players
         
    def __repr__(self):
        return "<Point lorax_score:%s lorax_pull:%s, assist:%s, goal:%s, male_players:%s, female_players:%s>" % (self.lorax_score, self.lorax_pull, self.assist, self.goal, self.male_players, self.female_players)

    def __str__(self):
        return "<Point: lorax_score:%s lorax_pull:%s, assist:%s, goal:%s, male_players:%s, female_players:%s>" % (self.lorax_score, self.lorax_pull, self.assist, self.goal, self.male_players, self.female_players)
