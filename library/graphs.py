from .globalvars import *

class Graph(Protocol):
    def neighbors(self, id: LOCATION) -> List[LOCATION]: pass

class WeightedGraph(Graph):
    def cost(self, from_id: LOCATION, to_id: LOCATION) -> float: pass