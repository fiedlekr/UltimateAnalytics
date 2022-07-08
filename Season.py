# -*- coding: utf-8 -*-
"""
Class to represent the information needed to describe an ultimate season.

Author: Kevin Fiedler
Date Created: 6/22/22
Date Last Modified: 6/22/22
"""

import Tournament
import pandas as pd

class Season():
    
    def __init__(self, name="", tournaments={}):
        self.tournaments = tournaments
        self.season_stats = pd.DataFrame()
        self.pair_season_stats = {}
        
    def add_Tournament(self, tournament):
        self.tournaments.append(tournament)
        self._update_stats()
        
    def add_TournamentsFromFiles(self, filenames):
        #Read in the tourneys from Excel files.
        for filename in filenames:
            base_filename = filename.split("_")[1]
            tournament = Tournament.Tournament(games=[], name=base_filename) #This is bad, but it seems hard to fix.
            tournament.add_GamesFromFile(filename)
            self.tournaments[filename] = tournament
        self._update_stats()
        
    def get_stats(self):
        return self.season_stats
    
    def get_pair_stats(self):
        return self.pair_season_stats
        
    def _update_stats(self):
        self.season_stats = pd.DataFrame()
        self._compute_DefenseTotals()
        self._compute_OffenseTotals()
        self._compute_AllPointTotals()
        self._compute_DefPercentage()
        self._compute_OffPercentage()
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
        for tournament in self.tournaments.keys():
            games = self.tournaments[tournament].games
            for game in games:
                for point in game.points:
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

        self.pair_season_stats = {}
        self.pair_season_stats['DPP'] = empty_df.copy()
        self.pair_season_stats['OPP'] = empty_df.copy()
        self.pair_season_stats['PP'] = empty_df.copy()
        self.pair_season_stats['D%'] = empty_df.copy()
        self.pair_season_stats['O%'] = empty_df.copy()
        self.pair_season_stats['GA'] = empty_df.copy()
        self.pair_season_stats['GAPP'] = empty_df.copy()
        self.pair_season_stats['BRK'] = empty_df.copy()
        self.pair_season_stats['BRK%'] = empty_df.copy()
        self.pair_season_stats['BRK%-AVG'] = empty_df.copy()
        self.pair_season_stats['BAA'] = empty_df.copy()
        self.pair_season_stats['HLD'] = empty_df.copy()
        self.pair_season_stats['HLD%'] = empty_df.copy()
        self.pair_season_stats['HLD%-AVG'] = empty_df.copy()
        self.pair_season_stats['HAA'] = empty_df.copy()
        self.pair_season_stats['TAA'] = empty_df.copy()
        
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
        self._compute_PairHoldAboveAverage()
        self._compute_PairHoldPercentageMinusAverage()
        self._compute_PairTotalAboveAverage() 

        
    def _compute_DefenseTotals(self):
        d_totals = {}
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].get_stats()["DPP"]
            for player in tournament_value.keys():
                if player in d_totals.keys():
                    d_totals[player] = d_totals[player] + tournament_value[player]
                else:
                    d_totals[player] = tournament_value[player]
            
        df = pd.DataFrame.from_dict(d_totals, orient="index", columns=["DPP"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)
        
    def _compute_OffenseTotals(self):
        o_totals = {}
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].get_stats()["OPP"]
            for player in tournament_value.keys():
                if player in o_totals.keys():
                    o_totals[player] = o_totals[player] + tournament_value[player]
                else:
                    o_totals[player] = tournament_value[player]
            
        df = pd.DataFrame.from_dict(o_totals, orient="index", columns=["OPP"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)
        
    def _compute_AllPointTotals(self):
        all_points_totals = {}
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].get_stats()["PP"]
            for player in tournament_value.keys():
                if player in all_points_totals.keys():
                    all_points_totals[player] = all_points_totals[player] + tournament_value[player]
                else:
                    all_points_totals[player] = tournament_value[player]
            
        df = pd.DataFrame.from_dict(all_points_totals, orient="index", columns=["PP"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)
        
    def _compute_OffPercentage(self):
        off_percentage = {}
        off_totals = self.season_stats["OPP"]
        point_totals = self.season_stats["PP"]
        for player in off_totals.keys():
            if off_totals[player] != 0:
                off_percentage[player] = off_totals[player]/point_totals[player]
            else:
                off_percentage[player] = 0
        df = pd.DataFrame.from_dict(off_percentage, orient="index", columns=["O%"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)
        
        
    def _compute_DefPercentage(self):
        def_percentage = {}
        def_totals = self.season_stats["DPP"]
        point_totals = self.season_stats["PP"]
        for player in def_totals.keys():
            if def_totals[player] != 0:
                def_percentage[player] = def_totals[player]/point_totals[player]
            else:
                def_percentage[player] = 0
        df = pd.DataFrame.from_dict(def_percentage, orient="index", columns=["D%"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)
        
    def _compute_GoalTotals(self):
        goal_totals = {}
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].get_stats()["G"]
            for player in tournament_value.keys():
                if player in goal_totals.keys():
                    goal_totals[player] = goal_totals[player] + tournament_value[player]
                else:
                    goal_totals[player] = tournament_value[player]
            
        df = pd.DataFrame.from_dict(goal_totals, orient="index", columns=["G"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)
    
    def _compute_GoalsPerPoint(self):
        goals_per_point = {}
        goals = self.season_stats["G"]
        points = self.season_stats["PP"]
        for player in points.keys():
            if points[player] != 0:
                goals_per_point[player] = goals[player]/points[player]
            else:
                goals_per_point[player] = 0
        df = pd.DataFrame.from_dict(goals_per_point, orient="index", columns=["GPP"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)
    
    def _compute_AssistTotals(self):
        assist_totals = {}
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].get_stats()["A"]
            for player in tournament_value.keys():
                if player in assist_totals.keys():
                    assist_totals[player] = assist_totals[player] + tournament_value[player]
                else:
                    assist_totals[player] = tournament_value[player]
            
        df = pd.DataFrame.from_dict(assist_totals, orient="index", columns=["A"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)
    
    def _compute_AssistsPerPoint(self):
        assists_per_point = {}
        assists = self.season_stats["A"]
        points = self.season_stats["PP"]
        for player in points.keys():
            if points[player] != 0:
                assists_per_point[player] = assists[player]/points[player]
            else:
                assists_per_point[player] = 0
        df = pd.DataFrame.from_dict(assists_per_point, orient="index", columns=["APP"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)
    
    def _compute_GoalAssistTotals(self):
        goalassist_totals = {}
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].get_stats()["GA"]
            for player in tournament_value.keys():
                if player in goalassist_totals.keys():
                    goalassist_totals[player] = goalassist_totals[player] + tournament_value[player]
                else:
                    goalassist_totals[player] = tournament_value[player]
            
        df = pd.DataFrame.from_dict(goalassist_totals, orient="index", columns=["GA"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)
    
    def _compute_GoalAssistPerPoint(self):
        goalassist_per_point = {}
        goalassist = self.season_stats["GA"]  
        points = self.season_stats["PP"]
        for player in points.keys():
            if points[player] != 0:
                goalassist_per_point[player] = goalassist[player]/points[player]
            else:
                goalassist_per_point[player] = 0
        df = pd.DataFrame.from_dict(goalassist_per_point, orient="index", columns=["GAPP"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)
        
    def _compute_Breaks(self):
        breaks = {}
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].get_stats()["BRK"]
            for player in tournament_value.keys():
                if player in breaks.keys():
                    breaks[player] = breaks[player] + tournament_value[player]
                else:
                    breaks[player] = tournament_value[player]
            
        df = pd.DataFrame.from_dict(breaks, orient="index", columns=["BRK"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)
        
    def _compute_BreakPercentage(self):
        break_percentage = {}
        breaks = self.season_stats["BRK"]
        def_totals = self.season_stats["DPP"]
        for player in def_totals.keys():
            if def_totals[player] != 0:
                break_percentage[player] = 100*breaks[player]/def_totals[player]
            else:
                break_percentage[player] = 0
        df = pd.DataFrame.from_dict(break_percentage, orient="index", columns=["BRK%"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)
        
    def _compute_BreakAboveAverage(self):
        break_above_average = {}
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].get_stats()["BAA"]
            for player in tournament_value.keys():
                if player in break_above_average.keys():
                    break_above_average[player] = break_above_average[player] + tournament_value[player]
                else:
                    break_above_average[player] = tournament_value[player]
        
        #Round the result to a reasonable number of decimal places
        for player in break_above_average.keys():
            break_above_average[player] = round(break_above_average[player], 2)
            
        df = pd.DataFrame.from_dict(break_above_average, orient="index", columns=["BAA"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)    
        
    def _compute_Holds(self):
        holds = {}
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].get_stats()["HLD"]
            for player in tournament_value.keys():
                if player in holds.keys():
                    holds[player] = holds[player] + tournament_value[player]
                else:
                    holds[player] = tournament_value[player]
            
        df = pd.DataFrame.from_dict(holds, orient="index", columns=["HLD"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)
        
    def _compute_HoldPercentage(self):
        hold_percentage = {}
        holds = self.season_stats["HLD"]
        off_totals = self.season_stats["OPP"]
        for player in off_totals.keys():
            if off_totals[player] != 0:
                hold_percentage[player] = 100*holds[player]/off_totals[player]
            else:
                hold_percentage[player] = 0
        df = pd.DataFrame.from_dict(hold_percentage, orient="index", columns=["HLD%"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)
    
    def _compute_HoldAboveAverage(self):
        holds_above_average = {}
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].get_stats()["HAA"]
            for player in tournament_value.keys():
                if player in holds_above_average.keys():
                    holds_above_average[player] = holds_above_average[player] + tournament_value[player]
                else:
                    holds_above_average[player] = tournament_value[player]
        
        #Round the result to a reasonable number of decimal places
        for player in holds_above_average.keys():
            holds_above_average[player] = round(holds_above_average[player], 2)
            
        df = pd.DataFrame.from_dict(holds_above_average, orient="index", columns=["HAA"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)
            
    def _compute_TotalAboveAverage(self):
        total_above_average = {}
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].get_stats()["TAA"]
            for player in tournament_value.keys():
                if player in total_above_average.keys():
                    total_above_average[player] = total_above_average[player] + tournament_value[player]
                else:
                    total_above_average[player] = tournament_value[player]
        
        #Round the result to a reasonable number of decimal places
        for player in total_above_average.keys():
            total_above_average[player] = round(total_above_average[player], 2)
            
        df = pd.DataFrame.from_dict(total_above_average, orient="index", columns=["TAA"])
        self.season_stats = pd.concat([self.season_stats, df], axis=1).fillna(0)
        
    def _compute_TotalRow(self):
        for ind in range(len(self.tournaments)):
            tournament = self.tournaments[ind]
            totals = self.tournaments[tournament].get_stats().sum(axis=0)
            totals = totals.rename('Total')
            
            #Convert the ones that should be averages.
            totals['DPP'] = totals['DPP']/7
            totals['OPP'] = totals['OPP']/7
            totals['PP'] = totals['PP']/7
            totals['D%'] = totals['D%']/len(self.season_stats['D%'].keys())
            totals['O%'] = totals['O%']/len(self.season_stats['O%'].keys())
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
            
            #season. = self.tournaments[tournament].get_stats().append(totals)
            #self.tournaments[ind] = tournament 
        
    def save_Stats(self, filename):        
        #Create an excel writer.
        writer = pd.ExcelWriter(filename)
        self.season_stats.to_excel(writer, sheet_name="Season Totals") #Full tourney stats.
        for tournament in self.tournaments.keys():
            self.tournaments[tournament].get_stats().to_excel(writer, sheet_name=self.tournaments[tournament].name)
        writer.save()
        
    def save_PairStats(self, filename):         
        #Create an excel writer.
        writer = pd.ExcelWriter(filename)
        for stat in self.pair_season_stats:
            self.pair_season_stats[stat].to_excel(writer, sheet_name=stat)
        writer.save()
            
    def _compute_PairDefenseTotals(self):
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].pair_tourney_stats["DPP"]
            for first in tournament_value.keys():
                for second in tournament_value.keys():
                    self.pair_season_stats["DPP"][first][second] = self.pair_season_stats["DPP"][first][second] + tournament_value[first][second]

    def _compute_PairOffenseTotals(self):
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].pair_tourney_stats["OPP"]
            for first in tournament_value.keys():
                for second in tournament_value.keys():
                    self.pair_season_stats["OPP"][first][second] = self.pair_season_stats["OPP"][first][second] + tournament_value[first][second]

    def _compute_PairAllPointTotals(self):
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].pair_tourney_stats["PP"]
            for first in tournament_value.keys():
                for second in tournament_value.keys():
                    self.pair_season_stats["PP"][first][second] = self.pair_season_stats["PP"][first][second] + tournament_value[first][second]

    def _compute_PairOffPercentage(self):
        off_totals = self.pair_season_stats["OPP"]
        for first in off_totals.to_dict().keys():
            for second in off_totals.to_dict().keys():
                if off_totals[first][second] != 0:
                    self.pair_season_stats['O%'][first][second] = 100*off_totals[first][second]/off_totals[first][first]
                else:
                    self.pair_season_stats['O%'][first][second] = 0
                    
    def _compute_PairDefPercentage(self):
        def_totals = self.pair_season_stats["DPP"]
        for first in def_totals.to_dict().keys():
            for second in def_totals.to_dict().keys():
                if def_totals[first][second] != 0:
                    self.pair_season_stats['D%'][first][second] = 100*def_totals[first][second]/def_totals[first][first]
                else:
                    self.pair_season_stats['D%'][first][second] = 0    

    def _compute_PairGoalAssist(self):
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].pair_tourney_stats["GA"]
            for first in tournament_value.keys():
                for second in tournament_value.keys():
                    self.pair_season_stats["GA"][first][second] = self.pair_season_stats["GA"][first][second] + tournament_value[first][second]
    
    def _compute_PairBreaks(self):
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].pair_tourney_stats["BRK"]
            for first in tournament_value.keys():
                for second in tournament_value.keys():
                    self.pair_season_stats["BRK"][first][second] = self.pair_season_stats["BRK"][first][second] + tournament_value[first][second]

    def _compute_PairBreakPercentage(self):
        breaks = self.pair_season_stats["BRK"]
        def_totals = self.pair_season_stats["DPP"]
        for first in def_totals.to_dict().keys():
            for second in def_totals.to_dict().keys():
                if def_totals[first][second] != 0:
                    self.pair_season_stats['BRK%'][first][second] = breaks[first][second]/def_totals[first][second]
                else:
                    self.pair_season_stats['BRK%'][first][second] = 0    
                    
    def _compute_PairBreakPercentageMinusAverage(self):
        breaks = self.season_stats["BRK"]
        total_breaks = sum(breaks)/7
        d_points = self.season_stats["DPP"]
        total_d_points = sum(d_points)/7
        avg_breakPercentage = total_breaks/total_d_points
        
        breaks = self.pair_season_stats["BRK"]
        def_totals = self.pair_season_stats["DPP"]
        for first in def_totals.to_dict().keys():
            for second in def_totals.to_dict().keys():
                if def_totals[first][second] != 0:
                    self.pair_season_stats['BRK%-AVG'][first][second] = breaks[first][second]/def_totals[first][second] - avg_breakPercentage
                else:
                    self.pair_season_stats['BRK%-AVG'][first][second] = 0

    def _compute_PairBreakAboveAverage(self):
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].pair_tourney_stats["BAA"]
            for first in tournament_value.keys():
                for second in tournament_value.keys():
                    self.pair_season_stats["BAA"][first][second] = self.pair_season_stats["BAA"][first][second] + tournament_value[first][second]
    
    def _compute_PairHolds(self):
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].pair_tourney_stats["HLD"]
            for first in tournament_value.keys():
                for second in tournament_value.keys():
                    self.pair_season_stats["HLD"][first][second] = self.pair_season_stats["HLD"][first][second] + tournament_value[first][second]

    def _compute_PairHoldPercentage(self):
        holds = self.pair_season_stats["HLD"]
        off_totals = self.pair_season_stats["OPP"]
        for first in off_totals.to_dict().keys():
            for second in off_totals.to_dict().keys():
                if off_totals[first][second] != 0:
                    self.pair_season_stats['HLD%'][first][second] = holds[first][second]/off_totals[first][second]
                else:
                    self.pair_season_stats['HLD%'][first][second] = 0
    
    def _compute_PairHoldPercentageMinusAverage(self):
        holds = self.season_stats["HLD"]
        total_holds = sum(holds)/7
        o_points = self.season_stats["OPP"]
        total_o_points = sum(o_points)/7
        avg_holdPercentage = total_holds/total_o_points
        
        holds = self.pair_season_stats["HLD"]
        off_totals = self.pair_season_stats["OPP"]
        for first in off_totals.to_dict().keys():
            for second in off_totals.to_dict().keys():
                if off_totals[first][second] != 0:
                    self.pair_season_stats['HLD%-AVG'][first][second] = holds[first][second]/off_totals[first][second] - avg_holdPercentage
                else:
                    self.pair_season_stats['HLD%-AVG'][first][second] = 0

    
    def _compute_PairHoldAboveAverage(self):
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].pair_tourney_stats["HAA"]
            for first in tournament_value.keys():
                for second in tournament_value.keys():
                    self.pair_season_stats["HAA"][first][second] = self.pair_season_stats["HAA"][first][second] + tournament_value[first][second]

    def _compute_PairTotalAboveAverage(self):
        for tournament in self.tournaments.keys():
            tournament_value = self.tournaments[tournament].pair_tourney_stats["TAA"]
            for first in tournament_value.keys():
                for second in tournament_value.keys():
                    self.pair_season_stats["TAA"][first][second] = self.pair_season_stats["TAA"][first][second] + tournament_value[first][second]

