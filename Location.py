class Location():
    def __init__(self, row, col):
        self.row = row
        self.column = col
    


class LocationRange():
    def __init__(self, start: Location, end: Location):
        self.start = start
        self.end = end