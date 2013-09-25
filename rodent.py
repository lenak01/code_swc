class Rodent:
    def __init__(self, tag_id, size):
        self.tagID = tag_id
        self.size = size
        self.sighting = {}
    def is_large(self):#size>5oz
        return (self.size > 5)
    def is_small(self):#size<3oz
        return (self.size < 3)
    def capture(self, month):#captured this rodent once in this month
        if month not in self.sighting:
            self.sighting[month] = 0
        self.sighting[month] += 1
    def plot(self):#letter of the plot at which this rodent was first captured
        return self.tagID[0]


