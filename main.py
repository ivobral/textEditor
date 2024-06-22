import tkinter as tk
from TextEditorModel import TextEditorModel
from TextEditor import TextEditor


def main():
    root = tk.Tk()
    root.title("Text Editor")
    
    model = TextEditorModel("Ab ovo.\nAd astra.\nCarpe diem!\nHomo homini lupus est.\nDictum, factum.\nHomo homini lupus est.\nAlea iacta est!\nPro domo!")
    editor = TextEditor(root, model)

    root.mainloop()

if __name__ == '__main__':
    main()