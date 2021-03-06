
from matplotlib import pyplot as plt
import numpy
from scipy import stats
import netCDF3

data = []
nc = netCDF3.Dataset("NCP_28.22_89.62_temp_humid.out.mon.nc")
data.append( nc.variables['tas'][:] )
nc.close()
nc = netCDF3.Dataset("NCP_30.42_88.92_temp_humid.out.mon.nc")
data.append( nc.variables['tas'][:] )
nc.close()
nc = netCDF3.Dataset("NCP_34.38_89.54_temp_humid.out.mon.nc")
data.append( nc.variables['tas'][:] )
nc.close()

fig = plt.figure()
ax = fig.add_subplot(111)

width = 0.20
bar1 = ax.bar( numpy.arange(12), data[0] - 273.15, width, color='b' )
bar2 = ax.bar( numpy.arange(12) + width, data[1] - 273.15, width, color='g' )
bar3 = ax.bar( numpy.arange(12) + (width *2.), data[2] - 273.15, width, color='r' )

ax.set_xticks( numpy.arange(12) + width)
ax.set_xticklabels( ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"] )
ax.set_ylabel("Temperature [C]")
ax.set_ylabel("$\mathrm{Temperature}\hspace{0.6}^{\circ}\mathrm{C}$")
#ax.set_xlabel("Month")
ax.set_title("Mississippi Average Monthly Temperature Change\nReanalysis Run")
ax.grid(True)
ax.legend( (bar1[0], bar2[0], bar3[0]), ('Gulf', 'Biloxi', 'Tupelo') , loc=2, ncol=3)
ax.set_ylim(0,35)


fig.savefig("test.png")

