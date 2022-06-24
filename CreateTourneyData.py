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


def make_pair_plots(tourney, base_filename):
    #Make a graph showing goal scorers and assisters
    pair_stats = tourney.pair_tourney_stats
    data = pair_stats['GA']
    plt.close('all')
    plt.imshow(data, origin='lower')
    plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
    plt.ylabel('Assister')
    plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
    plt.xlabel('Scorer')
    plt.title(str(base_filename) + ' Goal and Assist Data')
    plt.grid()
    plt.colorbar()
    plt.set_cmap('binary')
    plt.tight_layout()
    plt.savefig('Plots/' + str(base_filename) + '_AssistGoal_Map.png', dpi=300)

    #Make a graph showing BAA for pairs
    data = pair_stats['BAA']
    plt.figure()
    plt.imshow(data, origin='lower')
    plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
    plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
    plt.title(str(base_filename) + ' Breaks Above Average (BAA)')
    plt.grid()
    plt.colorbar()
    plt.set_cmap('bwr')
    plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
    plt.tight_layout()
    plt.savefig('Plots/' + str(base_filename) + '_BAA_Map.png', dpi=300)

    #Make a graph showing HAA for pairs
    data = pair_stats['HAA']
    plt.figure()
    plt.imshow(data, origin='lower')
    plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
    plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
    plt.title(str(base_filename) + ' Holds Above Average (HAA)')
    plt.grid()
    plt.colorbar()
    plt.set_cmap('bwr')
    plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
    plt.tight_layout()
    plt.savefig('Plots/' + str(base_filename) + '_HAA_Map.png', dpi=300)

    #Make a graph showing TAA for pairs
    data = pair_stats['TAA']
    plt.figure()
    plt.imshow(data, origin='lower')
    plt.yticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys())
    plt.xticks(ticks=range(0,len(data.to_dict().keys())), labels=data.to_dict().keys(), rotation=90)
    plt.title(str(base_filename) + ' Total Above Average (TAA)')
    plt.grid()
    plt.colorbar()
    plt.set_cmap('bwr')
    plt.clim([-np.ceil(np.max(data.values)), np.ceil(np.max(data.values))])
    plt.tight_layout()
    plt.savefig('Plots/' + str(base_filename) + '_TAA_Map.png', dpi=300)


print("2022 - Onion Fest")
filename = "PointData/2022_OnionFest_Points.xlsx"
base_filename = '2022_OnionFest'
tourney = Tournament(name=base_filename, games=[])
tourney.add_GamesFromFile(filename)
tourney.save_TourneyStats("Stats/" + str(base_filename) + "_Stats.xlsx")
tourney.save_PairTourneyStats("Stats/" + str(base_filename) + "_PairStats.xlsx")
make_pair_plots(tourney, base_filename)

print("2022 - Gandy Goose")
filename = "PointData/2022_GandyGoose_Points.xlsx"
base_filename = '2022_GandyGoose'
tourney = Tournament(name=base_filename, games=[])
tourney.add_GamesFromFile(filename)
tourney.save_TourneyStats("Stats/" + str(base_filename) + "_Stats.xlsx")
tourney.save_PairTourneyStats("Stats/" + str(base_filename) + "_PairStats.xlsx")
make_pair_plots(tourney, base_filename)

print("2022 - Log Jam")
filename = "PointData/2022_LogJam_Points.xlsx"
base_filename = '2022_LogJam'
tourney = Tournament(name=base_filename, games=[])
tourney.add_GamesFromFile(filename)
tourney.save_TourneyStats("Stats/" + str(base_filename) + "_Stats.xlsx")
tourney.save_PairTourneyStats("Stats/" + str(base_filename) + "_PairStats.xlsx")
make_pair_plots(tourney, base_filename)

print("2022 - Mixed Masters Regionals")
filename = "PointData/2022_MixedMastersRegionals_Points.xlsx"
base_filename = '2022_MixedMasters'
tourney = Tournament(name=base_filename, games=[])
tourney.add_GamesFromFile(filename)
tourney.save_TourneyStats("Stats/" + str(base_filename) + "_Stats.xlsx")
tourney.save_PairTourneyStats("Stats/" + str(base_filename) + "_PairStats.xlsx")
make_pair_plots(tourney, base_filename)
