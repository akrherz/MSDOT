
from matplotlib import pyplot as plt
import numpy
from scipy import stats


vals = numpy.array([[282.81,	281.52],
[283.95,	282.46],
[288.16,	284.95],
[291.26,	288.88],
[295.43,	292.72],
[297.76,	295.84],
[299.30,	296.55],
[298.41,	296.39],
[296.20,	294.32],
[291.86,	289.92],
[288.10,	286.08],
[283.94,	282.50]])

fig = plt.figure()
ax = fig.add_subplot(211)

width = 0.30
bar1 = ax.bar( numpy.arange(12) + width, vals[:,0] - 273.15, width, color='r' )

bar2 = ax.bar( numpy.arange(12), vals[:,1] - 273.15, width, color='b' )

ax.set_xticks( numpy.arange(12) + width)
ax.set_xticklabels( ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"] )
ax.set_ylabel("Temperature [C]")
ax.set_ylabel("$\mathrm{Temperature}\hspace{0.6}^{\circ}\mathrm{C}$")
#ax.set_xlabel("Month")
ax.set_title("Mississippi Average Monthly Temperature Change")
ax.grid(True)
ax.legend( (bar1[0], bar2[0]), ('Future', 'Contemporary') , loc=2, ncol=2)
ax.set_ylim(0,35)

ax2 = fig.add_subplot(212)

bar3 = ax2.bar( numpy.arange(12), vals[:,0] - vals[:,1], width * 2., color='000' )
ax2.set_xticks( numpy.arange(12) + (width ))
ax2.set_xticklabels( ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"] )
ax2.set_ylabel("$\mathrm{Temperature}\hspace{0.6}\Delta^{\circ}\mathrm{C}$")
ax2.grid(True)


fig.savefig("test.png")

