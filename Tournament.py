# -*- coding: utf-8 -*-
"""
Class to represent the information needed to describe an ultimate tournament.

Author: Kevin Fiedler
Date Created: 5/31/22
Date Last Modified: 7/9/22
"""

import Game
import pandas as pd

class Tournament():
    
    def __init__(self, name="", games=[]):
        self.games = games
        self.name = name
        self.tourney_stats = pd.DataFrame()
        self.pair_tourney_stats = {}
        
    def add_Game(self, game):
        self.games.append(game)
        self._update_stats()
        
    def add_GamesFromFile(self, filename):
        #Read in the file from an Excel file.
        df = pd.read_excel(filename, sheet_name=None)
        for sheet in df.keys():
            game = Game.Game(points=[], name=sheet)
            game.add_PointsFromDataframe(df[sheet])
            self.games.append(game)
        self._update_stats()
        
    def get_stats(self):
        return self.tourney_stats
    
    def get_pair_stats(self):
        return self.pair_tourney_stats
        
    def _update_stats(self):
        self.tourney_stats = pd.DataFrame()
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
        
        #Sort the pair data based upon TAA values.
        total_above_average = self.tourney_stats['TAA'].sort_values(ascending=False)
        players = total_above_average.keys()
        
        empty_df = pd.DataFrame()
        for player in players:
            if type(player) is type(0.0): #Skip nan values.
                continue
            partners = {}
            for partner in players:
                if type(partner) is type(0.0): #Skip nan values.
                    continue
                partners[partner] = 0.0
            df = pd.DataFrame.from_dict(partners, orient="index", columns=[player])
            empty_df = pd.concat([empty_df, df], axis=1).fillna(0)   

        self.pair_tourney_stats = {}
        self.pair_tourney_stats['DPP'] = empty_df.copy()
        self.pair_tourney_stats['OPP'] = empty_df.copy()
        self.pair_tourney_stats['PP'] = empty_df.copy()
        self.pair_tourney_stats['D%'] = empty_df.copy()
        self.pair_tourney_stats['O%'] = empty_df.copy()
        self.pair_tourney_stats['GA'] = empty_df.copy()
        self.pair_tourney_stats['GAPP'] = empty_df.copy()
        self.pair_tourney_stats['BRK'] = empty_df.copy()
        self.pair_tourney_stats['BRK%'] = empty_df.copy()
        self.pair_tourney_stats['BRK%-AVG'] = empty_df.copy()
        self.pair_tourney_stats['BAA'] = empty_df.copy()
        self.pair_tourney_stats['HLD'] = empty_df.copy()
        self.pair_tourney_stats['HLD%'] = empty_df.copy()
        self.pair_tourney_stats['HLD%-AVG'] = empty_df.copy()
        self.pair_tourney_stats['HAA'] = empty_df.copy()
        self.pair_tourney_stats['TAA'] = empty_df.copy()
        
        self._compute_PairDefenseTotals()
        self._compute_PairOffenseTotals()
        self._compute_PairAllPointTotals()
        self._compute_PairDefPercentage()
        self._compute_PairOffPercentage()
        self._compute_PairGoalAssist()
        self._compute_PairBreaks()
        self._compute_PairBreakPercentage()
        self._compute_PairBreakPercentageMinusAverage()
        self._compute_PairBreakAboveAverage()
        self._compute_PairHolds()
        self._compute_PairHoldPercentage()
        self._compute_PairHoldPercentageMinusAverage()
        self._compute_PairHoldAboveAverage()
        self._compute_PairTotalAboveAverage() 
        
    def _compute_DefenseTotals(self):
        d_totals = {}
        for game in self.games:
            game_value = game.stats["DPP"]
            for player in game_value.keys():
                if player in d_totals.keys():
                    d_totals[player] = d_totals[player] + game_value[player]
                else:
                    d_totals[player] = game_value[player]
            
        df = pd.DataFrame.from_dict(d_totals, orient="index", columns=["DPP"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
        
    def _compute_OffenseTotals(self):
        o_totals = {}
        for game in self.games:
            game_value = game.stats["OPP"]
            for player in game_value.keys():
                if player in o_totals.keys():
                    o_totals[player] = o_totals[player] + game_value[player]
                else:
                    o_totals[player] = game_value[player]
            
        df = pd.DataFrame.from_dict(o_totals, orient="index", columns=["OPP"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
        
    def _compute_AllPointTotals(self):
        all_points_totals = {}
        for game in self.games:
            game_value = game.stats["PP"]
            for player in game_value.keys():
                if player in all_points_totals.keys():
                    all_points_totals[player] = all_points_totals[player] + game_value[player]
                else:
                    all_points_totals[player] = game_value[player]
            
        df = pd.DataFrame.from_dict(all_points_totals, orient="index", columns=["PP"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)\
            
    def _compute_OffPercentage(self):
        off_percentage = {}
        off_totals = self.tourney_stats["OPP"]
        point_totals = self.tourney_stats["PP"]
        for player in off_totals.keys():
            if off_totals[player] != 0:
                off_percentage[player] = 100*off_totals[player]/point_totals[player]
            else:
                off_percentage[player] = 0
        df = pd.DataFrame.from_dict(off_percentage, orient="index", columns=["O%"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
        
    def _compute_OffPercentageAboveAverage(self):
        off_percentage = self.tourney_stats["O%"]
        total_o_points = 0
        totaL_points = 0
        for game in self.games:
            for point in game.points:
                totaL_points = totaL_points + 1
                if point.lorax_pull is False:
                    total_o_points = total_o_points + 1       
        avg_o_percent = 100*total_o_points/totaL_points
        off_percentage_above_average = {}
        for player in off_percentage.keys():
            off_percentage_above_average[player] = off_percentage[player] - avg_o_percent

        df = pd.DataFrame.from_dict(off_percentage_above_average, orient="index", columns=["O%AA"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
        
    def _compute_DefPercentage(self):
        def_percentage = {}
        def_totals = self.tourney_stats["DPP"]
        point_totals = self.tourney_stats["PP"]
        for player in def_totals.keys():
            if def_totals[player] != 0:
                def_percentage[player] = 100*def_totals[player]/point_totals[player]
            else:
                def_percentage[player] = 0
        df = pd.DataFrame.from_dict(def_percentage, orient="index", columns=["D%"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
        
    def _compute_DefPercentageAboveAverage(self):
        def_percentage = self.tourney_stats["D%"]
        total_d_points = 0
        total_points = 0
        for game in self.games:
            for point in game.points:
                total_points = total_points + 1
                if point.lorax_pull is True:
                    total_d_points = total_d_points + 1       
        avg_d_percent = 100*total_d_points/total_points
        def_percentage_above_average = {}
        for player in def_percentage.keys():
            def_percentage_above_average[player] = def_percentage[player] - avg_d_percent

        df = pd.DataFrame.from_dict(def_percentage_above_average, orient="index", columns=["D%AA"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
        
    def _compute_GoalTotals(self):
        goal_totals = {}
        for game in self.games:
            game_value = game.stats["G"]
            for player in game_value.keys():
                if player in goal_totals.keys():
                    goal_totals[player] = goal_totals[player] + game_value[player]
                else:
                    goal_totals[player] = game_value[player]
            
        df = pd.DataFrame.from_dict(goal_totals, orient="index", columns=["G"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
    
    def _compute_GoalsPerPoint(self):
        goals_per_point = {}
        goals = self.tourney_stats["G"]
        points = self.tourney_stats["PP"]
        for player in points.keys():
            if points[player] != 0:
                goals_per_point[player] = goals[player]/points[player]
            else:
                goals_per_point[player] = 0
        df = pd.DataFrame.from_dict(goals_per_point, orient="index", columns=["GPP"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
    
    def _compute_AssistTotals(self):
        assist_totals = {}
        for game in self.games:
            game_value = game.stats["A"]
            for player in game_value.keys():
                if player in assist_totals.keys():
                    assist_totals[player] = assist_totals[player] + game_value[player]
                else:
                    assist_totals[player] = game_value[player]
            
        df = pd.DataFrame.from_dict(assist_totals, orient="index", columns=["A"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
    
    def _compute_AssistsPerPoint(self):
        assists_per_point = {}
        assists = self.tourney_stats["A"]
        points = self.tourney_stats["PP"]
        for player in points.keys():
            if points[player] != 0:
                assists_per_point[player] = assists[player]/points[player]
            else:
                assists_per_point[player] = 0
        df = pd.DataFrame.from_dict(assists_per_point, orient="index", columns=["APP"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
    
    def _compute_GoalAssistTotals(self):
        goalassist_totals = {}
        for game in self.games:
            game_value = game.stats["GA"]
            for player in game_value.keys():
                if player in goalassist_totals.keys():
                    goalassist_totals[player] = goalassist_totals[player] + game_value[player]
                else:
                    goalassist_totals[player] = game_value[player]
            
        df = pd.DataFrame.from_dict(goalassist_totals, orient="index", columns=["GA"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
    
    def _compute_GoalAssistPerPoint(self):
        goalassist_per_point = {}
        goalassist = self.tourney_stats["GA"]  
        points = self.tourney_stats["PP"]
        for player in points.keys():
            if points[player] != 0:
                goalassist_per_point[player] = goalassist[player]/points[player]
            else:
                goalassist_per_point[player] = 0
        df = pd.DataFrame.from_dict(goalassist_per_point, orient="index", columns=["GAPP"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
        
    def _compute_Breaks(self):
        breaks = {}
        for game in self.games:
            game_value = game.stats["BRK"]
            for player in game_value.keys():
                if player in breaks.keys():
                    breaks[player] = breaks[player] + game_value[player]
                else:
                    breaks[player] = game_value[player]
            
        df = pd.DataFrame.from_dict(breaks, orient="index", columns=["BRK"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
        
    def _compute_BreakPercentage(self):
        break_percentage = {}
        breaks = self.tourney_stats["BRK"]
        def_totals = self.tourney_stats["DPP"]
        for player in def_totals.keys():
            if def_totals[player] != 0:
                break_percentage[player] = 100*breaks[player]/def_totals[player]
            else:
                break_percentage[player] = 0
        df = pd.DataFrame.from_dict(break_percentage, orient="index", columns=["BRK%"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
        
    def _compute_BreakAboveAverage(self):
        break_above_average = {}
        for game in self.games:
            game_value = game.stats["BAA"]
            for player in game_value.keys():
                if player in break_above_average.keys():
                    break_above_average[player] = break_above_average[player] + game_value[player]
                else:
                    break_above_average[player] = game_value[player]
        
        #Round the result to a reasonable number of decimal places
        for player in break_above_average.keys():
            break_above_average[player] = round(break_above_average[player], 4)
            
        df = pd.DataFrame.from_dict(break_above_average, orient="index", columns=["BAA"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)    
        
    def _compute_Holds(self):
        holds = {}
        for game in self.games:
            game_value = game.stats["HLD"]
            for player in game_value.keys():
                if player in holds.keys():
                    holds[player] = holds[player] + game_value[player]
                else:
                    holds[player] = game_value[player]
            
        df = pd.DataFrame.from_dict(holds, orient="index", columns=["HLD"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
        
    def _compute_HoldPercentage(self):
        hold_percentage = {}
        holds = self.tourney_stats["HLD"]
        off_totals = self.tourney_stats["OPP"]
        for player in off_totals.keys():
            if off_totals[player] != 0:
                hold_percentage[player] = 100*holds[player]/off_totals[player]
            else:
                hold_percentage[player] = 0
        df = pd.DataFrame.from_dict(hold_percentage, orient="index", columns=["HLD%"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
    
    def _compute_HoldAboveAverage(self):
        holds_above_average = {}
        for game in self.games:
            game_value = game.stats["HAA"]
            for player in game_value.keys():
                if player in holds_above_average.keys():
                    holds_above_average[player] = holds_above_average[player] + game_value[player]
                else:
                    holds_above_average[player] = game_value[player]
        
        #Round the result to a reasonable number of decimal places
        for player in holds_above_average.keys():
            holds_above_average[player] = round(holds_above_average[player], 4)
            
        df = pd.DataFrame.from_dict(holds_above_average, orient="index", columns=["HAA"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
            
    def _compute_TotalAboveAverage(self):
        total_above_average = {}
        for game in self.games:
            game_value = game.stats["TAA"]
            for player in game_value.keys():
                if player in total_above_average.keys():
                    total_above_average[player] = total_above_average[player] + game_value[player]
                else:
                    total_above_average[player] = game_value[player]
        
        #Round the result to a reasonable number of decimal places
        for player in total_above_average.keys():
            total_above_average[player] = round(total_above_average[player], 2)
            
        df = pd.DataFrame.from_dict(total_above_average, orient="index", columns=["TAA"])
        self.tourney_stats = pd.concat([self.tourney_stats, df], axis=1).fillna(0)
        
    def _compute_TotalGameRows(self):
        for ind in range(len(self.games)):
            game = self.games[ind]
            totals = game.stats.sum(axis=0)
            totals = totals.rename('Total')
            
            #Convert the ones that should be averages.
            totals['DPP'] = totals['DPP']/7
            totals['OPP'] = totals['OPP']/7
            totals['PP'] = totals['PP']/7
            totals['D%'] = totals['D%']/len(game.stats['D%'].keys())
            totals['D%AA'] = ''
            totals['O%'] = totals['O%']/len(game.stats['O%'].keys())
            totals['O%AA'] = ''
            totals['GPP'] = ''
            totals['APP'] = ''
            totals['GAPP'] = ''
            totals['BRK'] = totals['BRK']/7
            totals['BRK%'] = ''
            totals['BAA'] = ''
            totals['HLD'] = totals['HLD']/7
            totals['HLD%'] = ''
            totals['HAA'] = ''
            totals['TAA'] = ''
            
            game.stats = game.stats.append(totals)
            self.games[ind] = game
            
        
    def save_Stats(self, filename): 
        #Create total rows at the end for each game.
        self._compute_TotalGameRows()
        
        #Create total rows for the full tourney stats.
        totals = self.tourney_stats.sum(axis=0)
        totals = totals.rename('Total')
        
        #Convert the ones that should be averages.
        totals['DPP'] = totals['DPP']/7
        totals['OPP'] = totals['OPP']/7
        totals['PP'] = totals['PP']/7
        totals['D%'] = totals['D%']/len(self.tourney_stats['D%'].keys())
        totals['O%'] = totals['O%']/len(self.tourney_stats['O%'].keys())
        totals['GPP'] = ''
        totals['APP'] = ''
        totals['GAPP'] = ''
        totals['BRK'] = totals['BRK']/7
        totals['BRK%'] = ''
        totals['BAA'] = ''
        totals['HLD'] = totals['HLD']/7
        totals['HLD%'] = ''
        totals['HAA'] = ''
        totals['TAA'] = ''
        self.tourney_stats = self.tourney_stats.append(totals)
        
        #Create an excel writer.
        writer = pd.ExcelWriter(filename)
        self.tourney_stats.to_excel(writer, sheet_name="Totals") #Full tourney stats.
        for game in self.games:
            game.stats.to_excel(writer, sheet_name=game.name)
        writer.save()
        
    def save_PairStats(self, filename):         
        #Create an excel writer.
        writer = pd.ExcelWriter(filename)
        for stat in self.pair_tourney_stats:
            self.pair_tourney_stats[stat].to_excel(writer, sheet_name=stat)
        writer.save()
        
    def _compute_PairDefenseTotals(self):
        for game in self.games:
            game_value = game.pair_stats["DPP"]
            for first in game_value.keys():
                for second in game_value.keys():
                    self.pair_tourney_stats["DPP"][first][second] = self.pair_tourney_stats["DPP"][first][second] + game_value[first][second]

    def _compute_PairOffenseTotals(self):
        for game in self.games:
            game_value = game.pair_stats["OPP"]
            for first in game_value.keys():
                for second in game_value.keys():
                    self.pair_tourney_stats["OPP"][first][second] = self.pair_tourney_stats["OPP"][first][second] + game_value[first][second]

    def _compute_PairAllPointTotals(self):
        for game in self.games:
            game_value = game.pair_stats["PP"]
            for first in game_value.keys():
                for second in game_value.keys():
                    self.pair_tourney_stats["PP"][first][second] = self.pair_tourney_stats["PP"][first][second] + game_value[first][second]

    def _compute_PairOffPercentage(self):
        off_totals = self.pair_tourney_stats["OPP"]
        for first in off_totals.to_dict().keys():
            for second in off_totals.to_dict().keys():
                if off_totals[first][second] != 0:
                    self.pair_tourney_stats['O%'][first][second] = 100*off_totals[first][second]/off_totals[first][first]
                else:
                    self.pair_tourney_stats['O%'][first][second] = 0
                    
    def _compute_PairDefPercentage(self):
        def_totals = self.pair_tourney_stats["DPP"]
        for first in def_totals.to_dict().keys():
            for second in def_totals.to_dict().keys():
                if def_totals[first][second] != 0:
                    self.pair_tourney_stats['D%'][first][second] = 100*def_totals[first][second]/def_totals[first][first]
                else:
                    self.pair_tourney_stats['D%'][first][second] = 0

    def _compute_PairGoalAssist(self):
        for game in self.games:
            game_value = game.pair_stats["GA"]
            for first in game_value.keys():
                for second in game_value.keys():
                    self.pair_tourney_stats["GA"][first][second] = self.pair_tourney_stats["GA"][first][second] + game_value[first][second]
    
    def _compute_PairBreaks(self):
        for game in self.games:
            game_value = game.pair_stats["BRK"]
            for first in game_value.keys():
                for second in game_value.keys():
                    self.pair_tourney_stats["BRK"][first][second] = self.pair_tourney_stats["BRK"][first][second] + game_value[first][second]

    def _compute_PairBreakPercentage(self):
        breaks = self.pair_tourney_stats["BRK"]
        def_totals = self.pair_tourney_stats["DPP"]
        for first in def_totals.to_dict().keys():
            for second in def_totals.to_dict().keys():
                if def_totals[first][second] != 0:
                    self.pair_tourney_stats['BRK%'][first][second] = 100*breaks[first][second]/def_totals[first][second]
                else:
                    self.pair_tourney_stats['BRK%'][first][second] = 0    
                    
    def _compute_PairBreakPercentageMinusAverage(self):
        breaks = self.tourney_stats["BRK"]
        total_breaks = sum(breaks)/7
        d_points = self.tourney_stats["DPP"]
        total_d_points = sum(d_points)/7
        avg_breakPercentage = 100*total_breaks/total_d_points
        
        breaks = self.pair_tourney_stats["BRK"]
        def_totals = self.pair_tourney_stats["DPP"]
        for first in def_totals.to_dict().keys():
            for second in def_totals.to_dict().keys():
                if def_totals[first][second] != 0:
                    self.pair_tourney_stats['BRK%-AVG'][first][second] = 100*breaks[first][second]/def_totals[first][second] - avg_breakPercentage
                else:
                    self.pair_tourney_stats['BRK%-AVG'][first][second] = 0

    def _compute_PairBreakAboveAverage(self):
        for game in self.games:
            game_value = game.pair_stats["BAA"]
            for first in game_value.keys():
                for second in game_value.keys():
                    self.pair_tourney_stats["BAA"][first][second] = self.pair_tourney_stats["BAA"][first][second] + game_value[first][second]

    
    def _compute_PairHolds(self):
        for game in self.games:
            game_value = game.pair_stats["HLD"]
            for first in game_value.keys():
                for second in game_value.keys():
                    self.pair_tourney_stats["HLD"][first][second] = self.pair_tourney_stats["HLD"][first][second] + game_value[first][second]

    def _compute_PairHoldPercentage(self):
        holds = self.pair_tourney_stats["HLD"]
        off_totals = self.pair_tourney_stats["OPP"]
        for first in off_totals.to_dict().keys():
            for second in off_totals.to_dict().keys():
                if off_totals[first][second] != 0:
                    self.pair_tourney_stats['HLD%'][first][second] = 100*holds[first][second]/off_totals[first][second]
                else:
                    self.pair_tourney_stats['HLD%'][first][second] = 0
                    
    def _compute_PairHoldPercentageMinusAverage(self):
        holds = self.tourney_stats["HLD"]
        total_holds = sum(holds)/7
        o_points = self.tourney_stats["OPP"]
        total_o_points = sum(o_points)/7
        avg_holdPercentage = 100*total_holds/total_o_points
        
        holds = self.pair_tourney_stats["HLD"]
        off_totals = self.pair_tourney_stats["OPP"]
        for first in off_totals.to_dict().keys():
            for second in off_totals.to_dict().keys():
                if off_totals[first][second] != 0:
                    self.pair_tourney_stats['HLD%-AVG'][first][second] = 100*holds[first][second]/off_totals[first][second] - avg_holdPercentage
                else:
                    self.pair_tourney_stats['HLD%-AVG'][first][second] = 0
    
    def _compute_PairHoldAboveAverage(self):
        for game in self.games:
            game_value = game.pair_stats["HAA"]
            for first in game_value.keys():
                for second in game_value.keys():
                    self.pair_tourney_stats["HAA"][first][second] = self.pair_tourney_stats["HAA"][first][second] + game_value[first][second]

    def _compute_PairTotalAboveAverage(self):
        for game in self.games:
            game_value = game.pair_stats["TAA"]
            for first in game_value.keys():
                for second in game_value.keys():
                    self.pair_tourney_stats["TAA"][first][second] = self.pair_tourney_stats["TAA"][first][second] + game_value[first][second]

