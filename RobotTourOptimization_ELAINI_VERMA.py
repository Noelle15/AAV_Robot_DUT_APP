# Your code should work with python 3.6 or less. Function/Method from python 3.8 are prohibited !!!
import math  # https://docs.python.org/3/library/math.html
import operator
import itertools
import random


def calcul_distance(first_point_value, second_point_value):
    """
        Calculate the distance between two points.
        
    """
    
    sq1 = (first_point_value[0] - second_point_value[0]) * \
        (first_point_value[0] - second_point_value[0])
    sq2 = (first_point_value[1] - second_point_value[1]) * \
        (first_point_value[1] - second_point_value[1])
    return math.sqrt(sq1+sq2)


def calcul_circuit(list_of_points, cycle):
    """
        Calculate the circuit. 
    
    """
   
    d = 0
    # Calculate and sum the distance between two points of the cycle
    for p in range(len(cycle)-1):
        first_point = list_of_points.get(cycle[p])
        second_point = list_of_points.get(cycle[p+1])
        d = d + calcul_distance(first_point, 
                                second_point)
    # Add the distance between the last point and the first point to close the circuit
    d = d + calcul_distance(second_point,
                            list_of_points.get(cycle[0]))
    return d


def nearest_neighbor_algorithm(first_point, list_of_points):
    """
        Searches for the nearest point to the initial point then delete it 
        from the list_of_unvisited_points.
        The nearest point becomes the initial point at each iteration.

    """

    list_of_unvisited_points = list_of_points.copy()
    cycle = {}
    # Start with the first point
    initial_point = first_point
    cycle[0] = list_of_unvisited_points.get(first_point)
    del list_of_unvisited_points[first_point]
    # Find the nearest point to the initial point
    while (len(list_of_unvisited_points) > 0):
        i = 0
        for j in list_of_unvisited_points:
            if i == 0:
                min_distance = calcul_distance(
                    list_of_points[initial_point], list_of_unvisited_points[j])
                closest = j
            else:
                dist = calcul_distance(
                    list_of_points[initial_point], list_of_unvisited_points[j])
                if dist < min_distance:
                    min_distance = dist
                    closest = j
                elif dist == min_distance:
                    continue
            i = i + 1
        # Add the nearest point found to the cycle
        cycle[closest] = list_of_unvisited_points[closest]
        initial_point = closest
        # Delete that point from the list of unvisited points
        del list_of_unvisited_points[closest]

    return list(cycle.keys())


def great_algorithm(first_point, list_of_points):
    """
        Comparing the distance of 3 points and choosing the order 
        that makes the shortest distance.
        
    """
    cycle = list()
    order = list(list_of_points.keys())
    # Initialise the minimal distance
    circuit_min  = calcul_circuit(list_of_points, list(list_of_points.keys()))
    i = 1
    # Compare the distance of every 3 points 
    while i<(len(list_of_points) - 2):
        for j in range (i+2,(len(list_of_points.keys()))):
            pair = order[i:j].copy()
            pair.reverse()
            order = order[:i] + pair + order[j:]
            distance_circuit = calcul_circuit(list_of_points, order)
            if distance_circuit < circuit_min :
                circuit_min = distance_circuit
                cycle = [i for i in order]
            if distance_circuit == circuit_min:
                cycle = [i for i in order]
        i=i+1
    return cycle



def optimal_algorithm(first_point, list_of_points):
    """ 
        Generates all the possibilities of circuits, calculates the total 
        distance then return the smallest one.

    """
    cycle = list()
    cycle_min = {}
    # Initialise the minimal distance
    circuit_min = calcul_circuit(list_of_points, list(list_of_points.keys()))
    # Generate all the possibilities of cycles 
    for order in (itertools.permutations(list_of_points)):
        # Fix the first point 
        if (order[0] == first_point):
            circuit_total = calcul_circuit(list_of_points, order)
            # Only keep the cycle with the shortest distance
            if circuit_total < circuit_min:
                circuit_min = circuit_total
                cycle = [i for i in order]
            elif circuit_total == circuit_min:
                cycle = [i for i in order]
                continue
        else:
            continue

    for i in cycle:
        cycle_min[i] = list_of_points[i]
        
    return list(cycle_min.keys())


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


def get_tricky_points():
    list_of_points = {
        0: (0, 0),
        1: (0, 1),
        2: (0, 3),
        3: (0, 11),
        4: (0, -21),
        5: (0, -5),
        6: (0, -1),
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


def test_big_better_algorithm():
    """I will test with a lot of points"""
    pass


def test_small_optimal_algorithm():
    list_of_points = get_small_list_of_points()

    first_point = 0
    result = optimal_algorithm(first_point, list_of_points)
    assert len(result) == 10
    assert result[0] == first_point
    circuit_cost = calcul_circuit(list_of_points, result)
    assert round(circuit_cost) <= 27
    assert round(circuit_cost, 2) == 24.75
    assert result == [0, 2, 3, 1, 7, 5, 9, 6, 8, 4]


def test_big_optimal_algorithm():
    """I will test with a lot of points"""
    pass


def test_tricky_nearest_neighbor():
    list_of_points = get_tricky_points()

    first_point = 0
    result = nearest_neighbor_algorithm(first_point, list_of_points)
    assert len(result) == 7
    assert result[0] == first_point
    assert round(calcul_circuit(list_of_points, result)) <= 80

    
def test_tricky_better_algorithm():
    list_of_points = get_tricky_points()

    first_point = 0
    result = great_algorithm(first_point, list_of_points)
    assert len(result) == 7
    assert result[0] == first_point
    assert round(calcul_circuit(list_of_points, result)) < 80

    
def test_tricky_optimal_algorithm():
    list_of_points = get_tricky_points()

    first_point = 0
    result = optimal_algorithm(first_point, list_of_points)
    assert len(result) == 7
    assert result[0] == first_point
    assert round(calcul_circuit(list_of_points, result)) == 64

"our tests"


def test_basic_function():
    test_calcul_distance()
    test_calcul_min_circuit()
    test_calcul_circuit()


def test_nearest_neighbor():
    test_return_sized()
    #test_small_nearest_neighbor()
    #test_big_nearest_neighbor()
    test_tricky_nearest_neighbor()


def test_better_algorithm():
    test_small_better_algorithm()
    #test_big_better_algorithm()
    #test_tricky_better_algorithm()


def test_optimal_algorithm():
    test_small_optimal_algorithm()
    #test_big_optimal_algorithm()
    test_tricky_optimal_algorithm()

#test_optimal_algorithm()
#test_nearest_neighbor()
#test_better_algorithm()
