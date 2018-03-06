import unittest
from GraphAlgos import *

class KiwilandRailTest(unittest.TestCase):

    def setUp(self):
        input = "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"
        self.G = GraphfromString()
        self.G.create(input)


    def test_GetDistance(self):

        # Test 1:
        self.assertEqual(self.G.GetDistanceofRoute("A-B-C"),9)

        # Test 2:
        self.assertEqual(self.G.GetDistanceofRoute("A-D"),5)

        # Test 3:
        self.assertEqual(self.G.GetDistanceofRoute("A-D-C"),13)

        # Test 4:
        self.assertEqual(self.G.GetDistanceofRoute("A-E-B-C-D"),22)

        # Test 5:
        self.assertEqual(self.G.GetDistanceofRoute("A-E-D"),"NO SUCH ROUTE")

    def test_NbofTrips(self):

        # Test 6:
        self.assertEqual(self.G.GetNumofTripsMaxStep("C", "C", 3), 2)

        # Test 7:
        self.assertEqual(self.G.GetNumofTripsFixStep("A", "C", 4), 3)

    def test_ShortestRoute(self):

        # Test 8:
        self.assertEqual(self.G.GetShortestRoute("A", "C"), 9)

        # Test 9:
        self.assertEqual(self.G.GetShortestRoute("B", "B"), 9)

    def test_NbofTripsMaxDistance(self):

        # Test 10:
        self.assertEqual(self.G.GetNumofTripsMaxDist("C", "C", 30), 7)


if __name__ == '__main__':
    unittest.main()
