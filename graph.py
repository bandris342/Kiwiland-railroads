class GraphClass:
    """This is a general class with some basic graph methods"""

    def __init__(self):
        self.graph = {} #Create a dictionary to stock nodes and routes
        self.NbEdges = 0

    def addroute(self, A, B, distance):
        """Add a new route between two nodes"""
        if A in self.graph: #Check if the A node exists already
            self.graph[A].update({B : distance})
        else:
            self.graph.update({A : {B : distance}})
        self.NbEdges+=1

    def getdistance(self, A, B):
        """"Get the distance between A and B"""
        if B in self.graph[A]:
            return int(self.graph[A][B])
        else:
            return -1 #If no route between A and B, return -1

    def getroutesfrom(self, A):
        """Get the list of directly accessible nodes from A"""
        if A in self.graph:
            return self.graph[A]
