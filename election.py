from random import random
total_wins = 
for i in range(10000):
  region_wins = 0
  region_1 = random()
  if region_1 <= .87:
    region_wins = region_wins + 1
  else:
    region_wins = region_wins
  region_2 = random()
  if region_2 <= .65:
    region_wins = region_wins + 1
  else:
    region_wins = region_wins
  region_3 = random()
  if region_3 <= .17:
    region_wins = region_wins + 1
  else:
    region_wins = region_wins
    
  if region_wins >= 2:
    print 
  else:
    print "You did not win the election..."
