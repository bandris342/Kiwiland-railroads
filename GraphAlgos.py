from graph import *

class GraphfromString:
    """This class includes the creation a graph from a string input and
       complex graph algorithmes for the Kiwiland railroad exercises"""

    def create(self, InpString):
        """Create the Graph from a String input"""
        self.Graph = GraphClass()
        list_nodes = InpString.split(", ")
        for n in list_nodes:
            self.Graph.addroute(n[0], n[1], n[2:])


    def GetDistanceofRoute(self, RouteStr):
        """Calculate the distance of a given route ("A-B-C-D" format)"""
        list_nodes = RouteStr.split("-")
        dist = 0
        for i in range(len(list_nodes) -1):
            if self.Graph.getdistance(list_nodes[i], list_nodes[i+1]) != -1:
                dist+=self.Graph.getdistance(list_nodes[i], list_nodes[i+1])
            else:
                return "NO SUCH ROUTE"
        return dist


    def BreadthFirstTraversal(self, From, StepLimit, DistLimit):
        """This is a modified Breadth-first graph traversal algorithm using 
        limited depth (steps) and distance.
        Instead of the classical version, here the loops are allowed.
        It returns a list of accessible nodes in 1,2...StepLimit steps from
        the Start node with their distances (until DistLimit)."""
        list_nodes = []
        list_nodes.append({From : [0]}) #In 0 step we can reach only the starting point (distance=0)
        step = 0
        while (step < StepLimit) and (list_nodes[step] != {}):
            step += 1
            list_nodes.append({})
            for A in list_nodes[step-1]:
                for B in self.Graph.getroutesfrom(A):
                    for i in list_nodes[step-1][A]:     #Stock all of the possible routes and distances in a list
                        d = i + self.Graph.getdistance(A, B)
                        if d <= DistLimit:
                            if B not in list_nodes[step]:
                                list_nodes[step][B] = []
                            list_nodes[step][B].append(d)
        return list_nodes


    def GetNumofTripsMaxStep(self, A, B, MaxStep):
        """Calculate the number of trips from A to B with maximum MaxStep steps"""
        list_nodes=self.BreadthFirstTraversal(A, MaxStep, float('inf'))  #The distance is not limited
        num = 0
        for i in range(1,len(list_nodes)):
            if B in list_nodes[i]:
                num += len(list_nodes[i][B])
        return num


    def GetNumofTripsFixStep(self, A, B, Steps):  #Calculate the number of trips from A to B with Fix steps
        list_nodes = self.BreadthFirstTraversal(A, Steps, float('inf'))  #The distance is not limited
        return len(list_nodes[Steps][B])



    def GetShortestRoute(self, A, B):
        """To calculate the shortest route I'm using here again 
        the modified Breadth-first graph traversal algorithm.
        The StepLimit is the number of edges (this is the deepest 
        graph that we can theoretically create)."""
        list_nodes = self.BreadthFirstTraversal(A, self.Graph.NbEdges, float('inf'))
        DisMin=float('inf')    #Find the minimum distance between A and B
        for i in range(1, len(list_nodes)):
            if B in list_nodes[i]:
                if min(list_nodes[i][B]) < DisMin:
                    DisMin = min(list_nodes[i][B])
        return DisMin


    def GetNumofTripsMaxDist(self, A, B, MaxDist):
        """Calculate the number of trips from A to B with maximum MaxDist distance"""
        list_nodes = self.BreadthFirstTraversal(A, float('inf'), MaxDist-1)  #The step number is not limited, distance < MaxDist!
        num = 0
        for i in range(1,len(list_nodes)):
            if B in list_nodes[i]:
                num += len(list_nodes[i][B])
        return num


#Input string
input = "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"
#Create a Graph from the input string
G = GraphfromString()
G.create(input)

# Question 1
print(G.GetDistanceofRoute("A-B-C"))
# Question 2
print(G.GetDistanceofRoute("A-D"))
# Question 3
print(G.GetDistanceofRoute("A-D-C"))
# Question 4
print(G.GetDistanceofRoute("A-E-B-C-D"))
# Question 5
print(G.GetDistanceofRoute("A-E-D"))
# Question 6
print(G.GetNumofTripsMaxStep("C", "C", 3))
# Question 7
print(G.GetNumofTripsFixStep("A", "C", 4))
# Question 8
print(G.GetShortestRoute("A", "C"))
# Question 9
print(G.GetShortestRoute("B", "B"))
# Question 10
print(G.GetNumofTripsMaxDist("C", "C", 30))