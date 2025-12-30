import sys
from geometry.primitives import Point, Segment
import solver.simple_solver as simple_solver

def parse_input_file(input_file):
    with open(input_file, 'r') as file:
        segments = []
        number_of_tests = int(file.readline())
        for test_number in range(number_of_tests):
            number_of_segments = int(file.readline())
            segments_in_test = []
            for segment_number in range(number_of_segments):
                line = file.readline()
                coords = list(map(float, line.strip().split()))
                x1, y1, x2, y2 = coords
                p = Point(x1, y1)
                q = Point(x2, y2)
                segment = Segment(p, q)
                segments_in_test.append(segment)
            
            segments.append(segments_in_test)
    
    return segments

def create_result_file(segments):
    for test_segments in segments:
        print(simple_solver.find_number_of_intersection_points(test_segments))
    