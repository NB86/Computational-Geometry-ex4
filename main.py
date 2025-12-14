from solver.sweep_line_sovler import SweepLineSolver
from geometry.primitives import Point

def main():
    points_list = []
    solver = SweepLineSolver()
    result = solver.find_number_of_intersection_points(points_list) 
    print(result)

if __name__ == "__main__":
    main()