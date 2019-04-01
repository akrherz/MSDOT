import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
from matplotlib.patches import Polygon, Circle


m = Basemap(llcrnrlon=-91.9,llcrnrlat=30.0,urcrnrlon=-88.,urcrnrlat=35.1,
            projection='lcc',lat_1=30,lat_2=33,lon_0=-90)

shp_info = m.readshapefile('mscnty','counties',drawbounds=True)

# Draw zone polygons
ax = plt.gca()
x,y = -88.92, 30.42
buf = 1.0
poly = Polygon((m(x-(3*buf),y-buf),m(x-(3*buf),y+buf),m(x+(3*buf),y+buf),m(x+(3*buf),y-buf),m(x-buf,y-buf)),facecolor='r',edgecolor='r')
ax.add_patch(poly)

x,y = -89.54, 34.42
poly = Polygon((m(x-3*buf,y-buf),m(x-3*buf,y+buf),m(x+3*buf,y+buf),m(x+3*buf,y-buf),m(x-3*buf,y-buf)),facecolor='g',edgecolor='g')
ax.add_patch(poly)

x,y = -89.22, 32.42
poly = Polygon((m(x-3*buf,y-buf),m(x-3*buf,y+buf),m(x+3*buf,y+buf),m(x+3*buf,y-buf),m(x-3*buf,y-buf)),facecolor='y',edgecolor='y')
ax.add_patch(poly)

virtual = [(31.180,-90.802),(33.658,-88.773),(30.866,-88.640),
           (32.407,-88.664),(32.756,-89.523),(34.770,-89.497),
           (30.775,-89.582),(34.257,-90.288),(32.784,-90.389)]
for pr in virtual:
  c = Circle( m(pr[1],pr[0]), 10000)
  ax.add_patch(c)


plt.title('Mississippi Virtual Climate Files Locations')
plt.savefig('test.png')

