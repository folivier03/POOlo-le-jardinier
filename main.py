from tomate import Tomate
from potato import Potato
from concombre import Pickle
from garden import Garden

g = Garden()
g.add(Tomate())
p = Pickle()
p.grow(8)
g.add(p)
print(g.seed)
