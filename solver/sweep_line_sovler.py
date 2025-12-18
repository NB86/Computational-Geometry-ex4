from avltree import AvlTree
from data_structures.priority_queue import CG24PriorityQueue
from data_structures.event import Event, EventType
from geometry.primitives import Segment, intersection 

class SweepLineSolver:
    def __init__(self):
        self.event_queue = CG24PriorityQueue()
        self.sweep_line_status = AvlTree[Segment, Segment]()
        self.intersection_cache = set()

    def _get_previous_segment(self, segment):
        prev_segment = None
        try:
            prev_segment = list(self.sweep_line_status.between(stop=segment, treatment='exclusive'))[-1]
        except:
            pass

        return prev_segment

    def _get_next_segment(self, segment):
        return next(self.sweep_line_status.between(start=segment, treatment='exclusive'), None)
    
    def _check_for_intersection(self, first_segment, second_segment):
        if first_segment != None and second_segment != None:
            intersection_point = intersection(first_segment, second_segment)
            if intersection_point != None and intersection_point not in self.intersection_cache:
                event = Event(intersection_point, EventType.INTERSECTION_POINT, [first_segment, second_segment])
                self.event_queue.insert(event)
                self.intersection_cache.add(intersection_point)
                

    def find_number_of_intersection_points(self, segments):
        number_of_intersection_points = 0

        for segment in segments:
            start_point_event = Event(segment.p, EventType.START_OF_SEGMENT, [segment])
            end_point_event = Event(segment.q, EventType.END_OF_SEGMENT, [segment])
            self.event_queue.insert(start_point_event)
            self.event_queue.insert(end_point_event)
        
        while True:
            try:
                current_event = self.event_queue.pop()
            except:
                break
            
            match current_event.event_type:
                case EventType.START_OF_SEGMENT:
                    current_segment = current_event.segments[0] 
                    self.sweep_line_status[current_segment] = current_segment
                    prev_segment = self._get_previous_segment(current_segment)
                    next_segment = self._get_next_segment(current_segment)
                    self._check_for_intersection(current_segment, prev_segment)
                    self._check_for_intersection(current_segment, next_segment)

                case EventType.END_OF_SEGMENT:
                    current_segment = current_event.segments[0]
                    prev_segment = self._get_previous_segment(current_segment)
                    next_segment = self._get_next_segment(current_segment)
                    del self.sweep_line_status[current_segment]
                    self._check_for_intersection(prev_segment, next_segment)

                case EventType.INTERSECTION_POINT:
                    number_of_intersection_points += 1
                    first_segment = min(current_event.segments[0], current_event.segments[1])
                    second_segment = max(current_event.segments[0], current_event.segments[1])

                    prev_segment = self._get_previous_segment(first_segment)
                    self._check_for_intersection(second_segment, prev_segment)
                    next_segment = self._get_next_segment(second_segment)
                    self._check_for_intersection(first_segment, next_segment)

                    # Swap the segments in the sweep line status
                    del self.sweep_line_status[first_segment]
                    del self.sweep_line_status[second_segment]
                    self.sweep_line_status[first_segment] = second_segment
                    self.sweep_line_status[second_segment] = first_segment

        return number_of_intersection_points
