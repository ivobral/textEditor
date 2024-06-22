from tkinter import *
from TextEditorModel import TextEditorModel
from Observers import CursorObserver
from Location import Location

class TextEditor(Canvas, CursorObserver):
    def __init__(self, root: None, model: TextEditorModel):
        super().__init__(root, bg="white", width=600, height=400)
        self.model = model
        self.focus_set()

        self.model.addCursorObserver(self)
        self.cursorVisible = True
        self.blink_cursor()

        self.bind("<Left>", lambda event: self.model.moveCursorLeft())
        self.bind("<Right>", lambda event: self.model.moveCursorRight())
        self.bind("<Up>", lambda event: self.model.moveCursorUp())
        self.bind("<Down>", lambda event: self.model.moveCursorDown())



        self.show()
        self.drawCursor(self.model.getCursorLocation())

    def setCursorVisible(self, visible: bool):
        self.cursorVisible = visible

    def getCursorVisible(self):
        return self.cursorVisible

    def drawCursor(self, location: Location):
        self.delete("cursor")

        x = 10 + location.column * 12    #width of a character
        y = 10 + location.row * 20    #height of a character
        
        self.create_line(x, y, x, y + 20, fill="black", tags="cursor")

    def updateCursorLocation(self, location: Location):
        self.drawCursor(location)

    def blink_cursor(self):
        self.setCursorVisible(not self.getCursorVisible())
        self.drawCursor(self.model.getCursorLocation()) if self.getCursorVisible() else self.delete("cursor")
        self.after(500, self.blink_cursor)

    def show(self):
        iterator = self.model.allLines()
        for i, line in enumerate(iterator):
            self.create_text(10, 10 + 20 * i, anchor=NW, text=line, font=("Courier", 15))
        self.pack()