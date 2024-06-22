from Location import Location
from Observers import CursorObserver

class TextEditorModel():
    def __init__(self, text: str):
        self.lines = text.split("\n")
        self.selectionRange = None
        self.cursorLocation = Location(0, 0)

        self.cursorObservers = []
    
    def getLines(self):
        return self.lines
    
    def getCursorObservers(self):
        return self.cursorObservers

    def getCursorLocation(self):
        return self.cursorLocation
    
    def getSelectionRange(self):
        return self.selectionRange
    
    def setCursorLocation(self, location: Location):
        self.cursorLocation = location
    
    # iterators
    def allLines(self):
        # return iterator which goes through all lines
        for line in self.getLines():
            yield line

    def linesRange(self, index1: int, index2: int):
        # return iterator which goes through lines from index1 to index2
        for i in range(index1, index2):
            yield self.getLines()[i]

    # cursor
    def addCursorObserver(self, observer: CursorObserver):
        self.cursorObservers.append(observer)

    def removeCursorObserver(self, observer: CursorObserver):
        self.cursorObservers.remove(observer)

    def notifyCursorObservers(self):
        for observer in self.getCursorObservers():
            observer.updateCursorLocation(self.getCursorLocation())

    def moveCursorLeft(self):
        if self.getCursorLocation().column > 0:
            #print("Curosor not at the beginning of the line. Moving left.")
            self.setCursorLocation(Location(self.getCursorLocation().row, self.getCursorLocation().column - 1))
        else:
            if self.getCursorLocation().row == 0 and self.getCursorLocation().column == 0:
                #print("Cursor at the beginning of the file. Staying put.")
                return
            if self.getCursorLocation().row > 0:
                #print("Cursor at the beginning of the line. Moving up.")
                self.setCursorLocation(Location(self.getCursorLocation().row - 1, len(self.getLines()[self.getCursorLocation().row - 1])))

        self.notifyCursorObservers()

    def moveCursorRight(self):
        if self.getCursorLocation().column < len(self.getLines()[self.getCursorLocation().row]):
            #print("Curosor not at the end of the line. Moving right.")
            self.setCursorLocation(Location(self.getCursorLocation().row, self.getCursorLocation().column + 1))
        else:
            if self.getCursorLocation().row == len(self.getLines()) - 1 and self.getCursorLocation().column == len(self.getLines()[self.getCursorLocation().row]):
                #print("Cursor at the end of the file. Staying put.")
                return
            if self.getCursorLocation().row < len(self.getLines()):
                #print("Cursor at the end of the line. Moving down.")
                self.setCursorLocation(Location(self.getCursorLocation().row + 1, 0))

        self.notifyCursorObservers()

    def moveCursorUp(self):
        if self.getCursorLocation().row > 0:
            self.setCursorLocation(Location(self.getCursorLocation().row - 1, min(self.getCursorLocation().column, len(self.getLines()[self.getCursorLocation().row - 1]))))

        self.notifyCursorObservers()

    def moveCursorDown(self):
        if self.getCursorLocation().row < len(self.getLines()) - 1:
            self.setCursorLocation(Location(self.getCursorLocation().row + 1, min(self.getCursorLocation().column, len(self.getLines()[self.getCursorLocation().row + 1]))))

        self.notifyCursorObservers()