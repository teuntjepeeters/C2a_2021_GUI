import tkinter
from tkinter import messagebox


class GUI:
    def __init__(self):
        # Maak een main window
        self.main_window = tkinter.Tk()
        self.main_window.title("GUI")

        # Maak frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame,
                                          text="Geef aantal km:")
        self.km_entry = tkinter.Entry(self.top_frame,
                                      width=10)
        # Plaats label
        self.prompt_label.pack(side="left")
        self.km_entry.pack(side="left")

        # Maak twee buttons
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text="Convert",
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="Quit",
                                          command=self.main_window.destroy)
        # Plaats buttons in GUI
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")


        # Plaats de frames in de GUI
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Maak main window visible
        tkinter.mainloop()

    def convert(self):
        km = float(self.km_entry.get())
        miles = km * 0.6214
        output = "{} km is gelijk aan {} miles".format(str(km), str(round(miles, 2)))
        tkinter.messagebox.showinfo("Results", output)


if __name__ == '__main__':
    myGUI = GUI()