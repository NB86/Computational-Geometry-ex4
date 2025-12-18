import itertools
from geometry.primitives import intersection 

def find_number_of_intersection_points(segments):
    number_of_intersection_points = 0
    for pair in itertools.combinations(segments, r=2):
            intersection_point = intersection(pair[0], pair[1])
            if intersection_point != None:
                number_of_intersection_points += 1
    
    return number_of_intersection_points