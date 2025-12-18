from enum import Enum
from geometry.primitives import Point, Segment 

class EventType(Enum):
    START_OF_SEGMENT = 1
    END_OF_SEGMENT = 2
    INTERSECTION_POINT =3 

class Event:
    def __init__(self, point : Point, event_type: EventType, segments: list[Segment]):
        self.point = point
        self.event_type = event_type
        self.segments = segments # the segments which cross the point.
    
    def __lt__(self, other):
        return self.point < other.point
    
    def __str__(self):
        return str(self.point)

    def __repr__(self):
        return str(self.point)