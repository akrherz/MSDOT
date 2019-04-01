import pg
from pyIEM import mesonet

asos = pg.connect('asos', 'iemdb', user='nobody')

rs = asos.query("SELECT extract(month from valid) as m, avg(tmpf) as t from alldata where station = 'TUP' and valid between '1979-01-01' and '1989-01-01' and tmpf > -50 GROUP by m ORDER by m ASC").dictresult()
for i in range(len(rs)):
 print mesonet.f2k(rs[i]['t'])
