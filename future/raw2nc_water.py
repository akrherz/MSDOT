# Need something to convert the text files from the RCM to netcdf

import netCDF3
import sys
import numpy
import mx.DateTime

fp = sys.argv[1]
t1979 = mx.DateTime.DateTime(1979,1,1)

nc = netCDF3.Dataset(fp+".nc", 'w')
nc.createDimension('time', 0)

tm = nc.createVariable('time', numpy.float, ('time',))
tm.units = 'hours since 1979-01-01 00:00:00+00'

pr = nc.createVariable('pr', numpy.float, ('time',))
pr.units = 'mm'

i = 0
for line in open(fp):
  tokens = line.split()
  if tokens[0] == "year":
    continue
  y, m, d, h = tokens[:4]
  #print y, m, d , h
  if int(m) == 2 and (int(d) == 29 or int(d) == 30 or int(d) == 31):
    continue
  ts = mx.DateTime.DateTime(1900+int(y),int(m),int(d),int(h))
  tm[i] = (ts - t1979).hours
  pr[i] = tokens[8]
  i += 1

nc.close()
