import csv, pickle

with open('OccupancyData.csv', newline='') as f: #4 is block 5 is lot 16 is long 17 is lat
    reader = csv.reader(f)
    OccupancyData = list(reader)

with open('TaxData2014.csv', newline='') as f: # 0 is block 1 is low 3 is tax
    reader = csv.reader(f)
    TaxData = list(reader)

occD = []
occ2d = {}

for b in OccupancyData:
    occD.append((b[4], b[5]))
    occ2d[(b[4], b[5])] = [b[16], b[17]]

taxD = []
tax2d = {}
for d in TaxData:
    taxD.append((d[0], d[1]))
    tax2d[(d[0], d[1])] = [d[3]]

i = 0

outData = []

for d in taxD:
    pass
    if d in occD:
        i = i + 1
        outData.append((d[0], d[1], tax2d[d][0], occ2d[d][0],occ2d[d][1] ))


file = open('data', 'wb')
pickle.dump(outData, file)
file.close()




print(i)