import math, os
SITES = {}

#o = open('virtual2/virtual_station.dat', 'w')

def findloc(lat,lon):
  mindist = 100000.
  minstid = ''
  for id in SITES.keys():
    dist = math.sqrt(((lat - SITES[id]['lat'])**2 + (lon - SITES[id]['lon'])**2))
    if dist < mindist:
      mindist = dist
      minstid = id
  return minstid

for line in open('/mesonet/share/pickup/msdot/virtual_station.dat'):
  tokens = line.split(",")
  stid = tokens[0]
  SITES[stid] = {'lat' : float(tokens[3]), 'lon' : float(tokens[4])}

for line in open('/mesonet/share/pickup/msdot/station.dat'):
  tokens = line.split(",")
  stid = tokens[0]
  name = tokens[1].split("|")[0]
  lat = float(tokens[3])
  lon = float(tokens[4])
  bloc = findloc(lat,lon)
  print '%s,%s' % (name,bloc)
  #o.write("%05i,%s,%s,%s,%s,%s,20100101\n" % (10000 + int(stid),
  #  tokens[1], tokens[1].split("|")[0], lat, lon, tokens[5]))
  #os.system("cp virtual/%s.hcd virtual2/%s.hcd" % (bloc, 10000 + int(stid),))
#o.close()
