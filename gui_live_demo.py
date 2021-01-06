import tkinter
from tkinter import messagebox


class GUI:
    def __init__(self):
        # Maak de window aan
        self.main_window = tkinter.Tk()

        # Maak twee frames aan (top en bottom)
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Maak een label aan
        self.label1 = tkinter.Label(self.top_frame,
                                    text="Was het maar vakantie!")
        self.label2 = tkinter.Label(self.top_frame,
                                    text="Hello world!")
        self.label3 = tkinter.Label(self.top_frame,
                                    text="Sushi")

        # Maak een button aan
        self.knopje = tkinter.Button(self.bottom_frame, # Waar komt de knop?
                                     text="Klik hier!", # Tekst in de knop
                                     command=self.do_something) # Wat te doen bij klikken?
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="quit",
                                          command=self.main_window.destroy)

        # Plaats de buttons in je GUI
        self.knopje.pack(side="left")
        self.quit_button.pack(side="left")

        # Plaats de labels in de GUI
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()

        # Plaats de twee frames in de GUI
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Zorg dat de GUI tevoorschijn komt
        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo("Response",
                                    "Bedankt voor het klikken")


if __name__ == '__main__':
    myGUI = GUI()