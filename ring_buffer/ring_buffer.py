#ring_buffer/ring_buffer.py



class RingBuffer:
    def __init__(self, capacity):
        self.capacity=capacity
        self.list_items=[]
        self.index=0

    def append(self, item):
        if len(self.list_items)!=self.capacity:
            self.list_items.append(item)
        else:
            self.list_items[self.index]=item
        self.index=(self.index+1)%self.capacity

    def get(self):
        return self.list_items
        