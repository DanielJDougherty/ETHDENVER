import random

class Split(object):
     #represents one split in a race showing lat, long and culm time
    def __init__ (self, lat=0, lng=0, culmt=0):
        self.lat = lat
        self.long = lng
        self.culmt  = culmt

def racesplitpace():
     return random.randrange(244,466)

cumulativet = 0

for x in range(0, 2):
    #print(racesplitpace())
    s = Split()
    s.culmt =  cumulativet + racesplitpace()

    print(s.culmt)

