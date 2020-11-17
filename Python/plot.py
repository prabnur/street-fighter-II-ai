import matplotlib.pyplot as plt
import sys
import json
import numpy as np

# Usage: python plot.py title

statistics = {}
with open(f'Python/stats/{sys.argv[1]}.txt', 'r') as datafile:
    statistics = json.load(datafile)
if statistics: # non empty
    rounds = list(np.arange(len(statistics['average_rewards'])) + 1) # Adds 1 to all
    plt.clf()
    plt.title(statistics['title'])
    plt.plot(rounds, statistics['average_rewards'], 'b')
    # plt.plot(rounds, hp_differences, 'r')
    plt.ylabel('Average Reward')
    plt.xlabel('Round')
    plt.show()
    winrate = statistics['winrate']
    print(f'Winrate {winrate}')