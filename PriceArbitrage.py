# Author : ShadowStriker

import sys

def detectArbitrage(filename):
	bet_details = open(filename, "r")
	lines = bet_details.readlines()
	count = 0
	best_odds1 = {}
	best_odds2 = {}
	for line in lines:
		if count != 0:
			bookie_odds = [word.strip() for word in line.split(',')]
			if len(best_odds1) > 0:
				odds1_key = getKey(best_odds1)
				best_odds_so_far = best_odds1[odds1_key]
				if (bookie_odds[1] > best_odds_so_far):
					best_odds1.pop(odds1_key);
					best_odds1[bookie_odds[0]] = bookie_odds[1]
			else:
				best_odds1[bookie_odds[0]] = bookie_odds[1]

			if len(best_odds2) > 0:
				odds2_key = getKey(best_odds2)
				best_odds_so_far = best_odds2[odds2_key]
				if (bookie_odds[2] > best_odds_so_far):
					best_odds2.pop(odds2_key);
					best_odds2[bookie_odds[0]] = bookie_odds[2]
			else:
				best_odds2[bookie_odds[0]] = bookie_odds[2]
		count += 1
	total_implied_probability = caclulateTotalImpliedProbability(getValue(best_odds1), getValue(best_odds2))
	if (total_implied_probability < 1):
		print("Arbitrage Exists using Odds1 " + str(best_odds1) + " and Odds2 " + str(best_odds2))
	else:
		print("No Arbitrage Exists")

 
def getKey(dict):
    templist = []
    for key in dict.keys():
        templist.append(key)
    return templist[0]

def getValue(dict):
    templist = []
    for value in dict.values():
        templist.append(value)
    return float(templist[0])

def caclulateTotalImpliedProbability(odds1, odds2):
	total_implied_probability = 1/odds1 + 1/odds2
	return total_implied_probability

detectArbitrage(sys.argv [1])
