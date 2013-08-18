
import Ngl
import numpy

vals = [278.14, 280.87, 280.87]
lats = [31.39, 33.21, 33.57]
lons = [-92.29, -87.62, -86.75]

XAXIS = numpy.arange(-92., -88.25, 0.25)
YAXIS = numpy.arange(30.,25., 0.25)

grid = Ngl.natgrid(lons, lats, vals, XAXIS, YAXIS)
grid = Ngl.natgrid(lons, lats, vals, XAXIS, YAXIS)
