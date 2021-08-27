import unittest
from math import sqrt
from data_for_app import data_for_app
from dijkstra import dijkstra
from idastar import idastar
from min_heap import MinHeap


class TestPathFindingApp(unittest.TestCase):
    def setUp(self):
        self.cities, self.coordinates, self.speedlimits, self.adjlist = data_for_app()
        self.adjlist1 = {}
        self.create_example_graph_1()
        self.adjlist2 = {}
        self.create_example_graph_2()
        self.adjlist3 = {}
        self.coordinates3 = {}
        self.create_example_graph_3()
        self.heap1 = MinHeap()
    
    
    def create_example_graph_1(self):
        self.adjlist1['A'] = [('B',9), ('F',2)]
        self.adjlist1['B'] = [('C',7)]
        self.adjlist1['C'] = [('E',1)]
        self.adjlist1['D'] = [('C',4)]
        self.adjlist1['E'] = [('B',2), ('D',3)]
        self.adjlist1['F'] = [('B',5), ('E',1)]
    
    def create_example_graph_2(self):
        self.adjlist2['A'] = [('B',4), ('H',8)]
        self.adjlist2['B'] = [('A',4), ('C',8), ('H',11)]
        self.adjlist2['C'] = [('B',8), ('D',7), ('F',4), ('I',2)]
        self.adjlist2['D'] = [('C',7), ('E',9), ('F',14)]
        self.adjlist2['E'] = [('D',9), ('F',10)]
        self.adjlist2['F'] = [('C',4), ('D',14), ('E',10), ('G',2)]
        self.adjlist2['G'] = [('F',2), ('H',1), ('I',6)]
        self.adjlist2['H'] = [('A',8), ('B',11), ('G',1), ('I',7)]
        self.adjlist2['I'] = [('C',2), ('G',6), ('H',7)]
    
    def create_example_graph_3(self):
        self.adjlist3['A'] = [('F',sqrt(2))]
        self.adjlist3['B'] = [('C',1), ('D',sqrt(8)), ('F',5)]
        self.adjlist3['C'] = [('B',1), ('F',sqrt(26))]
        self.adjlist3['D'] = [('B',sqrt(8)), ('E',sqrt(52)), ('F',sqrt(13)), ('G',6)]
        self.adjlist3['E'] = [('D',sqrt(52)), ('G',4)]
        self.adjlist3['F'] = [('A',sqrt(2)), ('B',5), ('C',sqrt(26)), ('D',sqrt(13)), ('H',sqrt(17))]
        self.adjlist3['G'] = [('D',6), ('E',4), ('I',2)]
        self.adjlist3['H'] = [('F',sqrt(17)), ('I',sqrt(20))]
        self.adjlist3['I'] = [('G',2), ('H',sqrt(20))]
        self.coordinates3['A'] = (0/100,0/100)
        self.coordinates3['B'] = (6/100,1/100)
        self.coordinates3['C'] = (6/100,0/100)
        self.coordinates3['D'] = (4/100,3/100)
        self.coordinates3['E'] = (8/100,9/100)
        self.coordinates3['F'] = (1/100,1/100)
        self.coordinates3['G'] = (4/100,9/100)
        self.coordinates3['H'] = (0/100,5/100)
        self.coordinates3['I'] = (2/100,9/100)
    
    
    # Test Dijkstra's Algorithm 1 - Distances
    def test_dijkstra_algorithm_on_graph_1_distances(self):
        distB, pathB, timeB = dijkstra('A', 'B', self.adjlist1)
        distC, pathC, timeC = dijkstra('A', 'C', self.adjlist1)
        distD, pathD, timeD = dijkstra('A', 'D', self.adjlist1)
        distE, pathE, timeE = dijkstra('A', 'E', self.adjlist1)
        distF, pathF, timeF = dijkstra('A', 'F', self.adjlist1)
        
        self.assertEqual( (distB,distC,distD,distE,distF) , (5,10,6,3,2) )
    
    # Test Dijkstra's Algorithm 1 - Paths
    def test_dijkstra_algorithm_on_graph_1_paths(self):
        distB, pathB, timeB = dijkstra('A', 'B', self.adjlist1)
        distC, pathC, timeC = dijkstra('A', 'C', self.adjlist1)
        distD, pathD, timeD = dijkstra('A', 'D', self.adjlist1)
        distE, pathE, timeE = dijkstra('A', 'E', self.adjlist1)
        distF, pathF, timeF = dijkstra('A', 'F', self.adjlist1)
        
        self.assertEqual( (pathB,pathC,pathD,pathE,pathF) , (['A','F','E','B'],['A','F','E','D','C'],['A','F','E','D'],['A','F','E'],['A','F']) )


    # Test Dijkstra's Algorithm 2 - Distances
    def test_dijkstra_algorithm_on_graph_2_distances(self):
        distB, pathB, timeB = dijkstra('A', 'B', self.adjlist2)
        distC, pathC, timeC = dijkstra('A', 'C', self.adjlist2)
        distD, pathD, timeD = dijkstra('A', 'D', self.adjlist2)
        distE, pathE, timeE = dijkstra('A', 'E', self.adjlist2)
        distF, pathF, timeF = dijkstra('A', 'F', self.adjlist2)
        distG, pathG, timeG = dijkstra('A', 'G', self.adjlist2)
        distH, pathH, timeH = dijkstra('A', 'H', self.adjlist2)
        distI, pathI, timeI = dijkstra('A', 'I', self.adjlist2)
        
        self.assertEqual( (distB,distC,distD,distE,distF,distG,distH,distI) , (4,12,19,21,11,9,8,14) )
    
    # Test Dijkstra's Algorithm 2 - Paths
    def test_dijkstra_algorithm_on_graph_2_paths(self):
        distB, pathB, timeB = dijkstra('A', 'B', self.adjlist2)
        distC, pathC, timeC = dijkstra('A', 'C', self.adjlist2)
        distD, pathD, timeD = dijkstra('A', 'D', self.adjlist2)
        distE, pathE, timeE = dijkstra('A', 'E', self.adjlist2)
        distF, pathF, timeF = dijkstra('A', 'F', self.adjlist2)
        distG, pathG, timeG = dijkstra('A', 'G', self.adjlist2)
        distH, pathH, timeH = dijkstra('A', 'H', self.adjlist2)
        distI, pathI, timeI = dijkstra('A', 'I', self.adjlist2)
        
        self.assertEqual( (pathB,pathC,pathD,pathE,pathF,pathG,pathH,pathI) , (['A','B'],['A','B','C'],['A','B','C','D'],['A','H','G','F','E'],['A','H','G','F'],['A','H','G'],['A','H'],['A','B','C','I']) )    
    
    
    # Test IDA* Algorithm 3 - Distances
    def test_idastar_algorithm_on_graph_3_distances(self):
        distB, pathB, timeB = idastar('A', 'B', self.adjlist3, self.coordinates3)
        distC, pathC, timeC = idastar('A', 'C', self.adjlist3, self.coordinates3)
        distD, pathD, timeD = idastar('A', 'D', self.adjlist3, self.coordinates3)
        distE, pathE, timeE = idastar('A', 'E', self.adjlist3, self.coordinates3)
        distF, pathF, timeF = idastar('A', 'F', self.adjlist3, self.coordinates3)
        distG, pathG, timeG = idastar('A', 'G', self.adjlist3, self.coordinates3)
        distH, pathH, timeH = idastar('A', 'H', self.adjlist3, self.coordinates3)
        distI, pathI, timeI = idastar('A', 'I', self.adjlist3, self.coordinates3)
        resB = round(sqrt(2)+5,1)
        resC = round(sqrt(2)+sqrt(26),1)
        resD = round(sqrt(2)+sqrt(13),1)
        resE = round(sqrt(2)+sqrt(13)+sqrt(52),1)
        resF = round(sqrt(2),1)
        resG = round(sqrt(2)+sqrt(13)+6,1)
        resH = round(sqrt(2)+sqrt(17),1)
        resI = round(sqrt(2)+sqrt(17)+sqrt(20),1)
        
        self.assertEqual( (round(distB,1),round(distC,1),round(distD,1),round(distE,1),round(distF,1),round(distG,1),round(distH,1),round(distI,1)) , (resB,resC,resD,resE,resF,resG,resH,resI) )
    
    # Test IDA* Algorithm 3 - Paths
    def test_idastar_algorithm_on_graph_3_paths(self):
        distB, pathB, timeB = idastar('A', 'B', self.adjlist3, self.coordinates3)
        distC, pathC, timeC = idastar('A', 'C', self.adjlist3, self.coordinates3)
        distD, pathD, timeD = idastar('A', 'D', self.adjlist3, self.coordinates3)
        distE, pathE, timeE = idastar('A', 'E', self.adjlist3, self.coordinates3)
        distF, pathF, timeF = idastar('A', 'F', self.adjlist3, self.coordinates3)
        distG, pathG, timeG = idastar('A', 'G', self.adjlist3, self.coordinates3)
        distH, pathH, timeH = idastar('A', 'H', self.adjlist3, self.coordinates3)
        distI, pathI, timeI = idastar('A', 'I', self.adjlist3, self.coordinates3)
        
        self.assertEqual( (pathB,pathC,pathD,pathE,pathF,pathG,pathH,pathI) , (['A','F','B'],['A','F','C'],['A','F','D'],['A','F','D','E'],['A','F'],['A','F','D','G'],['A','F','H'],['A','F','H','I']) )
    
    
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
    
    
    # Test Paths on Dijkstra from Helsinki
    def test_paths_on_dijkstra_on_real_graph_from_helsinki(self):
        d, path_tampere, t = dijkstra('Helsinki', 'Tampere', self.adjlist)
        d, path_rauma, t = dijkstra('Helsinki', 'Rauma', self.adjlist)
        d, path_lappeenranta, t = dijkstra('Helsinki', 'Lappeenranta', self.adjlist)
        d, path_savonlinna, t = dijkstra('Helsinki', 'Savonlinna', self.adjlist)
        d, path_joensuu, t = dijkstra('Helsinki', 'Joensuu', self.adjlist)
        d, path_seinajoki, t = dijkstra('Helsinki', 'Seinajoki', self.adjlist)
        d, path_kajaani, t = dijkstra('Helsinki', 'Kajaani', self.adjlist)
        d, path_oulu, t = dijkstra('Helsinki', 'Oulu', self.adjlist)
        d, path_kilpisjarvi, t = dijkstra('Helsinki', 'Kilpisjarvi', self.adjlist)
        d, path_utsjoki, t = dijkstra('Helsinki', 'Utsjoki', self.adjlist)
        
        path_tampere_correct = ['Helsinki', 'Hyvinkaa', 'Hameenlinna', 'Toijala', 'Tampere']
        path_rauma_correct = ['Helsinki', 'Espoo', 'Palojarvi', 'Lohja', 'Salo', 'Turku', 'Rauma']
        path_lappeenranta_correct = ['Helsinki', 'Porvoo', 'Koskenkyla', 'Kouvola', 'Taavetti', 'Lappeenranta']
        path_savonlinna_correct = ['Helsinki', 'Mantsala', 'Lahti', 'Heinola', 'Mikkeli', 'Juva', 'Savonlinna']
        path_joensuu_correct = ['Helsinki', 'Mantsala', 'Lahti', 'Heinola', 'Mikkeli', 'Juva', 'Varkaus', 'Joensuu']
        path_seinajoki_correct = ['Helsinki', 'Hyvinkaa', 'Hameenlinna', 'Toijala', 'Tampere', 'Parkano', 'Jalasjarvi', 'Seinajoki']
        path_kajaani_correct = ['Helsinki', 'Mantsala', 'Lahti', 'Heinola', 'Mikkeli', 'Juva', 'Varkaus', 'Kuopio', 'Iisalmi', 'Kajaani']
        path_oulu_correct = ['Helsinki', 'Mantsala', 'Lahti', 'Heinola', 'Jyvaskyla', 'Aanekoski', 'Pyhajarvi', 'Karsamaki', 'Liminka', 'Oulu']
        path_kilpisjarvi_correct = ['Helsinki', 'Mantsala', 'Lahti', 'Heinola', 'Jyvaskyla', 'Aanekoski', 'Pyhajarvi', 'Karsamaki', 'Liminka', 'Oulu', 'Kemi', 'Keminmaa', 'Tornio', 'Pello', 'Kolari', 'Muonio', 'Kilpisjarvi']
        path_utsjoki_correct = ['Helsinki', 'Mantsala', 'Lahti', 'Heinola', 'Jyvaskyla', 'Aanekoski', 'Pyhajarvi', 'Karsamaki', 'Liminka', 'Oulu', 'Kemi', 'Keminmaa', 'Rovaniemi', 'Sodankyla', 'Ivalo', 'Utsjoki']
        
        self.assertEqual( (path_tampere, path_rauma, path_lappeenranta, path_savonlinna, path_joensuu, path_seinajoki, path_kajaani, path_oulu, path_kilpisjarvi, path_utsjoki) , 
                        (path_tampere_correct, path_rauma_correct, path_lappeenranta_correct, path_savonlinna_correct, path_joensuu_correct, 
                        path_seinajoki_correct, path_kajaani_correct, path_oulu_correct, path_kilpisjarvi_correct, path_utsjoki_correct) )
        
    # Test Paths on IDA* from Helsinki
    def test_paths_on_idastar_on_real_graph_from_helsinki(self):
        d, path_tampere, t = idastar('Helsinki', 'Tampere', self.adjlist, self.coordinates)
        d, path_rauma, t = idastar('Helsinki', 'Rauma', self.adjlist, self.coordinates)
        d, path_lappeenranta, t = idastar('Helsinki', 'Lappeenranta', self.adjlist, self.coordinates)
        d, path_savonlinna, t = idastar('Helsinki', 'Savonlinna', self.adjlist, self.coordinates)
        d, path_joensuu, t = idastar('Helsinki', 'Joensuu', self.adjlist, self.coordinates)
        d, path_seinajoki, t = idastar('Helsinki', 'Seinajoki', self.adjlist, self.coordinates)
        d, path_kajaani, t = idastar('Helsinki', 'Kajaani', self.adjlist, self.coordinates)
        d, path_oulu, t = idastar('Helsinki', 'Oulu', self.adjlist, self.coordinates)
        d, path_kilpisjarvi, t = idastar('Helsinki', 'Kilpisjarvi', self.adjlist, self.coordinates)
        d, path_utsjoki, t = idastar('Helsinki', 'Utsjoki', self.adjlist, self.coordinates)
        
        path_tampere_correct = ['Helsinki', 'Hyvinkaa', 'Hameenlinna', 'Toijala', 'Tampere']
        path_rauma_correct = ['Helsinki', 'Espoo', 'Palojarvi', 'Lohja', 'Salo', 'Turku', 'Rauma']
        path_lappeenranta_correct = ['Helsinki', 'Porvoo', 'Koskenkyla', 'Kouvola', 'Taavetti', 'Lappeenranta']
        path_savonlinna_correct = ['Helsinki', 'Mantsala', 'Lahti', 'Heinola', 'Mikkeli', 'Juva', 'Savonlinna']
        path_joensuu_correct = ['Helsinki', 'Mantsala', 'Lahti', 'Heinola', 'Mikkeli', 'Juva', 'Varkaus', 'Joensuu']
        path_seinajoki_correct = ['Helsinki', 'Hyvinkaa', 'Hameenlinna', 'Toijala', 'Tampere', 'Parkano', 'Jalasjarvi', 'Seinajoki']
        path_kajaani_correct = ['Helsinki', 'Mantsala', 'Lahti', 'Heinola', 'Mikkeli', 'Juva', 'Varkaus', 'Kuopio', 'Iisalmi', 'Kajaani']
        path_oulu_correct = ['Helsinki', 'Mantsala', 'Lahti', 'Heinola', 'Jyvaskyla', 'Aanekoski', 'Pyhajarvi', 'Karsamaki', 'Liminka', 'Oulu']
        path_kilpisjarvi_correct = ['Helsinki', 'Mantsala', 'Lahti', 'Heinola', 'Jyvaskyla', 'Aanekoski', 'Pyhajarvi', 'Karsamaki', 'Liminka', 'Oulu', 'Kemi', 'Keminmaa', 'Tornio', 'Pello', 'Kolari', 'Muonio', 'Kilpisjarvi']
        path_utsjoki_correct = ['Helsinki', 'Mantsala', 'Lahti', 'Heinola', 'Jyvaskyla', 'Aanekoski', 'Pyhajarvi', 'Karsamaki', 'Liminka', 'Oulu', 'Kemi', 'Keminmaa', 'Rovaniemi', 'Sodankyla', 'Ivalo', 'Utsjoki']
        
        self.assertEqual( (path_tampere, path_rauma, path_lappeenranta, path_savonlinna, path_joensuu, path_seinajoki, path_kajaani, path_oulu, path_kilpisjarvi, path_utsjoki) , 
                        (path_tampere_correct, path_rauma_correct, path_lappeenranta_correct, path_savonlinna_correct, path_joensuu_correct, 
                        path_seinajoki_correct, path_kajaani_correct, path_oulu_correct, path_kilpisjarvi_correct, path_utsjoki_correct) )
    
    
    # Test Paths on Dijkstra from Jyvaskyla
    def test_paths_on_dijkstra_on_real_graph_from_jyvaskyla(self):
        d, path_turku, t = dijkstra('Jyvaskyla', 'Turku', self.adjlist)
        d, path_kouvola, t = dijkstra('Jyvaskyla', 'Kouvola', self.adjlist)
        d, path_vaasa, t = dijkstra('Jyvaskyla', 'Vaasa', self.adjlist)
        d, path_kuusamo, t = dijkstra('Jyvaskyla', 'Kuusamo', self.adjlist)
        d, path_kilpisjarvi, t = dijkstra('Jyvaskyla', 'Kilpisjarvi', self.adjlist)
        
        path_turku_correct = ['Jyvaskyla', 'Jamsa', 'Tampere', 'Toijala', 'Humppila', 'Turku']
        path_kouvola_correct = ['Jyvaskyla', 'Heinola', 'Lahti', 'Kouvola']
        path_vaasa_correct = ['Jyvaskyla', 'Petajavesi', 'Ahtari', 'Seinajoki', 'Ylistaro', 'Laihia', 'Vaasa']
        path_kuusamo_correct = ['Jyvaskyla', 'Aanekoski', 'Pyhajarvi', 'Karsamaki', 'Liminka', 'Oulu', 'Kiiminki', 'Pudasjarvi', 'Taivalkoski', 'Kuusamo']
        path_kilpisjarvi_correct = ['Jyvaskyla', 'Aanekoski', 'Pyhajarvi', 'Karsamaki', 'Liminka', 'Oulu', 'Kemi', 'Keminmaa', 'Tornio', 'Pello', 'Kolari', 'Muonio', 'Kilpisjarvi']
    
        self.assertEqual( (path_turku, path_kouvola, path_vaasa, path_kuusamo, path_kilpisjarvi) , 
                        (path_turku_correct, path_kouvola_correct, path_vaasa_correct, path_kuusamo_correct, path_kilpisjarvi_correct) )
    
    # Test Paths on IDA* from Jyvaskyla
    def test_paths_on_idastar_on_real_graph_from_jyvaskyla(self):
        d, path_turku, t = idastar('Jyvaskyla', 'Turku', self.adjlist, self.coordinates)
        d, path_kouvola, t = idastar('Jyvaskyla', 'Kouvola', self.adjlist, self.coordinates)
        d, path_vaasa, t = idastar('Jyvaskyla', 'Vaasa', self.adjlist, self.coordinates)
        d, path_kuusamo, t = idastar('Jyvaskyla', 'Kuusamo', self.adjlist, self.coordinates)
        d, path_kilpisjarvi, t = idastar('Jyvaskyla', 'Kilpisjarvi', self.adjlist, self.coordinates)
        
        path_turku_correct = ['Jyvaskyla', 'Jamsa', 'Tampere', 'Toijala', 'Humppila', 'Turku']
        path_kouvola_correct = ['Jyvaskyla', 'Heinola', 'Lahti', 'Kouvola']
        path_vaasa_correct = ['Jyvaskyla', 'Petajavesi', 'Ahtari', 'Seinajoki', 'Ylistaro', 'Laihia', 'Vaasa']
        path_kuusamo_correct = ['Jyvaskyla', 'Aanekoski', 'Pyhajarvi', 'Karsamaki', 'Liminka', 'Oulu', 'Kiiminki', 'Pudasjarvi', 'Taivalkoski', 'Kuusamo']
        path_kilpisjarvi_correct = ['Jyvaskyla', 'Aanekoski', 'Pyhajarvi', 'Karsamaki', 'Liminka', 'Oulu', 'Kemi', 'Keminmaa', 'Tornio', 'Pello', 'Kolari', 'Muonio', 'Kilpisjarvi']
    
        self.assertEqual( (path_turku, path_kouvola, path_vaasa, path_kuusamo, path_kilpisjarvi) , 
                        (path_turku_correct, path_kouvola_correct, path_vaasa_correct, path_kuusamo_correct, path_kilpisjarvi_correct) )
    
    
    # Test Paths on Dijkstra from Oulu
    def test_paths_on_dijkstra_on_real_graph_from_oulu(self):
        d, path_porvoo, t = dijkstra('Oulu', 'Porvoo', self.adjlist)
        d, path_pori, t = dijkstra('Oulu', 'Pori', self.adjlist)
        d, path_hameenlinna, t = dijkstra('Oulu', 'Hameenlinna', self.adjlist)
        d, path_kuopio, t = dijkstra('Oulu', 'Kuopio', self.adjlist)
        d, path_kilpisjarvi, t = dijkstra('Oulu', 'Kilpisjarvi', self.adjlist)
        
        path_porvoo_correct = ['Oulu', 'Liminka', 'Karsamaki', 'Pyhajarvi', 'Aanekoski', 'Jyvaskyla', 'Heinola', 'Lahti', 'Mantsala', 'Helsinki', 'Porvoo']
        path_pori_correct = ['Oulu', 'Liminka', 'Kalajoki', 'Kalvia', 'Kokkola', 'Uusikaarlepyy', 'Vaasa', 'Pori']
        path_hameenlinna_correct = ['Oulu', 'Liminka', 'Karsamaki', 'Pyhajarvi', 'Aanekoski', 'Jyvaskyla', 'Jamsa', 'Tampere', 'Toijala', 'Hameenlinna']
        path_kuopio_correct = ['Oulu', 'Liminka', 'Karsamaki', 'Pyhajarvi', 'Iisalmi', 'Kuopio']
        path_kilpisjarvi_correct = ['Oulu', 'Kemi', 'Keminmaa', 'Tornio', 'Pello', 'Kolari', 'Muonio', 'Kilpisjarvi']
        
        self.assertEqual( (path_porvoo, path_pori, path_hameenlinna, path_kuopio, path_kilpisjarvi) , 
                        (path_porvoo_correct, path_pori_correct, path_hameenlinna_correct, path_kuopio_correct, path_kilpisjarvi_correct) )
    
    # Test Paths on IDA* from Oulu
    def test_paths_on_idastar_on_real_graph_from_oulu(self):
        d, path_porvoo, t = idastar('Oulu', 'Porvoo', self.adjlist, self.coordinates)
        d, path_pori, t = idastar('Oulu', 'Pori', self.adjlist, self.coordinates)
        d, path_hameenlinna, t = idastar('Oulu', 'Hameenlinna', self.adjlist, self.coordinates)
        d, path_kuopio, t = idastar('Oulu', 'Kuopio', self.adjlist, self.coordinates)
        d, path_kilpisjarvi, t = idastar('Oulu', 'Kilpisjarvi', self.adjlist, self.coordinates)
        
        path_porvoo_correct = ['Oulu', 'Liminka', 'Karsamaki', 'Pyhajarvi', 'Aanekoski', 'Jyvaskyla', 'Heinola', 'Lahti', 'Mantsala', 'Helsinki', 'Porvoo']
        path_pori_correct = ['Oulu', 'Liminka', 'Kalajoki', 'Kalvia', 'Kokkola', 'Uusikaarlepyy', 'Vaasa', 'Pori']
        path_hameenlinna_correct = ['Oulu', 'Liminka', 'Karsamaki', 'Pyhajarvi', 'Aanekoski', 'Jyvaskyla', 'Jamsa', 'Tampere', 'Toijala', 'Hameenlinna']
        path_kuopio_correct = ['Oulu', 'Liminka', 'Karsamaki', 'Pyhajarvi', 'Iisalmi', 'Kuopio']
        path_kilpisjarvi_correct = ['Oulu', 'Kemi', 'Keminmaa', 'Tornio', 'Pello', 'Kolari', 'Muonio', 'Kilpisjarvi']
        
        self.assertEqual( (path_porvoo, path_pori, path_hameenlinna, path_kuopio, path_kilpisjarvi) , 
                        (path_porvoo_correct, path_pori_correct, path_hameenlinna_correct, path_kuopio_correct, path_kilpisjarvi_correct) )
    
    
    