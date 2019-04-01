import netCDF3
from matplotlib import pyplot as plt
import numpy
from scipy import stats

def k2f(ar):
  return (ar - 273.5 ) * 9.0/5.0 + 32.0

cnc = netCDF3.Dataset("HDC_30.42_88.92_temp_humid.out.nc", 'r')
ctas = cnc.variables["tas"]

fnc = netCDF3.Dataset("SNR_30.42_88.92_temp_humid.out.nc", 'r')
ftas = fnc.variables["tas"]


fig = plt.figure()
ax = fig.add_subplot(111)
width = 0.35


n, bins, patches = ax.hist(numpy.ravel( ctas[:] - 273.15 ), 50, normed=1, histtype='step', label='Contemporary')
n2, bins2, patches2 = ax.hist(numpy.ravel( ftas[:] - 273.15 ), 50, normed=1, histtype='step', label='Future')
plt.legend(loc=2)
#ax.legend((bins[0],bins[1]), ("Contemporary", "Future"))

#ax.set_xticklabels( range(1970,2010,5) )
ax.set_xlabel("$\mathrm{Temperature}\hspace{0.6}^{\circ}\mathrm{C}$")
ax.set_ylabel("Frequency")
ax.set_title("Temperature Distribution for Mississippi")

#ax.set_ylim( 40, 90 )
ax.grid( True )

fig.savefig("test.png")

