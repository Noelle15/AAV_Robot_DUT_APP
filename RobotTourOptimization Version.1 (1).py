# Your code should work with python 3.6 or less. Function/Method from python 3.8 are prohibited !!!
import math  # https://docs.python.org/3/library/math.html
import operator

def calcul_distance(first_point_value, second_point_value):
    """
        Distance between two points calculation
        first_point_value : tuple (x, y) of a point
        second_point_value : tuple (x, y) of a point
        return a float, the distance between those two point
    """
    sq1=(first_point_value[0] - second_point_value[0])*(first_point_value[0] - second_point_value[0]) 
    sq2=(first_point_value[1] - second_point_value[1])*(first_point_value[1] - second_point_value[1])
    return math.sqrt(sq1+sq2)


def calcul_circuit(list_of_points, cycle):
    """
        Circuit length calculation
        first_point: label of the first point
        list_of_points: dict of all the point, the key is the label, the value is a tuple (x, y)
        return a float, a circuit length
    """
    d = 0
    print("----------------------",cycle)
    for p in range(len(cycle)-1):
        first_point = list_of_points.get(cycle[p])
        second_point= list_of_points.get(cycle[p+1])
        d = d + calcul_distance(first_point, second_point)
        print("ouuuuuuuu",first_point,"ettttttt", second_point)
        print ("distance entre les deux points ",calcul_distance(first_point, second_point))
    d = d + calcul_distance(second_point, list_of_points.get(cycle[0])) 
    return d


def Delete_par_valeur(list_of_points, valeur):
    list1 = dict(list_of_points)
    for k in range(len(list1.keys())):
        if (list1[k] == valeur): 
            del list_of_points[k]
    

def nearest_neighbor_algorithm(first_point, list_of_points):
    """
    Implement the nearest_neighbor algorithm.
    first_point: label of the first point
    list_of_points: dict of all the point, the key is the label, the value is a tuple (x, y)
    return a list of point to visit, starting from first_point.
    """
    list_of_unvisited_points = list_of_points.copy()
    cycle = {}
    initial_point =  first_point
    cycle[0] = list_of_unvisited_points.get(first_point)
    print("cycle début ", cycle)
    del list_of_unvisited_points[first_point]
    print(list_of_unvisited_points)
    
    #min_distance = calcul_distance(initial_point,list_of_unvisited_points[1])
    while (len(list_of_unvisited_points) > 0):
        i=0
        for j in list_of_unvisited_points:
            if i == 0:
                #print("le point avec lequel on teste  ",list_of_unvisited_points[j] )
                #print("PPPPPOOIIINNTTT IMP",cycle[initial_point] )
                min_distance = calcul_distance(list_of_points[initial_point], list_of_unvisited_points[j])
                closest = j
                #print("diastance minimale",min_distance)
            else :
                #print("le point   ",list_of_unvisited_points[j] )
                dist = calcul_distance(list_of_points[initial_point], list_of_unvisited_points[j])
                #print ("distance",dist)
                if dist <  min_distance:
                    min_distance = dist
                    closest = j
                    #print(cycle)
                elif dist == min_distance:
                    continue
            i=i+1

        #print("AVANT",list_of_unvisited_points[closest])
        cycle[closest] = list_of_unvisited_points[closest]
        initial_point = closest
        del list_of_unvisited_points[closest]
        #print ("le plus proche",closest)
        #print("APRES",closest)
    print("officiel",cycle)

    #print("TTTTEEEESSSSSSTTTTT--------------------calcul ciruit ",round(calcul_circuit(list_of_points, list(cycle.keys()))))
    #print("fonction points non visités ",list_of_unvisited_points)
    #print("fonction liste points  ",list_of_points)
    #print("fonction cycle ",cycle)
    return list(cycle.keys())


def great_algorithm(first_point, list_of_points):
    """
        Implement a good algorithm to resolve the case.
        first_point: label of the first point
        list_of_points: dict of all the point, the key is the label, the value is a tuple (x, y)
        return a list of point to visit, starting from first_point.
    """

    return list(list_of_points.keys())


def optimal_algorithm(first_point, list_of_points):
    """
        Implement an optimal algorithm. This solution is the best, but it is slow
        first_point: label of the first point
        list_of_points: dict of all the point, the key is the label, the value is a tuple (x, y)
        return a list of point to visit, starting from first_point.
    """

    return list(list_of_points.keys())


def get_small_list_of_points():
    list_of_points = {
        0: (1, 3),
        1: (2, 5),
        2: (0, 6),
        3: (1, 7),
        4: (5, 1),
        5: (5, 5),
        6: (6, 3),
        7: (4, 4),
        8: (7, 0),
        9: (6, 6)
    }
    return list_of_points


def test_calcul_distance():
    a = (-3, -2)
    b = (5, 2)
    assert round(calcul_distance(a, b), 3) == 8.944


def test_calcul_min_circuit():
    a = (-3, -2)
    b = (5, 2)
    list_of_points = {'a': a, 'b': b}
    cycle = ['a', 'b']
    assert round(calcul_circuit(list_of_points, cycle), 3) == 17.889


def test_calcul_circuit():
    list_of_points = get_small_list_of_points()

    cycle = list(list_of_points.keys())
    distance = calcul_circuit(list_of_points, cycle)
    assert round(distance, 3) == 38.483


def test_return_sized():
    list_of_points = get_small_list_of_points()
    first_point = 0
    result = nearest_neighbor_algorithm(first_point, list_of_points)
    assert len(result) == 10
    assert result[0] == first_point 

def test_small_nearest_neighbor():
    list_of_points = get_small_list_of_points()

    first_point = 0
    result = nearest_neighbor_algorithm(first_point, list_of_points)
    assert len(result) == 10
    assert result[0] == first_point
    print("--------------------calcul ciruit ",round(calcul_circuit(list_of_points, result)))
    assert round(calcul_circuit(list_of_points, result)) <= 27


def test_big_nearest_neighbor():
    """I will test with a lot of points"""
    pass


def test_small_better_algorithm():
    list_of_points = get_small_list_of_points()

    first_point = 0
    result = great_algorithm(first_point, list_of_points)
    assert len(result) == 10
    assert result[0] == first_point

    """I will add some tests here"""


def test_big_better_algorithm():
    """I will test with a lot of points"""
    pass


def test_small_optimal_algorithm():
    list_of_points = get_small_list_of_points()

    first_point = 0
    result = optimal_algorithm(first_point, list_of_points)
    assert len(result) == 10
    assert result[0] == first_point

    """I will add some tests here"""


def test_big_optimal_algorithm():
    """I will test with a lot of points"""
    pass


"our tests"
def test_basic_function():
    test_calcul_distance()
    test_calcul_min_circuit()
    test_calcul_circuit()

"our tests"
def test_nearest_neighbor():
    test_return_sized()
    test_small_nearest_neighbor()
    #test_big_nearest_neighbor()

#test_calcul_distance()
#test_basic_function()
#nearest_neighbor_algorithm((1, 3), get_small_list_of_points())
test_nearest_neighbor()
#a = (0,1,2,3,7,5,9,6,4,8)
#print(calcul_circuit(get_small_list_of_points(),a))
