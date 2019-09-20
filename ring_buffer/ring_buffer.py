class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #add to buffer
    self.storage[self.current] = item

    if self.current == self.capacity -1:
      self.current = 0
    else: 
      self.current += 1

  def get(self):
    #returns buffer storage, without [None]
    return [ea for ea in self.storage if ea is not None]