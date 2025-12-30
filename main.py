import argparse
import sys
from solver.sweep_line_sovler import SweepLineSolver
from input_output.plotting import plot_geometry 
from input_output.segment_parser import parse_input_file, create_result_file

def main():
    parser = argparse.ArgumentParser(description="Sweep Line Intersection Solver")
    
    # Positional argument for the input file
    parser.add_argument("input_filename", help="Path to the input file")
    
    # Optional flag for mode
    parser.add_argument("-m", "--mode", type=int, choices=[1, 2], default=1,
                        help="Mode 1: Run Algorithm (Default). Mode 2: Create Results File.")

    args = parser.parse_args()
    try:
        segments = parse_input_file(args.input_filename)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    if args.mode == 1:
        for test_segments in segments:
            #plot_geometry(test_segments, args.input_filename)
            solver = SweepLineSolver()
            result = solver.find_number_of_intersection_points(test_segments)
            print(result)
    elif args.mode == 2:
        create_result_file(segments)

if __name__ == "__main__":
    main()