# -*- coding: utf-8 -*-
"""
Compute the statistics for a season.

Author: Kevin Fiedler
Date Created: 6/22/2022
Date Last Modified: 6/22/2022
"""

from Season import Season
import matplotlib.pyplot as plt
import numpy as np

print("2022 - Season")
tournaments = ["PointData/2022_GandyGoose_Points.xlsx", "PointData/2022_LogJam_Points.xlsx", "PointData/2022_MixedMastersRegionals_Points.xlsx"]
season = Season.Season()
season.add_TournamentsFromFiles(tournaments)
season.save_TourneyStats("Stats/2022_Season_Stats.xlsx")
season.save_PairTourneyStats("Stats/2022_Season_PairStats.xlsx")


#Make a graph showing goal scorers and assisters
pair_stats = season.pair_tourney_stats
data = pair_stats['GA']
plt.close('all')
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
plt.ylabel('Assister')
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
plt.xlabel('Scorer')
plt.title('2022 Season - Assist and Goal Data')
plt.grid()
plt.colorbar()
plt.set_cmap('binary')
plt.tight_layout()
plt.savefig('Plots/2022_Season_AssistGoal_Map.png', dpi=300)

#Make a graph showing BAA for pairs
data = pair_stats['BAA']
plt.figure()
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
plt.title('2022 Season - Breaks Above Average (BAA)')
plt.grid()
plt.colorbar()
plt.set_cmap('bwr')
plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
plt.tight_layout()
plt.savefig('Plots/2022_Season_BAA_Map.png', dpi=300)

#Make a graph showing HAA for pairs
data = pair_stats['HAA']
plt.figure()
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
plt.title('2022 Season - Holds Above Average (HAA)')
plt.grid()
plt.colorbar()
plt.set_cmap('bwr')
plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
plt.tight_layout()
plt.savefig('Plots/2022_Season_HAA_Map.png', dpi=300)

#Make a graph showing TAA for pairs
data = pair_stats['TAA']
plt.figure()
plt.imshow(data)
plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
plt.title('2022 Season - Total Above Average (TAA)')
plt.grid()
plt.colorbar()
plt.set_cmap('bwr')
plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
plt.tight_layout()
plt.savefig('Plots/22022_Season_TAA_Map.png', dpi=300)