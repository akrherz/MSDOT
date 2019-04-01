
from matplotlib import pyplot as plt
import numpy
from scipy import stats
import netCDF3

nc = netCDF3.Dataset("SNR_30.42_88.92_water.out.mon.nc")
futured = nc.variables['pr'][:] * 240.
nc.close()

nc = netCDF3.Dataset("HDC_30.42_88.92_water.out.mon.nc")
contemp = nc.variables['pr'][:] * 240.
nc.close()

fig = plt.figure()
ax = fig.add_subplot(211)

width = 0.30
bar1 = ax.bar( numpy.arange(12) + width, futured, width, color='r' )

bar2 = ax.bar( numpy.arange(12), contemp, width, color='b' )

ax.set_xticks( numpy.arange(12) + width)
ax.set_xticklabels( ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"] )
ax.set_ylabel("Precipitation [mm]")
#ax.set_ylabel("$\mathrm{Temperature}\hspace{0.6}^{\circ}\mathrm{C}$")
#ax.set_xlabel("Month")
ax.set_title("Mississippi Average Monthly Precipitation Change")
ax.grid(True)
ax.legend( (bar1[0], bar2[0]), ('Future', 'Contemporary'), loc=2)
#ax.set_ylim(0,35)

ax2 = fig.add_subplot(212)

bar3 = ax2.bar( numpy.arange(12), futured - contemp, width * 2., color='000' )
ax2.set_xticks( numpy.arange(12) + (width ))
ax2.set_xticklabels( ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"] )
ax2.set_ylabel("$\mathrm{Precipitation}\hspace{0.6}\Delta\mathrm{mm}$")
ax2.grid(True)

print futured - contemp
print (futured - contemp) / contemp * 100.

fig.savefig("test.png")

