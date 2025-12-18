EPSILON = 1e-9

class Point:
    x : float 
    y : float 

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return (self.x < other.x) or (self.x == other.x and self.y < other.y) 
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (abs(self.x - other.x) < EPSILON) and \
               (abs(self.y - other.y) < EPSILON)

    def __hash__(self):
        # Snap the coordinates to a multiple of a large power of 10 
        # to ensure consistency across close floating-point values.
        # Example: Round to 9 decimal places.
        x_snap = round(self.x, 9)
        y_snap = round(self.y, 9)
        return hash((x_snap, y_snap))

class Segment:
    id : int # to overcome numerical error when we find a point on an ...
    #    # already-known segment we identify segments with unique ID.
    #    # binary search with numerical errors is guaranteed to find an ...
    #    # index whose distance from the correct one is O(1) (here it is 2).
    #
    p : Point # Point, after input we compare and swap to guarantee that p.x <= q.x
    q : Point # Point
    
    def __init__(self, p, q):
        if p.x > q.x:
            p,q = q,p
        self.p = p
        self.q = q
    
    # line: y = ax + b. it is guaranteed that the line is not vertical (a is finite)
    def a(self): # () -> double
        return ((self.p.y - self.q.y) / (self.p.x - self.q.x))
    
    def b(self): # () -> double
        return (self.p.y - (self.a() * self.p.x))
    
    # the y-coordinate of the point on the segment whose x-coordinate ..
    #   is given. Segment boundaries are NOT enforced here.
    def calc(self, x):
        return (self.a() * x + self.b())
    
    def __str__(self):
        return f"[{self.p}, {self.q}]"

    def __repr__(self):
        return f"[{self.p}, {self.q}]"

    def __lt__(self, other):
        start_point = min(self.p, self.q)
        other_start_point = min(other.p, other.q)
        if start_point.y == other_start_point.y:
            return max(self.p, self.q) < max(other.p, other.q)
        
        return start_point.y < other_start_point.y

def is_left_turn(a, b, c): # (Point,Point,Point) -> bool
    x1 = a.x
    x2 = b.x
    x3 = c.x
    y1 = a.y
    y2 = b.y
    y3 = c.y
    return ((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2))) > 0
# def

def intersection(s1, s2): # (segment,segment) -> Point | None
    if ((is_left_turn(s1.p, s1.q, s2.p) != is_left_turn(s1.p, s1.q, s2.q)) and
        (is_left_turn(s2.p, s2.q, s1.p) != is_left_turn(s2.p, s2.q, s1.q))):
        
        a1 = s1.a()
        a2 = s2.a()

        b1 = s1.b()
        b2 = s2.b()

        # commutation consistency: sort by a (then by b)
        if a1 > a2 or (a1 == a2 and b1 > b2):
            a1,a2 = a2,a1
            b1,b2 = b2,b1
        # if

        #
        # a1 x + b1 = y
        # a2 x + b2 = y
        # (a1 - a2)x + (b1-b2) = 0
        # x = (b2-b1)/(a1-a2)
        #

        x = (b2 - b1) / (a1 - a2)
        y = a1 * x + b1

        return Point(x, y)
    else:
        return None
    #else
#def

def intersects(s1, s2): # (Segment,Segment) -> bool
    return not(intersection(s1, s2) is None)
#def