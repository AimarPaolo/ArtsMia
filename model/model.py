import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._artObjectsLsit = DAO.getAllObjects()
        self._grafo = nx.Graph()
        self._grafo.add_nodes_from(self._artObjectsLsit)
        self._idMap = {}
        for f in self._artObjectsLsit:
            self._idMap[f.object_id] = f

    def getConnessa(self, v0int):
        #io vorrei un oggetto non solo un intero
        v0 = self._idMap[v0int]
        #modo 1: successori di v0 in DFS
        allSucc = []
        successors = nx.dfs_successors(self._grafo, v0)
        for succ in successors.values():
            allSucc.extend(succ)
            # [[1,3,2,4],[2,5,2,5] append
            # [1, 3, 2, 4, 2, 5, 2, 5] extend
        #print(f"Metodo 1 (pred): {len(successors.values())}")
        print(f"Metodo 1 (pred): {len(allSucc)}")

        #modo 2 predecessori di v0 in DFS
        predecessors = nx.dfs_predecessors(self._grafo, v0)
        print(f"Metodo 2 (succ): {len(predecessors.values())}")

        #modo 3 conto i nodi dell'albero di visita
        tree = nx.dfs_tree(self._grafo, v0)
        print(f"Metodo 3 (tree): {len(tree.nodes)}")
        #il metodo 3 dà il risultato del 2 + 1 perchè conta anche il nodo di origine

        #modo 4: node_connected_component
        connComp = nx.node_connected_component(self._grafo, v0)
        print("Metodo 4: ", len(connComp))
        #ci restituisce un set() di nodi

        return len(connComp)


    def buildGraph(self):
        self.addEdges()

    def addEdges(self):
        self._grafo.clear_edges()
        allEdges = DAO.getAllConnessioni(self._idMap)
        for e in allEdges:
            self._grafo.add_edge(e.v1, e.v2, weigth=e.peso)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def getNumNodes(self):
        return len(self._grafo.nodes)
