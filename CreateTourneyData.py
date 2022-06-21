# -*- coding: utf-8 -*-
"""
Compute the statistics for all the tournaments.

Author: Kevin Fiedler
Date Created: 6/6/2022
Date Last Modified: 6/6/2022
"""

from Tournament import Tournament
import matplotlib.pyplot as plt
import numpy as np



print("2022 - Gandy Goose")
filename = "PointData/2022_GandyGoose_Points.xlsx"
gandy_goose = Tournament(name="2022 Gandy Goose", games=[])
gandy_goose.add_GamesFromFile(filename)
gandy_goose.save_TourneyStats("Stats/2022_GandyGoose_Stats.xlsx")
gandy_goose.save_PairTourneyStats("Stats/2022_GandyGoose_PairStats.xlsx")

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
plt.savefig('Plots/2022_GandyGoose_GoalAssist_Map.png', dpi=300)

#Make a graph showing BAA for pairs
data = pair_stats['BAA']
plt.figure()
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
plt.title('Breaks Above Average (BAA)')
plt.grid()
plt.colorbar()
plt.set_cmap('bwr')
plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
plt.tight_layout()
plt.savefig('Plots/2022_GandyGoose_BAA_Map.png', dpi=300)

#Make a graph showing HAA for pairs
data = pair_stats['HAA']
plt.figure()
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
plt.title('Holds Above Average (HAA)')
plt.grid()
plt.colorbar()
plt.set_cmap('bwr')
plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
plt.tight_layout()
plt.savefig('Plots/2022_GandyGoose_HAA_Map.png', dpi=300)

#Make a graph showing TAA for pairs
data = pair_stats['TAA']
plt.figure()
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
plt.title('Total Above Average (TAA)')
plt.grid()
plt.colorbar()
plt.set_cmap('bwr')
plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
plt.tight_layout()
plt.savefig('Plots/2022_GandyGoose_TAA_Map.png', dpi=300)



print("2022 - Log Jam")
filename = "PointData/2022_LogJam_Points.xlsx"
log_jam = Tournament(name="2022 Log Jam", games=[])
log_jam.add_GamesFromFile(filename)
log_jam.save_TourneyStats("Stats/2022_LogJam_Stats.xlsx")
log_jam.save_PairTourneyStats("Stats/2022_LogJam_PairStats.xlsx")

#Make a graph showing goal scorers and assisters
pair_stats = log_jam.pair_tourney_stats
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
plt.savefig('Plots/2022_LogJam_GoalAssist_Map.png', dpi=300)

#Make a graph showing BAA for pairs
data = pair_stats['BAA']
plt.figure()
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
plt.title('Breaks Above Average (BAA)')
plt.grid()
plt.colorbar()
plt.set_cmap('bwr')
plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
plt.tight_layout()
plt.savefig('Plots/2022_LogJam_BAA_Map.png', dpi=300)

#Make a graph showing BAA for pairs
data = pair_stats['HAA']
plt.figure()
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
plt.title('Holds Above Average (HAA)')
plt.grid()
plt.colorbar()
plt.set_cmap('bwr')
plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
plt.tight_layout()
plt.savefig('Plots/2022_LogJam_HAA_Map.png', dpi=300)

#Make a graph showing TAA for pairs
data = pair_stats['TAA']
plt.figure()
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
plt.title('Total Above Average (TAA)')
plt.grid()
plt.colorbar()
plt.set_cmap('bwr')
plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
plt.tight_layout()
plt.savefig('Plots/2022_LogJam_TAA_Map.png', dpi=300)



print("2022 - Mixed Masters Regionals")
filename = "PointData/2022_MixedMasterRegionals_Points.xlsx"
mixed_masters = Tournament(name="2022 Mixed Masters Regionals", games=[])
mixed_masters.add_GamesFromFile(filename)
mixed_masters.save_TourneyStats("Stats/2022_MixedMasterRegionals_Stats.xlsx")
mixed_masters.save_PairTourneyStats("Stats/2022_MixedMasterRegionals_PairStats.xlsx")

#Make a graph showing goal scorers and assisters
pair_stats = mixed_masters.pair_tourney_stats
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
plt.savefig('Plots/2022_MixedMasterRegionals_GoalAssist_Map.png', dpi=300)

#Make a graph showing BAA for pairs
data = pair_stats['BAA']
plt.figure()
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
plt.title('Breaks Above Average (BAA)')
plt.grid()
plt.colorbar()
plt.set_cmap('bwr')
plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
plt.tight_layout()
plt.savefig('Plots/2022_MixedMasterRegionals_BAA_Map.png', dpi=300)

#Make a graph showing HAA for pairs
data = pair_stats['HAA']
plt.figure()
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
plt.title('Holds Above Average (HAA)')
plt.grid()
plt.colorbar()
plt.set_cmap('bwr')
plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
plt.tight_layout()
plt.savefig('Plots/2022_MixedMasterRegionals_HAA_Map.png', dpi=300)

#Make a graph showing TAA for pairs
data = pair_stats['TAA']
plt.figure()
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
plt.title('Total Above Average (TAA)')
plt.grid()
plt.colorbar()
plt.set_cmap('bwr')
plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
plt.tight_layout()
plt.savefig('Plots/2022_MixedMasterRegionals_TAA_Map.png', dpi=300)