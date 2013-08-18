# Leach Wunderground's archive

import urllib2, cookielib
from pyIEM import iemdb, mesonet
i = iemdb.iemdb()
asos = i['asos']
import mx.DateTime, csv, time
from metar import Metar
"""
    EGI  2008-12-18 21:55
"""

now = mx.DateTime.DateTime(1999,12,1)

lines = open('dec.txt', 'r').xreadlines()
for line in lines: # Skip header
    if line.strip() == "":
      continue
    mstr = line
    if len(mstr) > 200:
      continue
    try:
      mtr = Metar.Metar(mstr, now.month, now.year)
    except:
      continue
    sky = {'skyc1': "", 'skyc2': "", 'skyc3': "",
           'skyl1': "Null", 'skyl2': "Null", 'skyl3': "Null"}
    if mtr is not None and mtr.time is not None:
      if mtr.station_id[0] != 'K':
        continue
      stid = mtr.station_id[1:]
      gts = mx.DateTime.DateTime( mtr.time.year, mtr.time.month, 
                mtr.time.day, mtr.time.hour, mtr.time.minute)
      tmpf = "Null"
      if (mtr.temp):
        tmpf = mtr.temp.value("F")
      dwpf = "Null"
      if (mtr.dewpt):
        dwpf = mtr.dewpt.value("F")

      sknt = "Null"
      if mtr.wind_speed:
        sknt = mtr.wind_speed.value("KT")
      gust = "Null"
      if mtr.wind_gust:
        gust = mtr.wind_gust.value("KT")

      drct = "Null"
      if mtr.wind_dir and mtr.wind_dir.value() != "VRB":
        drct = mtr.wind_dir.value()

      vsby = "Null"
      if mtr.vis:
        vsby = mtr.vis.value("SM")

      alti = "Null"
      if mtr.press:
        alti = mtr.press.value("IN")

      p01m = 0
      if mtr.precip_1hr:
        p01m = mtr.precip_1hr.value("CM") * 10.0

      # Do something with sky coverage
      for i in range(len(mtr.sky)):
        (c,h,b) = mtr.sky[i]
        sky['skyc%s' % (i+1)] = c
        if h is not None:
          sky['skyl%s' % (i+1)] = h.value("FT")

      sql = """INSERT into t%s (station, valid, tmpf, dwpf, vsby, 
        drct, sknt, gust, p01m, alti, skyc1, skyc2, skyc3, 
        skyl1, skyl2, skyl3, metar) values ('%s','%s+00', %s, %s, %s, 
        %s, %s, %s, %s, %s, '%s', '%s', '%s', %s, %s, %s,'%s')""" % (now.year, 
        stid, gts.strftime("%Y-%m-%d %H:%M"), tmpf, dwpf, vsby, drct, 
        sknt, gust, p01m, alti, 
        sky['skyc1'], sky['skyc2'], sky['skyc3'],
        sky['skyl1'], sky['skyl2'], sky['skyl3'], mstr)
      asos.query("DELETE from t%s WHERE station = '%s' and valid = '%s+00'" % (now.year, stid, gts.strftime("%Y-%m-%d %H:%M")))
      try:
        asos.query(sql)
      except:
        print 'FAIL', stid, gts.strftime("%Y-%m-%d %H:%M")

