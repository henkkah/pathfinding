import unittest
from dijkstra import dijkstra


class TestPathFindingApp(unittest.TestCase):
    def setUp(self):
        self.cities, self.coordinates, self.speedlimits, self.adjlist = data_for_app()
    
    def create_example_graph_1(self):
        adjlist = {}
        adjlist['A'] = [('B',9), ('F',2)]
        adjlist['B'] = [('C',7)]
        adjlist['C'] = [('E',1)]
        adjlist['D'] = [('C',4)]
        adjlist['E'] = [('B',2), ('D',3)]
        adjlist['F'] = [('B',5), ('E',1)]
        return adjlist
    
    def test_dijkstra_algorithm_on_graph_1_to_B_distance(self):
        adjlist = self.create_example_graph_1()
        distanceB, pathB = dijkstra('A', 'B', adjlist)
        self.assertEqual(distanceB, 5)
    
    def test_dijkstra_algorithm_on_graph_1_to_C_distance(self):
        adjlist = self.create_example_graph_1()
        distanceC, pathC = dijkstra('A', 'C', adjlist)
        self.assertEqual(distanceC, 10)

    def test_dijkstra_algorithm_on_graph_1_to_D_distance(self):
        adjlist = self.create_example_graph_1()
        distanceD, pathD = dijkstra('A', 'D', adjlist)
        self.assertEqual(distanceD, 6)

    def test_dijkstra_algorithm_on_graph_1_to_E_distance(self):
        adjlist = self.create_example_graph_1()
        distanceE, pathE = dijkstra('A', 'E', adjlist)
        self.assertEqual(distanceE, 3)

    def test_dijkstra_algorithm_on_graph_1_to_F_distance(self):
        adjlist = self.create_example_graph_1()
        distanceF, pathF = dijkstra('A', 'F', adjlist)
        self.assertEqual(distanceE, 2)

    def test_dijkstra_algorithm_on_graph_1_to_B_path(self):
        adjlist = self.create_example_graph_1()
        distanceB, pathB = dijkstra('A', 'B', adjlist)
        self.assertEqual(pathB, ['A', 'F', 'E', 'B'])

    def test_dijkstra_algorithm_on_graph_1_to_C_path(self):
        adjlist = self.create_example_graph_1()
        distanceC, pathC = dijkstra('A', 'C', adjlist)
        self.assertEqual(pathB, ['A', 'F', 'E', 'D', 'C'])

    def test_dijkstra_algorithm_on_graph_1_to_D_path(self):
        adjlist = self.create_example_graph_1()
        distanceD, pathD = dijkstra('A', 'D', adjlist)
        self.assertEqual(pathB, ['A', 'F', 'E', 'D'])

    def test_dijkstra_algorithm_on_graph_1_to_E_path(self):
        adjlist = self.create_example_graph_1()
        distanceE, pathE = dijkstra('A', 'E', adjlist)
        self.assertEqual(pathB, ['A', 'F', 'E'])

    def test_dijkstra_algorithm_on_graph_1_to_F_path(self):
        adjlist = self.create_example_graph_1()
        distanceF, pathF = dijkstra('A', 'F', adjlist)
        self.assertEqual(pathB, ['A', 'F'])


