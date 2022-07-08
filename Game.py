# -*- coding: utf-8 -*-
"""
Class to represent the information needed to describe an ultimate game.

Author: Kevin Fiedler
Date Created: 5/30/22
Date Last Modified: 6/6/22
"""

import Point
import pandas as pd

class Game():
   
    def __init__(self, name="", points=[]):
        self.points = points
        self.stats = pd.DataFrame()
        self.name = name
        self.pair_stats = {}
        
    def add_Point(self, point):
        self.points.append(point)
        self._update_stats()
        
    def add_PointsFromFile(self, filename):
        #Read in the file from an Excel file.
        df = pd.read_excel(filename)
        self.add_PointsFromDataframe(df)
        
    def add_PointsFromDataframe(self, df):
        columns = list(df)
        for i in columns:
            if i == "Point":
                continue
            if i == 1:
                if df[i][0] == 1:
                    lorax_score = True
                else:
                    lorax_score = False
            else:#Look one column back to compare score
                if df[i-1][0] != df[i][0]:
                    lorax_score = True
                else:
                    lorax_score = False
                    
            if df[i][2] == "d" or df[i][2] == "D":
                lorax_pull = True
            elif df[i][2] == "o" or df[i][2] == "O":
                lorax_pull = False #Whether we started on O or D.
            else:
                print("Incorrect data format for O/D.")
                print(df[i][2])
                Exception()
                
            assist = df[i][3] #Name of player
            goal = df[i][4] #Name of player
            
            male_players = [] #list of names
            female_players = [] #list of names
            num_elems = len(df[i])
            for j in range(5, num_elems):
                if df[i][j] == "M":
                    male_players.append(df["Point"][j])
                elif df[i][j] == "F":
                    female_players.append(df["Point"][j])                
            
            self.points.append(Point.Point(lorax_score=lorax_score, lorax_pull=lorax_pull, \
                                           assist=assist, goal=goal, \
                                           male_players=male_players, female_players=female_players))
        self._update_stats()
            
    def get_stats(self):
        return self.stats
        
    def _update_stats(self):
        self.stats = pd.DataFrame()
        self._compute_DefenseTotals()
        self._compute_OffenseTotals()
        self._compute_AllPointTotals()
        self._compute_DefPercentage()
        self._compute_DefPercentageAboveAverage()
        self._compute_OffPercentage()
        self._compute_OffPercentageAboveAverage()
        self._compute_GoalTotals()
        self._compute_GoalsPerPoint()
        self._compute_AssistTotals()
        self._compute_AssistsPerPoint()
        self._compute_GoalAssistTotals()
        self._compute_GoalAssistPerPoint()
        self._compute_Breaks()
        self._compute_BreakPercentage()
        self._compute_BreakAboveAverage()
        self._compute_Holds()
        self._compute_HoldPercentage()
        self._compute_HoldAboveAverage()
        self._compute_TotalAboveAverage()   
        
        #For the pair stats, it is convenient to have the dataframes preconstructed.
        players = []
        for point in self.points:
            for player in point.male_players:
                if player not in players:
                    players.append(player)
            for player in point.female_players:
                if player not in players:
                    players.append(player)
        
        empty_df = pd.DataFrame()
        for player in players:
            partners = {}
            for partner in players:
                partners[partner] = 0.0
            df = pd.DataFrame.from_dict(partners, orient="index", columns=[player])
            empty_df = pd.concat([empty_df, df], axis=1).fillna(0)   

        self.pair_stats = {}
        self.pair_stats['DPP'] = empty_df.copy()
        self.pair_stats['OPP'] = empty_df.copy()
        self.pair_stats['PP'] = empty_df.copy()
        self.pair_stats['D%'] = empty_df.copy()
        self.pair_stats['O%'] = empty_df.copy()
        self.pair_stats['GA'] = empty_df.copy()
        self.pair_stats['BRK'] = empty_df.copy()
        self.pair_stats['BRK%'] = empty_df.copy()
        self.pair_stats['BAA'] = empty_df.copy()
        self.pair_stats['HLD'] = empty_df.copy()
        self.pair_stats['HLD%'] = empty_df.copy()
        self.pair_stats['HAA'] = empty_df.copy()
        self.pair_stats['TAA'] = empty_df.copy()
        
        self._compute_PairDefenseTotals()
        self._compute_PairOffenseTotals()
        self._compute_PairAllPointTotals()
        self._compute_PairOffPercentage()
        self._compute_PairDefPercentage()
        self._compute_PairGoalAssist()
        self._compute_PairBreaks()
        self._compute_PairBreakPercentage()
        self._compute_PairBreakAboveAverage()
        self._compute_PairHolds()
        self._compute_PairHoldPercentage()
        self._compute_PairHoldAboveAverage()
        self._compute_PairTotalAboveAverage() 
    
    def _compute_DefenseTotals(self):
        defense_totals = {}
        for point in self.points:
            if point.lorax_pull is True:
                for player in point.male_players:
                    if player in defense_totals.keys():
                        defense_totals[player] = defense_totals[player] + 1
                    else:
                        defense_totals[player] = 1
                for player in point.female_players:
                    if player in defense_totals.keys():
                        defense_totals[player] = defense_totals[player] + 1
                    else:
                        defense_totals[player] = 1
        df = pd.DataFrame.from_dict(defense_totals, orient="index", columns=["DPP"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
        
    def _compute_OffenseTotals(self):
        offense_totals = {}
        for point in self.points:
            if point.lorax_pull is False:
                for player in point.male_players:
                    if player in offense_totals.keys():
                        offense_totals[player] = offense_totals[player] + 1
                    else:
                        offense_totals[player] = 1
                for player in point.female_players:
                    if player in offense_totals.keys():
                        offense_totals[player] = offense_totals[player] + 1
                    else:
                        offense_totals[player] = 1
        df = pd.DataFrame.from_dict(offense_totals, orient="index", columns=["OPP"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
    
    def _compute_AllPointTotals(self):
        offense_totals = self.stats["OPP"]
        defense_totals = self.stats["DPP"]
        all_points_totals = {}
        for player in defense_totals.keys():
            if player in offense_totals.keys():
                all_points_totals[player] = offense_totals[player] + defense_totals[player]
            else:
                all_points_totals[player] = defense_totals[player]
        for player in offense_totals.keys():
            if player not in all_points_totals.keys():
                all_points_totals[player] = offense_totals[player]
        df = pd.DataFrame.from_dict(all_points_totals, orient="index", columns=["PP"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
        
    def _compute_OffPercentage(self):
        offense_totals = self.stats["OPP"]
        point_totals = self.stats["PP"]
        off_percentage = {}
        for player in point_totals.keys():
            if player in offense_totals.keys():
                off_percentage[player] = 100*offense_totals[player]/point_totals[player]
            else:
                off_percentage[player] = 0

        df = pd.DataFrame.from_dict(off_percentage, orient="index", columns=["O%"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
        
    def _compute_OffPercentageAboveAverage(self):
        off_percentage = self.stats["O%"]
        total_o_points = 0
        for point in self.points:
            if point.lorax_pull is False:
                total_o_points = total_o_points + 1       
        avg_o_percent = 100*total_o_points/len(self.points)
        off_percentage_above_average = {}
        for player in off_percentage.keys():
            off_percentage_above_average[player] = off_percentage[player] - avg_o_percent

        df = pd.DataFrame.from_dict(off_percentage_above_average, orient="index", columns=["O%AA"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
        
    def _compute_DefPercentage(self):
        defense_totals = self.stats["DPP"]
        point_totals = self.stats["PP"]
        def_percentage = {}
        for player in point_totals.keys():
            if player in defense_totals.keys():
                def_percentage[player] = 100*defense_totals[player]/point_totals[player]
            else:
                def_percentage[player] = 0

        df = pd.DataFrame.from_dict(def_percentage, orient="index", columns=["D%"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
        
    def _compute_DefPercentageAboveAverage(self):
        def_percentage = self.stats["D%"]
        total_d_points = 0
        for point in self.points:
            if point.lorax_pull is True:
                total_d_points = total_d_points + 1       
        avg_d_percent = 100*total_d_points/len(self.points)
        def_percentage_above_average = {}
        for player in def_percentage.keys():
            
            def_percentage_above_average[player] = def_percentage[player] - avg_d_percent

        df = pd.DataFrame.from_dict(def_percentage_above_average, orient="index", columns=["D%AA"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
        
    def _compute_GoalTotals(self):
        goal_totals = {}
        for point in self.points:   
            if type(point.goal) is type(0.0):
                continue
            else:
                if point.goal in goal_totals.keys():
                    goal_totals[point.goal] = goal_totals[point.goal] + 1
                else:
                    goal_totals[point.goal] = 1
        df = pd.DataFrame.from_dict(goal_totals, orient="index", columns=["G"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
    
    def _compute_GoalsPerPoint(self):
        goal_totals = self.stats["G"]
        goals_per_point = {}
        for player in goal_totals.keys():
            if self.stats["PP"][player] == 0:
                print(player)
                print(self.name)
            goals_per_point[player] = goal_totals[player]/self.stats["PP"][player]
        df = pd.DataFrame.from_dict(goals_per_point, orient="index", columns=["GPP"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
    
    def _compute_AssistTotals(self):
        assist_totals = {}
        for point in self.points:   
            if type(point.goal) is type(0.0):
                continue
            else:
                if point.assist in assist_totals.keys():
                    assist_totals[point.assist] = assist_totals[point.assist] + 1
                else:
                    assist_totals[point.assist] = 1
        df = pd.DataFrame.from_dict(assist_totals, orient="index", columns=["A"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
    
    def _compute_AssistsPerPoint(self):
        assist_totals = self.stats["A"]
        assists_per_point = {}
        for player in assist_totals.keys():
            if self.stats["PP"][player] == 0:
                assists_per_point[player] = 0
            else:             
                assists_per_point[player] = assist_totals[player]/self.stats["PP"][player]
        df = pd.DataFrame.from_dict(assists_per_point, orient="index", columns=["APP"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
    
    def _compute_GoalAssistTotals(self):
        goal_totals = self.stats["G"]
        assist_totals = self.stats["A"]
        goalassist_totals = {}
        for player in goal_totals.keys():
            if player in assist_totals.keys():
                goalassist_totals[player] = assist_totals[player] + goal_totals[player]
            else:
                goalassist_totals[player] = goal_totals[player]
        for player in assist_totals.keys():
            if player not in goalassist_totals.keys():
                goalassist_totals[player] = assist_totals[player]
        df = pd.DataFrame.from_dict(goalassist_totals, orient="index", columns=["GA"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
    
    def _compute_GoalAssistPerPoint(self):
        goals_per_point = self.stats["GPP"]
        assists_per_point = self.stats["APP"]
        goalassistperpoint_totals = {}
        for player in goals_per_point.keys():
            if player in assists_per_point.keys():
                goalassistperpoint_totals[player] = assists_per_point[player] + goals_per_point[player]
            else:
                goalassistperpoint_totals[player] = goals_per_point[player]
        for player in assists_per_point.keys():
            if player not in goalassistperpoint_totals.keys():
                goalassistperpoint_totals[player] = assists_per_point[player]
        df = pd.DataFrame.from_dict(goalassistperpoint_totals, orient="index", columns=["GAPP"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
    
    def _compute_Breaks(self):
        breaks = {}
        for point in self.points:
            if point.lorax_pull is True and point.lorax_score is True:
                for player in point.male_players:
                    if player in breaks.keys():
                        breaks[player] = breaks[player] + 1
                    else:
                        breaks[player] = 1
                for player in point.female_players:
                    if player in breaks.keys():
                        breaks[player] = breaks[player] + 1
                    else:
                        breaks[player] = 1
        df = pd.DataFrame.from_dict(breaks, orient="index", columns=["BRK"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
        
    def _compute_BreakPercentage(self):
        break_percentage = {}
        breaks = self.stats["BRK"]
        def_totals = self.stats["DPP"]
        for player in def_totals.keys():
            if def_totals[player] != 0:
                break_percentage[player] = 100*breaks[player]/def_totals[player]
            else:
                break_percentage[player] = 0
        df = pd.DataFrame.from_dict(break_percentage, orient="index", columns=["BRK%"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
    
    def _compute_BreakAboveAverage(self):
        breaks = self.stats["BRK"]
        total_breaks = sum(breaks)/7
        d_points = self.stats["DPP"]
        total_d_points = sum(d_points)/7
        avg_breakPercentage = 100*total_breaks/total_d_points
        
        break_percentage = self.stats["BRK%"]
        break_above_average = {}
        for player in break_percentage.keys():
            break_above_average[player] = (break_percentage[player] - avg_breakPercentage)*d_points[player]/total_d_points
            
        df = pd.DataFrame.from_dict(break_above_average, orient="index", columns=["BAA"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
    
    def _compute_Holds(self):
        holds = {}
        for point in self.points:
            if point.lorax_pull is False and point.lorax_score is True:
                for player in point.male_players:
                    if player in holds.keys():
                        holds[player] = holds[player] + 1
                    else:
                        holds[player] = 1
                for player in point.female_players:
                    if player in holds.keys():
                        holds[player] = holds[player] + 1
                    else:
                        holds[player] = 1
        df = pd.DataFrame.from_dict(holds, orient="index", columns=["HLD"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
       
    def _compute_HoldPercentage(self):
        hold_percentage = {}
        holds = self.stats["HLD"]
        off_totals = self.stats["OPP"]
        for player in off_totals.keys():
            if off_totals[player] != 0:
                hold_percentage[player] = 100*holds[player]/off_totals[player]
            else:
                hold_percentage[player] = 0
        df = pd.DataFrame.from_dict(hold_percentage, orient="index", columns=["HLD%"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
    
    def _compute_HoldAboveAverage(self):
        holds = self.stats["HLD"]
        total_holds = sum(holds)/7
        o_points = self.stats["OPP"]
        total_o_points = sum(o_points)/7
        avg_holdPercentage = 100*total_holds/total_o_points
        
        hold_percentage = self.stats["HLD%"]
        hold_above_average = {}
        for player in hold_percentage.keys():
            hold_above_average[player] = (hold_percentage[player] - avg_holdPercentage)*o_points[player]/total_o_points
            
        df = pd.DataFrame.from_dict(hold_above_average, orient="index", columns=["HAA"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
        
    def _compute_TotalAboveAverage(self):
        hold_above_average = self.stats["HAA"]
        break_above_average = self.stats["BAA"]
        total_above_average = {}
        for player in hold_above_average.keys():
            total_above_average[player] = hold_above_average[player] + break_above_average[player]

        df = pd.DataFrame.from_dict(total_above_average, orient="index", columns=["TAA"])
        self.stats = pd.concat([self.stats, df], axis=1).fillna(0)
        
    def _compute_PairDefenseTotals(self):       
        for point in self.points:
            if point.lorax_pull is True:
                current_players = []
                for player in point.male_players:
                    current_players.append(player)
                for player in point.female_players:
                    current_players.append(player)
                    
                for first in current_players:
                    for second in current_players:
                        self.pair_stats['DPP'][first][second] = self.pair_stats['DPP'][first][second] + 1

        
    def _compute_PairOffenseTotals(self):
        for point in self.points:
            if point.lorax_pull is False:
                current_players = []
                for player in point.male_players:
                    current_players.append(player)
                for player in point.female_players:
                    current_players.append(player)
                    
                for first in current_players:
                    for second in current_players:
                        self.pair_stats['OPP'][first][second] = self.pair_stats['OPP'][first][second] + 1

    def _compute_PairAllPointTotals(self):
        for point in self.points:
            current_players = []
            for player in point.male_players:
                current_players.append(player)
            for player in point.female_players:
                current_players.append(player)
                
            for first in current_players:
                for second in current_players:
                    self.pair_stats['PP'][first][second] = self.pair_stats['PP'][first][second] + 1

    def _compute_PairOffPercentage(self):
        off_totals = self.pair_stats["OPP"]
        for first in off_totals.to_dict().keys():
            for second in off_totals.to_dict().keys():
                if off_totals[first][second] != 0:
                    self.pair_stats['O%'][first][second] = 100*off_totals[first][second]/off_totals[first][first]
                else:
                    self.pair_stats['O%'][first][second] = 0
                    
    def _compute_PairDefPercentage(self):
        def_totals = self.pair_stats["DPP"]
        for first in def_totals.to_dict().keys():
            for second in def_totals.to_dict().keys():
                if def_totals[first][second] != 0:
                    self.pair_stats['D%'][first][second] = 100*def_totals[first][second]/def_totals[first][first]
                else:
                    self.pair_stats['D%'][first][second] = 0


    def _compute_PairGoalAssist(self):
        for point in self.points:
            if type(point.assist) is type(0.0):
                continue
            if type(point.goal) is type(0.0):
                continue
            self.pair_stats['GA'][point.goal][point.assist] = self.pair_stats['GA'][point.goal][point.assist] + 1
  
    def _compute_PairBreaks(self):
        for point in self.points:
            if point.lorax_pull is True and point.lorax_score is True:
                current_players = []
                for player in point.male_players:
                    current_players.append(player)
                for player in point.female_players:
                    current_players.append(player)
                    
                for first in current_players:
                    for second in current_players:
                        self.pair_stats['BRK'][first][second] = self.pair_stats['BRK'][first][second] + 1
    
    def _compute_PairBreakPercentage(self):
        breaks = self.pair_stats["BRK"]
        def_totals = self.pair_stats["DPP"]
        for first in def_totals.to_dict().keys():
            for second in def_totals.to_dict().keys():
                if def_totals[first][second] != 0:
                    self.pair_stats['BRK%'][first][second] = 100*breaks[first][second]/def_totals[first][second]
                else:
                    self.pair_stats['BRK%'][first][second] = 0

    def _compute_PairBreakAboveAverage(self):
        breaks = self.stats["BRK"]
        total_breaks = sum(breaks)/7
        d_points = self.stats["DPP"]
        total_d_points = sum(d_points)/7
        avg_breakPercentage = 100*total_breaks/total_d_points
        
        for first in self.pair_stats['BAA'].to_dict().keys():
            for second in self.pair_stats['BAA'].to_dict().keys():
                self.pair_stats['BAA'][first][second] = (self.pair_stats['BRK%'][first][second] - avg_breakPercentage)*self.pair_stats['DPP'][first][second]/total_d_points

    def _compute_PairHolds(self):
        for point in self.points:
            if point.lorax_pull is False and point.lorax_score is True:
                current_players = []
                for player in point.male_players:
                    current_players.append(player)
                for player in point.female_players:
                    current_players.append(player)
                    
                for first in current_players:
                    for second in current_players:
                        self.pair_stats['HLD'][first][second] = self.pair_stats['HLD'][first][second] + 1

    def _compute_PairHoldPercentage(self):
        holds = self.pair_stats["HLD"]
        off_totals = self.pair_stats["OPP"]
        for first in off_totals.to_dict().keys():
            for second in off_totals.to_dict().keys():
                if off_totals[first][second] != 0:
                    self.pair_stats['HLD%'][first][second] = 100*holds[first][second]/off_totals[first][second]
                else:
                    self.pair_stats['HLD%'][first][second] = 0

    def _compute_PairHoldAboveAverage(self):
        holds = self.stats["HLD"]
        total_holds = sum(holds)/7
        o_points = self.stats["OPP"]
        total_o_points = sum(o_points)/7
        avg_holdPercentage = 100*total_holds/total_o_points
        
        for first in self.pair_stats['HAA'].to_dict().keys():
            for second in self.pair_stats['HAA'].to_dict().keys():
                self.pair_stats['HAA'][first][second] = (self.pair_stats['HLD%'][first][second] - avg_holdPercentage)*self.pair_stats['OPP'][first][second]/total_o_points
    
    def _compute_PairTotalAboveAverage(self):
        for first in self.pair_stats['TAA'].to_dict().keys():
            for second in self.pair_stats['TAA'].to_dict().keys():
                self.pair_stats['TAA'][first][second] = self.pair_stats['BAA'][first][second] + self.pair_stats['HAA'][first][second]

        
    def print_GameStats(self):       
        print(self.stats)
        
    def save_Stats(self, filename):       
        self.stats.to_excel(filename)
        
    def print_PairStats(self):
        print(self.pair_stats)
        
    def save_PairStats(self, filename):       
        #Create an excel writer.
        writer = pd.ExcelWriter(filename)
        for stat in self.pair_stats:
            self.pair_stats[stat].to_excel(writer, sheet_name=stat)
        writer.save()
        
        
        