import tkinter
from tkinter import messagebox

class GUI:
    def __init__(self):
        # Maak een main window aan
        self.main_window = tkinter.Tk()

        # Maak twee frames voor checkbox en buttons
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Maak drie intvar objecten voor de checkbuttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        # Zet de drie intvar objecten naar 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        # Checkbuttens aanmaken
        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                       text="Are you okay?",
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text="Are you not okay?",
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                       text="Are you sure?",
                                       variable=self.cb_var3)
        # Zorg dat checkbuttens zichtbaar worden
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        # Maak buttons aan
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text="OK",
                                        command=self.show_results)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="QUIT",
                                          command=self.main_window.destroy)

        # Show buttons
        self.ok_button.pack(side="left")
        self.quit_button.pack(side="left")

        # Pack de frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Zorg dat GUI verschijnt
        tkinter.mainloop()

    def show_results(self):
        """Wanneer er op OK wordt gedrukt laten we zien in een
        messagebox welke check box is aangevinkt"""
        self.message = "Je hebt geselecteerd: \n"
        if self.cb_var1.get() == 1:
            self.message = self.message + "Are you okay?\n"
        if self.cb_var2.get() == 1:
            self.message = self.message + "Are you not okay?\n"
        if self.cb_var3.get() == 1:
            self.message = self.message + "Are you sure?"
        tkinter.messagebox.showinfo("Selectie", self.message)



if __name__ == '__main__':
    myGUI = GUI()
