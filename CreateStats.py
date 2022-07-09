# -*- coding: utf-8 -*-
"""
Compute the statistics for a season.

Author: Kevin Fiedler
Date Created: 6/22/2022
Date Last Modified: 7/9/2022
"""

from Tournament import Tournament
from Season import Season
import matplotlib.pyplot as plt
import numpy as np

def make_pair_plots(structure, base_filename):
    #Make a graph showing offensive points played
    pair_stats = structure.get_pair_stats()
    data = pair_stats['OPP']
    plt.close('all')
    plt.figure(figsize=(10, 10), dpi=600)
    plt.imshow(data, origin='lower')
    plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
    plt.ylabel('Player')
    plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
    plt.xlabel('Player')
    plt.title(str(base_filename) + ' Offensive Points Played')
    plt.grid()
    plt.colorbar()
    plt.set_cmap('binary')
    plt.tight_layout()
    plt.savefig('Plots/' + str(base_filename) + '_Points_Offense_Map.png', dpi=600)
    
    #Make a graph showing the defensive points played
    data = pair_stats['DPP']
    plt.close('all')
    plt.figure(figsize=(10, 10), dpi=600)
    plt.imshow(data, origin='lower')
    plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
    plt.ylabel('Player')
    plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
    plt.xlabel('Player')
    plt.title(str(base_filename) + ' Defensive Points Played')
    plt.grid()
    plt.colorbar()
    plt.set_cmap('binary')
    plt.tight_layout()
    plt.savefig('Plots/' + str(base_filename) + '_Points_Defense_Map.png', dpi=600)
    
    #Make a graph showing D% played with pairs
    data = pair_stats['D%']
    plt.close('all')
    plt.figure(figsize=(10, 10), dpi=600)
    plt.imshow(data, origin='lower')
    plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
    plt.ylabel('Player')
    plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
    plt.xlabel('Played with')
    plt.title(str(base_filename) + ' Defense Percentage')
    plt.grid()
    plt.colorbar()
    plt.set_cmap('binary')
    plt.tight_layout()
    plt.savefig('Plots/' + str(base_filename) + '_Points_D%_Map.png', dpi=600)
    
    #Make a graph showing O% played with pairs
    data = pair_stats['O%']
    plt.close('all')
    plt.figure(figsize=(10, 10), dpi=600)
    plt.imshow(data, origin='lower')
    plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
    plt.ylabel('Player')
    plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
    plt.xlabel('Played with')
    plt.title(str(base_filename) + ' Offense Percentage')
    plt.grid()
    plt.colorbar()
    plt.set_cmap('binary')
    plt.tight_layout()
    plt.savefig('Plots/' + str(base_filename) + '_Points_O%_Map.png', dpi=600)
    
    
    #Make a graph showing goal scorers and assisters
    data = pair_stats['GA']
    plt.close('all')
    plt.figure(figsize=(10, 10), dpi=600)
    plt.imshow(data, origin='lower')
    plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
    plt.ylabel('Assister')
    plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
    plt.xlabel('Scorer')
    plt.title(str(base_filename) + ' Goal and Assist Data (GA)')
    plt.grid()
    plt.colorbar()
    plt.set_cmap('binary')
    plt.tight_layout()
    plt.savefig('Plots/' + str(base_filename) + '_AssistGoal_Map.png', dpi=600)
    
    #Make a graph showing BRK% for pairs
    data = pair_stats['BRK%-AVG']
    plt.figure(figsize=(10, 10), dpi=600)
    plt.imshow(data, origin='lower')
    plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
    plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
    plt.title(str(base_filename) + ' Break Percentage Minus Average (BRK%-AVG)')
    plt.grid()
    plt.colorbar()
    plt.set_cmap('bwr')
    plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
    plt.tight_layout()
    plt.savefig('Plots/' + str(base_filename) + '_BRK%-AVG_Map.png', dpi=600)

    #Make a graph showing BAA for pairs
    data = pair_stats['BAA']
    plt.figure(figsize=(10, 10), dpi=600)
    plt.imshow(data, origin='lower')
    plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
    plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
    plt.title(str(base_filename) + ' Breaks Above Average (BAA)')
    plt.grid()
    plt.colorbar()
    plt.set_cmap('bwr')
    plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
    plt.tight_layout()
    plt.savefig('Plots/' + str(base_filename) + '_BAA_Map.png', dpi=600)
    
    #Make a graph showing HLD% for pairs
    data = pair_stats['HLD%-AVG']
    plt.figure(figsize=(10, 10), dpi=600)
    plt.imshow(data, origin='lower')
    plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
    plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
    plt.title(str(base_filename) + ' Hold Percentage Minus Average (HLD%-AVG)')
    plt.grid()
    plt.colorbar()
    plt.set_cmap('bwr')
    plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
    plt.tight_layout()
    plt.savefig('Plots/' + str(base_filename) + '_HLD%-AVG_Map.png', dpi=600)

    #Make a graph showing HAA for pairs
    data = pair_stats['HAA']
    plt.figure(figsize=(10, 10), dpi=600)
    plt.imshow(data, origin='lower')
    plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
    plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
    plt.title(str(base_filename) + ' Holds Above Average (HAA)')
    plt.grid()
    plt.colorbar()
    plt.set_cmap('bwr')
    plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
    plt.tight_layout()
    plt.savefig('Plots/' + str(base_filename) + '_HAA_Map.png', dpi=600)

    #Make a graph showing TAA for pairs
    data = pair_stats['TAA']
    plt.figure(figsize=(10, 10), dpi=600)
    plt.imshow(data, origin='lower')
    plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
    plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
    plt.title(str(base_filename) + ' Total Above Average (TAA)')
    plt.grid()
    plt.colorbar()
    plt.set_cmap('bwr')
    plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
    plt.tight_layout()
    plt.savefig('Plots/' + str(base_filename) + '_TAA_Map.png', dpi=600)
    
    plt.close('all')



