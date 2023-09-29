import random

total_four_costs = 12 * 12

owned_target_four_cost = 4
owned_other_four_cost = 8 #assuming all 8 other four costs are either on the board or on opponents boards/benches
#Assuming they do not have any of target 4 costs

benched_four_costs = 0

gold = 70
golden_ticket = True

def hit_four_cost(): 
    global owned_target_four_cost
    global gold 
    global total_four_costs
    global owned_other_four_cost
    benched_two_star = 0
    if (owned_target_four_cost >= 6):
        benched_two_star = 1
    if(0.15 > random.random()): #15% chance to hit a 4 cost at lvl 7
        if( ( (12 - owned_target_four_cost) / (total_four_costs - owned_target_four_cost - owned_other_four_cost) ) > (random.random()) ): #odds to roll target 4 cost out of pool of four costs
            owned_target_four_cost += 1
            gold -= 4
        else:
            if(gold >= 6 and 9 > (benched_two_star + owned_other_four_cost - 8)): #hit a 4 cost that isnt the target, so we buy it to increase our odds
               owned_other_four_cost += 1
               gold -= 4


def determine_odds(iter):
    global owned_target_four_cost
    global gold
    global owned_other_four_cost
    owned_target_four_cost = 4
    gold = 70
    while (gold >= 6):
        free_roll = True

        if (golden_ticket):
            free_roll = bool(random.getrandbits(1))

        if(free_roll == False):
            gold -= 2

        for a in range(0, 5):
            hit_four_cost()
            if (owned_target_four_cost >= 9):
                return True
            
        if(gold <= 6 and owned_other_four_cost > 8): #we're out of gold but we have extra non-target 4 costs
            owned_other_four_cost -= 1
            gold += 4
        
    return False

results = []
for x in range(100000):
    results.append(determine_odds(x))
    

successes = sum(results)
print(successes)