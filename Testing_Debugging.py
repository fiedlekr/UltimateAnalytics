# -*- coding: utf-8 -*-
"""
Used to test and debug the various classes.

Author: Kevin Fiedler
Date Created: 5/30/2022
Date Last Modified: 6/19/2022
"""

import Game, Tournament, Season
import matplotlib.pyplot as plt
import numpy as np


#Single game testing.
print("Single Game Testing")
filename = "Testing/2022_GandyGoose_SingleGame_Points.xlsx"
gandy_single = Game.Game()
gandy_single.add_PointsFromFile(filename)
#gandy_single.print_GameStats()
gandy_single.save_Stats("Testing/2022_GandyGoose_SingleGame_Stats.xlsx")
gandy_single.save_PairStats("Testing/2022_GandyGoose_SingleGame_PairStats.xlsx")

"""
#Make a graph showing goal scorers and assisters
pair_stats = gandy_single.pair_stats
data = pair_stats['GA']
plt.close('all')
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
plt.ylabel('Assister')
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90) 
plt.xlabel('Scorer')
plt.title('Goal and Assist Data')
plt.grid()
plt.colorbar()
plt.tight_layout()
plt.savefig('Testing/GoalAssistMap.png')
"""



"""
#Tournament testing.
print("Tournament Testing")
filename = "Testing/2022_GandyGoose_Points.xlsx"
gandy_goose = Tournament.Tournament()
gandy_goose.add_GamesFromFile(filename)
gandy_goose.save_Stats("Testing/2022_GandyGoose_Stats.xlsx")
gandy_goose.save_PairStats("Testing/2022_GandyGoose_PairStats.xlsx")


#Make a graph showing goal scorers and assisters
pair_stats = gandy_goose.pair_tourney_stats
data = pair_stats['GA']
plt.close('all')
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
plt.ylabel('Assister')
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
plt.xlabel('Scorer')
plt.title('Goal and Assist Data')
plt.grid()
plt.colorbar()
plt.set_cmap('binary')
plt.tight_layout()
plt.savefig('Testing/GoalAssistMap.png', dpi=300)

#Make a graph showing TAA
pair_stats = gandy_goose.pair_tourney_stats
data = pair_stats['TAA']
plt.figure()
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
#plt.ylabel('Assister')
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
#plt.xlabel('Scorer')
plt.title('Total Above Average (TAA)')
plt.grid()
plt.colorbar()
plt.set_cmap('bwr')
plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
plt.tight_layout()
plt.savefig('Testing/TAA_Map.png', dpi=300)
"""

"""
#Season testing.
print("Season Testing")
filenames = ["PointData/2022_GandyGoose_Points.xlsx", "PointData/2022_LogJam_Points.xlsx", "PointData/2022_MixedMastersRegionals_Points.xlsx"]
season = Season.Season()
season.add_TournamentsFromFiles(filenames)

#Make a graph showing goal scorers and assisters
pair_stats = season.pair_season_stats
data = pair_stats['GA']
plt.close('all')
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
plt.ylabel('Assister')
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
plt.xlabel('Scorer')
plt.title('Goal and Assist Data')
plt.grid()
plt.colorbar()
plt.set_cmap('binary')
plt.tight_layout()
plt.savefig('Testing/GoalAssistMap.png', dpi=300)

#Make a graph showing TAA
data = pair_stats['TAA']
plt.figure()
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
#plt.ylabel('Assister')
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
#plt.xlabel('Scorer')
plt.title('Total Above Average (TAA)')
plt.grid()
plt.colorbar()
plt.set_cmap('bwr')
plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
plt.tight_layout()
plt.savefig('Testing/TAA_Map.png', dpi=300)

"""