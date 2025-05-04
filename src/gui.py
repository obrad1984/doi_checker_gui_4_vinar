from tkinter import Tk, Label, Entry, Button, Text, END
from doi_checker_may_2025 import check_doi_exists

class DOICheckerGUI:
    def __init__(self, master):
        self.master = master
        master.title("DOI Checker")

        self.label = Label(master, text="Enter DOI:")
        self.label.pack()

        self.doi_entry = Entry(master, width=70)
        self.doi_entry.pack()

        self.check_button = Button(master, text="Check DOI", command=self.check_doi)
        self.check_button.pack()

        self.result_text = Text(master, height=10, width=80)
        self.result_text.pack()

        self.stop_button = Button(master, text="Stop", command=master.quit)
        self.stop_button.pack()

    def check_doi(self):
        doi = self.doi_entry.get()
        result = check_doi_exists(doi)
        self.result_text.delete(1.0, END)  # Clear previous results
        if result is None:
            self.result_text.insert(END, "An error occurred while checking the DOI.\n")
        elif result:
            self.result_text.insert(END, f"ATTENTION! Yes, DOI exists in the VinaR database.\n")
        else:
            self.result_text.insert(END, f"The sky is clear! DOI does not exist in the VinaR database.\n")

if __name__ == "__main__":
    root = Tk()
    gui = DOICheckerGUI(root)
    root.mainloop()