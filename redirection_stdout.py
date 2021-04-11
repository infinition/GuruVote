#redirection_stdout.py
 
import sys
import tkinter as tk
 
 
class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget
 
    def write(self, s):
        self.text_widget.insert('end', s)
        self.text_widget.see('end')
 
 
class StdoutTkinter(tk.Tk):
    def __init__(self):
        ## Python 3.X
        super().__init__()
        ## Python 2.X
        #tk.Tk.__init__(self)
 
        self.title('GuruVote')
 
        frame = tk.Frame(self, width=100, height=200)
        frame.pack()
 
        self.textbox = tk.Text(frame, wrap='word', fg="green", bg="black")
        self.textbox.pack()
 
        ## Voici le truc, on pointe le sys.stdout vers le textbox
        sys.stdout = StdoutRedirector(self.textbox)



        # self.consoleFrame = Frame(root)
        # self.consoleFrame.pack(expand=1, pady=15, padx=15, fill= BOTH)
        # self.consoleText = Text(self.consoleFrame, fg="green", bg="black",state=DISABLED)
        # self.consoleText.pack(expand=1, fill= BOTH)