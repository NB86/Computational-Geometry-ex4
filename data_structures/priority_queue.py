import copy 
from data_structures.event import Event

class CG24PriorityQueue:    
    def __init__(self):
        self.array = list()
        
    def insert(self, event: Event) -> None:
        self.array.append(event)
        
        # heapify up
        i = int(len(self.array)) - int(1)
        parent = int((i - 1) / 2)

        while i > 0 and self.array[i] < self.array[parent]:
            self.array[i], self.array[parent] = self.array[parent], self.array[i]
            i = parent
            parent = int((i - 1) / 2)
    
    def empty(self) -> bool:
        return 0 == len(self.array)
    
    def pop(self) -> Event: 
        if self.empty():
            raise ValueError
        
        res = self.array[0]
        
        if len(self.array) > 1:
            n = len(self.array)
            self.array[0], self.array[n - 1] = self.array[n - 1], self.array[0]
            n = n - 1
            
            i  = 0
            while i < n:
                best = i
                j1 = int(2 * i + 1)
                j2 = int(2 * i + 2)
                if j1 < n and self.array[j1] < self.array[best]:
                    best = j1

                if j2 < n and self.array[j2] < self.array[best]:
                    best = j2

                if best == i:
                    break

                self.array[i], self.array[best] = self.array[best], self.array[i]
                i = best

        self.array.pop()
        return res

    def __str__(self):
        temp = copy.deepcopy(self)
        string = ""
        while True:
            try:
                string += str(temp.pop())
            except:
                break
        return string

    def __repr__(self):
        return self.__str__()