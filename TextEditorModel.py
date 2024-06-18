from Location import Location

class TextEditorModel():
    def __init__(self, text: str):
        self.lines = text.split("\n")
        self.selectionRange = None
        self.cursorLocation = Location(0, 0)
    
    def getLines(self):
        return self.lines
    

    # iterators
    def allLines(self):
        # return iterator which goes through all lines
        for line in self.getLines():
            yield line

    def linesRange(self, index1: int, index2: int):
        # return iterator which goes through lines from index1 to index2
        for i in range(index1, index2):
            yield self.getLines()[i]