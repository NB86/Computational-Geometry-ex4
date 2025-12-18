import sys
from solver.sweep_line_sovler import SweepLineSolver
from input_output.plotting import plot_geometry 
from input_output.segment_parser import parse_input_file, create_result_file

def main():
    if len(sys.argv) > 1:
        input_filename = sys.argv[1]
    else:
        print("try run - python main.py [directory_to_input_file]")
        exit()

    segments = parse_input_file(input_filename)

    for test_segments in segments:
        #plot_geometry(test_segments, "t1.in")
        solver = SweepLineSolver()
        result = solver.find_number_of_intersection_points(test_segments)
        print(result)
    
    #create_result_file(f'./tests/expected_files/t1.out', segments)

if __name__ == "__main__":
    main()