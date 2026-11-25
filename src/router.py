"""Prototype for accessible campus routing. Standard-library only."""
from dataclasses import dataclass
from heapq import heappush, heappop
from typing import Dict, List, Tuple, Optional
import json

@dataclass(frozen=True)
class Edge:
    a: str; b: str; minutes: float; slope: float=0.0; stairs: bool=False; surface: str="paved"

class Graph:
    def __init__(self): self.adj: Dict[str,List[Tuple[str,Edge]]] = {}
    def add(self,e):
        self.adj.setdefault(e.a,[]).append((e.b,e)); self.adj.setdefault(e.b,[]).append((e.a,e))
    def nodes(self): return sorted(self.adj)

class RouteStrategy:
    name="base"
    def cost(self,e:Edge)->float: raise NotImplementedError
class FastestStrategy(RouteStrategy):
    name="fastest"
    def cost(self,e): return e.minutes
class AccessibleStrategy(RouteStrategy):
    name="accessible"
    def cost(self,e): return float('inf') if e.stairs else e.minutes*(1+2.5*e.slope)+(2 if e.surface=="rough" else 0)
class BalancedStrategy(RouteStrategy):
    name="balanced"
    def cost(self,e): return e.minutes*(1+0.8*e.slope)+(8 if e.stairs else 0)+(1.5 if e.surface=="rough" else 0)

class Router:
    """Dijkstra with pluggable edge cost; closures are excluded per request."""
    def __init__(self, graph:Graph): self.graph=graph
    def route(self, source:str, target:str, strategy:RouteStrategy, closed=())->dict:
        if source not in self.graph.adj or target not in self.graph.adj: raise ValueError("unknown endpoint")
        closed={frozenset(pair) for pair in closed}; dist={source:0.0}; prev={}; heap=[(0.0,source)]; visited=0
        while heap:
            d,u=heappop(heap)
            if d != dist.get(u): continue
            visited+=1
            if u==target: break
            for v,e in self.graph.adj[u]:
                if frozenset((e.a,e.b)) in closed: continue
                w=strategy.cost(e)
                if w==float('inf'): continue
                nd=d+w
                if nd < dist.get(v,float('inf')):
                    dist[v]=nd; prev[v]=(u,e); heappush(heap,(nd,v))
        if target not in dist: return {"found":False,"strategy":strategy.name,"source":source,"target":target,"path":[],"minutes":None,"score":None,"visited":visited}
        path=[target]; edges=[]; cur=target
        while cur!=source:
            p,e=prev[cur]; edges.append(e); path.append(p); cur=p
        path.reverse(); edges.reverse()
        minutes=sum(e.minutes for e in edges)
        return {"found":True,"strategy":strategy.name,"source":source,"target":target,"path":path,"minutes":round(minutes,2),"score":round(dist[target],2),"visited":visited,"stairs":sum(e.stairs for e in edges),"max_slope":max([e.slope for e in edges] or [0]),"segments":len(edges)}

def campus_graph():
    g=Graph()
    # Synthetic teaching map: edge time minutes; slope is a fraction (0.05 = 5%).
    for e in [
      Edge('Entrada','Plaza',3,.01), Edge('Plaza','Biblioteca',4,.02), Edge('Biblioteca','Aulas',3,.01),
      Edge('Plaza','Auditorio',2,.03), Edge('Auditorio','Aulas',3,.02), Edge('Plaza','Cafeteria',3,.01),
      Edge('Cafeteria','Aulas',4,.01), Edge('Biblioteca','Laboratorios',4,.02), Edge('Laboratorios','Aulas',3,.03),
      Edge('Entrada','Jardin',2,.02,False,'rough'), Edge('Jardin','Auditorio',2,.07,True,'rough'),
      Edge('Plaza','Jardin',3,.04,False,'rough'), Edge('Biblioteca','Cafeteria',2,.06,False,'rough'),
      Edge('Auditorio','Laboratorios',3,.05,False,'paved'), Edge('Cafeteria','Laboratorios',4,.02,False,'paved')]: g.add(e)
    return g

def demo():
    r=Router(campus_graph()); results=[]
    for s in (FastestStrategy(),AccessibleStrategy(),BalancedStrategy()): results.append(r.route('Entrada','Laboratorios',s))
    return results
if __name__=='__main__': print(json.dumps(demo(),ensure_ascii=False,indent=2))
