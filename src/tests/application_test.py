import unittest
from data_for_app import data_for_app
from dijkstra import dijkstra
from min_heap import MinHeap


class TestPathFindingApp(unittest.TestCase):
    def setUp(self):
        self.cities, self.coordinates, self.speedlimits, self.adjlist = data_for_app()
        self.adjlist1 = {}
        self.create_example_graph_1()
        self.heap1 = MinHeap()
    
    
    def create_example_graph_1(self):
        self.adjlist1['A'] = [('B',9), ('F',2)]
        self.adjlist1['B'] = [('C',7)]
        self.adjlist1['C'] = [('E',1)]
        self.adjlist1['D'] = [('C',4)]
        self.adjlist1['E'] = [('B',2), ('D',3)]
        self.adjlist1['F'] = [('B',5), ('E',1)]
    
    
    # Test Dijkstra's Algorithm - Distances
    def test_dijkstra_algorithm_on_graph_1_distances(self):
        distB, pathB = dijkstra('A', 'B', self.adjlist1)
        distC, pathC = dijkstra('A', 'C', self.adjlist1)
        distD, pathD = dijkstra('A', 'D', self.adjlist1)
        distE, pathE = dijkstra('A', 'E', self.adjlist1)
        distF, pathF = dijkstra('A', 'F', self.adjlist1)
        
        self.assertEqual( (distB,distC,distD,distE,distF) , (5,10,6,3,2) )
    
    
    # Test Dijkstra's Algorithm - Paths
    def test_dijkstra_algorithm_on_graph_1_paths(self):
        distB, pathB = dijkstra('A', 'B', self.adjlist1)
        distC, pathC = dijkstra('A', 'C', self.adjlist1)
        distD, pathD = dijkstra('A', 'D', self.adjlist1)
        distE, pathE = dijkstra('A', 'E', self.adjlist1)
        distF, pathF = dijkstra('A', 'F', self.adjlist1)
        
        self.assertEqual( (pathB,pathC,pathD,pathE,pathF) , (['A','F','E','B'],['A','F','E','D','C'],['A','F','E','D'],['A','F','E'],['A','F']) )
    
    
    # Test Min Heap - Insert
    def test_min_heap_1_insert(self):
        self.heap1 = MinHeap()
        
        min0 = self.heap1.get_min()     # None
        
        self.heap1.insert(7)
        min1 = self.heap1.get_min()     # 7
        
        self.heap1.insert(8)
        min2 = self.heap1.get_min()     # 7
        
        self.heap1.insert(13)
        min3 = self.heap1.get_min()     # 7
        
        self.heap1.insert(3)
        min4 = self.heap1.get_min()     # 3
        
        self.heap1.insert(7)
        min5 = self.heap1.get_min()     # 3
        
        self.heap1.insert(12)
        min6 = self.heap1.get_min()     # 3
        
        self.heap1.insert(2)
        min7 = self.heap1.get_min()     # 2
        
        self.heap1.insert(9)
        min8 = self.heap1.get_min()     # 2
        
        self.heap1.insert(15)
        min9 = self.heap1.get_min()     # 2
        
        self.heap1.insert(8)
        min10 = self.heap1.get_min()    # 2
        
        self.assertEqual( (min0,min1,min2,min3,min4,min5,min6,min7,min8,min9,min10) , (None,7,7,7,3,3,3,2,2,2,2) )


    # Test Min Heap - Pop
    def test_min_heap_1_pop(self):
        self.heap1 = MinHeap()
        self.heap1.insert(7)
        self.heap1.insert(8)
        self.heap1.insert(13)
        self.heap1.insert(3)
        self.heap1.insert(7)
        self.heap1.insert(12)
        self.heap1.insert(2)
        self.heap1.insert(9)
        self.heap1.insert(15)
        self.heap1.insert(8)
        
        pop10 = self.heap1.pop_min()    # 2
        pop9 = self.heap1.pop_min()     # 3
        pop8 = self.heap1.pop_min()     # 7
        pop7 = self.heap1.pop_min()     # 7
        pop6 = self.heap1.pop_min()     # 8
        pop5 = self.heap1.pop_min()     # 8
        pop4 = self.heap1.pop_min()     # 9
        pop3 = self.heap1.pop_min()     # 12
        pop2 = self.heap1.pop_min()     # 13
        pop1 = self.heap1.pop_min()     # 15
        pop0 = self.heap1.pop_min()     # None
        
        self.assertEqual( (pop10,pop9,pop8,pop7,pop6,pop5,pop4,pop3,pop2,pop1,pop0) , (2,3,7,7,8,8,9,12,13,15,None) )
        
        
        