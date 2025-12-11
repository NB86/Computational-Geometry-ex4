from event import Event, EventType

class CG24PriorityQueue:    
    def __init__(self):
        self.array  = list()
        
    def insert(self, event: Event) -> None:
        self.array.append(event)
        
        # heapify up
        i = int(len(self.arr)) - int(1)
        parent = int((i - 1) / 2)

        while i > 0 and self.arr[i] < self.arr[parent]:
            self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
            i = parent
            parent = int((i - 1) / 2)
    
    def empty(self) -> bool:
        return 0 == len(self.arr)
    
    def pop(self) -> Event: 
        if 0 == len(self.arr):
            return self.arr[0] # raise exception
        
        res = self.arr[0].event
        
        if len(self.arr) > 1:
            n = len(self.arr)
            self.arr[0], self.arr[n - 1] = self.arr[n - 1], self.arr[0]
            n = n - 1
            
            i  = 0
            while i < n:
                best = i
                j1 = int(2 * i + 1)
                j2 = int(2 * i + 2)
                if j1 < n and self.arr[j1] < self.arr[best]:
                    best = j1

                if j2 < n and self.arr[j2] < self.arr[best]:
                    best = j2

                if best == i:
                    break

                self.arr[i], self.arr[best] = self.arr[best], self.arr[i]
                i = best

        self.arr.pop()
        return res
        