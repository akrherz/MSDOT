#!/mesonet/python/bin/python
# Generate .hcd file for Pavement Design Guide

#YYYYMMDDHH,Temperature (F),Wind speed (mph),% Sun shine, Precipitation, Relative humidity.

pcsun = {
 -9999: 0,
     0: 100,
     1: 88,
     2: 75,
     3: 62,
     4: 50,
     5: 38,
     6: 25,
     7: 13,
     8:  0,
     9:  0,
}

import mx.DateTime, sys
from pyIEM import iemdb, mesonet
i = iemdb.iemdb()
asos = i['asos']

stid = sys.argv[1]
out = open("%s.dat" % (stid,), 'w')
fmt = "%s,%s,%.1f,%s,%s,%.1f\n"
missing = 0
now = mx.DateTime.DateTime(1972,12,31,23)
for yr in range(1973,2007):
  sql = "SELECT *, \
   case when sknt > 0 THEN sknt ELSE 0 END as sknt0,\
   case when p01m > 0 THEN p01m ELSE 0 END as p,\
   case when skyc > -1 THEN skyc ELSE 0 END as sk from t%s WHERE station = '%s' and tmpf > -50 and extract(year from valid) = %s ORDER by valid ASC" % (yr,stid,yr)
  rs = asos.query(sql).dictresult()
  for i in range(len(rs)):
    ts = mx.DateTime.strptime(rs[i]['valid'][:13], "%Y-%m-%d %H")
    if (now == ts):
      #print 'DUP', now
      continue
    tmpf = rs[i]['tmpf']
    mph = rs[i]['sknt0'] / 1.18
    psun = pcsun[ int(rs[i]['sk']) ]
    phour = rs[i]['p'] * 25.4
    relh = mesonet.relh( rs[i]['tmpf'], rs[i]['dwpf'])
    if (relh == "M"):
      relh = 65
    while ((now + mx.DateTime.RelativeDateTime(hours=1)) < ts):
      now += mx.DateTime.RelativeDateTime(hours=1)
      #print 'MISSING', now
      missing += 1
      out.write( fmt % (now.strftime("%Y%m%d%H"),tmpf, mph, psun, phour, relh))

    out.write(fmt % (ts.strftime("%Y%m%d%H"), tmpf, mph, psun, phour, relh))

    now = ts
out.close()
print 'Total missing:', missing
