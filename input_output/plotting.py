import matplotlib.pyplot as plt
from geometry.primitives import Segment, Point

def plot_geometry(test_segments: list[Segment], test_name: str):
    """
    Plots the line segments and highlights the intersection points for the FIRST test case.
    
    :param all_test_segments: A list of lists of segments (output from parse_file).
    :param intersections: A list of Point objects representing found intersections.
    :param test_name: The name of the test/file for the plot title.
    """
    if not test_segments:
        print("No segments to plot in the first test case.")
        return
        
    # Initialize the plot
    fig, ax = plt.subplots()
    ax.set_xlabel("X-Coordinate")
    ax.set_ylabel("Y-Coordinate")
    ax.grid(True)
    
    # 1. Plot the Segments (Lines)
    for seg in test_segments:
        # Create arrays of X and Y coordinates for the segment
        X = [seg.p.x, seg.q.x]
        Y = [seg.p.y, seg.q.y]
        
        # Plot the line 
        ax.plot(X, Y, color='blue', linestyle='-', marker='o', linewidth=1.5, alpha=0.7)

    # 2. Finalize and Show
    ax.set_aspect('equal', adjustable='box')
    plt.show()
