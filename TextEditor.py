from tkinter import *
from TextEditorModel import TextEditorModel

class TextEditor(Canvas):
    def __init__(self, root: None, model: TextEditorModel):
        super().__init__(root, bg="white", width=600, height=400)
        self.model = model

    def show(self):
        iterator = self.model.allLines()
        for i, line in enumerate(iterator):
            self.create_text(10, 10 + 20 * i, anchor=W, text=line)
        self.pack()