import random
import os 
import csv

class Split(object):
     #represents one split in a race showing lat, long and culm time
    def __init__ (self, nylat=0, nylng=0, nyculmt=0, denlat=0, denlng=0, denculmt=0, chilat=0, chilng=0, chiculmt=0):
        self.nylat = nylat
        self.nylng = nylng
        self.nyculmt  = nyculmt
        self.denlat = denlat
        self.denlng = denlng
        self.denculmt = denculmt
        self.chilat = chilat
        self.chilng = chilng
        self.chiculmt = chiculmt

def racesplitpace():
     return random.randrange(200,725, 25)

cumulativetny = 0
cumulativetchi = 0
cumulativetden = 0
splits = []

with open('routes.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
         s = Split()

         cumulativetny = cumulativetny + racesplitpace()
         s.nyculmt = cumulativetny

         cumulativetchi = cumulativetchi + racesplitpace()
         s.chiculmt = cumulativetchi

         cumulativetden = cumulativetden + racesplitpace()
         s.denculmt = cumulativetden
         
         s.nylat = row[0]
         s.nylng = row[1]
         s.chilat = row[2]
         s.chilng = row[3]
         s.denlat = row [4]
         s.denlng = row [5]
         splits.append(s)

#output = "nylat,nylng,nyculmt,chilat,chilng,chiculmt,denlat,denlng,denculmt" + "\n"
for split in splits:
    row = "{},{},{},{},{},{},{},{},{} \n".format(split.nylat,split.nylng,split.nyculmt,split.chilat,split.chilng,split.chiculmt,split.denlat,split.denlng,split.denculmt)
    output = row #+ "\n"

o = "generatedroutes.csv"
f = open(o,"a")
f.write(output)
f.close

  



   