print("2022 - Onion Fest")
filename = "PointData/2022_OnionFest_Points.xlsx"
base_filename = '2022_OnionFest'
tourney = Tournament(name=base_filename, games=[])
tourney.add_GamesFromFile(filename)
tourney.save_Stats("Stats/" + str(base_filename) + "_Stats.xlsx")
tourney.save_PairStats("Stats/" + str(base_filename) + "_PairStats.xlsx")
make_pair_plots(tourney, base_filename)

print("2022 - Gandy Goose")
filename = "PointData/2022_GandyGoose_Points.xlsx"
base_filename = '2022_GandyGoose'
tourney = Tournament(name=base_filename, games=[])
tourney.add_GamesFromFile(filename)
tourney.save_Stats("Stats/" + str(base_filename) + "_Stats.xlsx")
tourney.save_PairStats("Stats/" + str(base_filename) + "_PairStats.xlsx")
make_pair_plots(tourney, base_filename)

print("2022 - Log Jam")
filename = "PointData/2022_LogJam_Points.xlsx"
base_filename = '2022_LogJam'
tourney = Tournament(name=base_filename, games=[])
tourney.add_GamesFromFile(filename)
tourney.save_Stats("Stats/" + str(base_filename) + "_Stats.xlsx")
tourney.save_PairStats("Stats/" + str(base_filename) + "_PairStats.xlsx")
make_pair_plots(tourney, base_filename)

print("2022 - Mixed Masters Regionals")
filename = "PointData/2022_MixedMastersRegionals_Points.xlsx"
base_filename = '2022_MixedMasters'
tourney = Tournament(name=base_filename, games=[])
tourney.add_GamesFromFile(filename)
tourney.save_Stats("Stats/" + str(base_filename) + "_Stats.xlsx")
tourney.save_PairStats("Stats/" + str(base_filename) + "_PairStats.xlsx")
make_pair_plots(tourney, base_filename)

print("2022 - Sunbreak")
filename = "PointData/2022_Sunbreak_Points.xlsx"
base_filename = '2022_Sunbreak'
tourney = Tournament(name=base_filename, games=[])
tourney.add_GamesFromFile(filename)
tourney.save_Stats("Stats/" + str(base_filename) + "_Stats.xlsx")
tourney.save_PairStats("Stats/" + str(base_filename) + "_PairStats.xlsx")
make_pair_plots(tourney, base_filename)

print("2022 - Season")
tournaments = ["PointData/2022_OnionFest_Points.xlsx", "PointData/2022_GandyGoose_Points.xlsx", \
               "PointData/2022_LogJam_Points.xlsx", "PointData/2022_MixedMastersRegionals_Points.xlsx", \
               "PointData/2022_Sunbreak_Points.xlsx"]
base_filename = "2022_Season"
season = Season()
season.add_TournamentsFromFiles(tournaments)
season.save_Stats("Stats/" + str(base_filename) + "_Stats.xlsx")
season.save_PairStats("Stats/" + str(base_filename) + "_PairStats.xlsx")
make_pair_plots(season, base_filename)

