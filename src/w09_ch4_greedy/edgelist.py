class EdgeList:
    def __init__(self):
        self.graph=[]
    def append(self, vertex_from, vertex_to, weight):
        if vertex_from > vertex_to:
            vertex_from, vertex_to = vertex_to, vertex_from
        self.graph.append(( weight, vertex_from, vertex_to))
        self.graph.sort(key=lambda e: e[2])
    def __repr__(self):
        return str(self.graph)
    def __eq__(self, other):
        return self.graph == other.graph

e1 = EdgeList()
e1.append(1, 2, 300)
e1.append(5, 2, 250)
e2 = EdgeList()
e2.append(2, 5, 250)
e2.append(5, 2, 300)
print(f"{(e1==e2)=} {e1=} {e2=}")
