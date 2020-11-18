import matplotlib.pyplot as plt
import sys
import json
import numpy as np
import os

# Usage: python plot.py title

# statistics = {}
# with open(f'Python/stats/{sys.argv[1]}.txt', 'r') as datafile:
#     statistics = json.load(datafile)
# if statistics: # non empty
#     rounds = list(np.arange(len(statistics['average_rewards'])) + 1) # Adds 1 to all
#     plt.clf()
#     plt.title(statistics['title'])
#     plt.plot(rounds, statistics['average_rewards'], 'b')
#     # plt.plot(rounds, hp_differences, 'r')
#     plt.ylabel('Average Reward')
#     plt.xlabel('Round')
#     plt.show()
#     winrate = statistics['winrate']
#     print(f'Winrate {winrate}')

with os.scandir('Python/stats/') as entries:
  for entry in entries:
    # inp = input('Anotha one? ')
    # if inp == 'n':
    #   break
    statistics = {}
    with open(entry, 'r') as datafile:
      statistics = json.load(datafile)
    if statistics: # non empty
      rounds = list(np.arange(len(statistics['hp_differences'])) + 1) # Adds 1 to all
      title = statistics['title']
      plt.title(title)
      plt.plot(rounds, statistics['hp_differences'], 'b')
      # plt.plot(rounds, hp_differences, 'r')
      plt.ylabel('HP Difference')
      plt.xlabel('Round')
      # plt.show()
      plt.savefig(f'figures/{title}.png')
      plt.clf()
      winrate = statistics['winrate']
      print(f'Winrate {winrate}')
