import customtkinter
from tkinter import filedialog
from tkinter import messagebox
import main

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")

        self.title("Web Scraper")
        self.geometry("600x650")

        label = customtkinter.CTkLabel(self, text="Web Scraper", font=("Nata Sans", 40))
        label.pack(side="top", padx=20, pady=20)

        label_url = customtkinter.CTkLabel(self, text="URL", font=("Nata Sans", 25))
        label_url.pack(padx=20,anchor="w")

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter your url", height=35)
        self.entry.pack(pady=20, padx=20, fill="x")

        label_selector = customtkinter.CTkLabel(self, text="Choose desired selector", font=("Nata Sans", 25))
        label_selector.pack(padx=20,anchor="w")

        frame = customtkinter.CTkFrame(self, fg_color="transparent")
        frame.pack(pady=20)

        self.choice = customtkinter.IntVar(value=0)

        radio_sel1 = customtkinter.CTkRadioButton(frame, text="Tag name", font=("Nata Sans", 15), value=1, variable=self.choice)
        radio_sel1.grid(row = 0, column=1, padx=20, pady=20)

        radio_sel2 = customtkinter.CTkRadioButton(frame, text="Class name", font=("Nata Sans", 15), value=2, variable=self.choice)
        radio_sel2.grid(row = 0, column=2, padx=20, pady=20)

        radio_sel3 = customtkinter.CTkRadioButton(frame, text="CSS celector", font=("Nata Sans", 15), value=3, variable=self.choice)
        radio_sel3.grid(row = 0, column=3, padx=20, pady=20)

        frame2 = customtkinter.CTkFrame(self, fg_color="transparent")
        frame2.pack(fill="x",pady=20)

        label_selector_name = customtkinter.CTkLabel(frame2, text="Choose selector name", font=("Nata Sans", 25))
        label_selector_name.pack(padx=20, anchor="w")

        self.entry_selector_name = customtkinter.CTkEntry(frame2, placeholder_text="Enter your selector name", height=35, width=300)
        self.entry_selector_name.pack(pady=20, padx=20, anchor="w")

        label_path = customtkinter.CTkLabel(frame2, text="Choose where to save the file", font=("Nata Sans", 25))
        label_path.pack(padx=20, anchor="w")

        btn_choose_folder = customtkinter.CTkButton(frame2, text="Choose path", command=self.path)
        btn_choose_folder.pack(pady=20, padx=20, anchor="w")

        self.selected_path = ""

        btn_start = customtkinter.CTkButton(self, text="Start", height=40, width=250, corner_radius=20, font=("Nata Sans", 30), command=self.run_program)
        btn_start.pack(pady=20, padx=20)

    def path(self):
        folder_path = filedialog.askdirectory(title="Choose path")
        self.selected_path = folder_path

    def run_program(self):
        url = self.entry.get()
        choice_value = self.choice.get()
        selector_name = self.entry_selector_name.get()
        
        self.cheak_input(url, choice_value, selector_name)

    def cheak_input(self, url, choice_value, selector_name):
        if url == "":
            messagebox.showwarning("Warning", "Please enter url")
        elif choice_value == 0:
            messagebox.showwarning("Warning", "Please choose selector")
        elif selector_name == "":
            messagebox.showwarning("Warning", "Please enter selector name")
        else:
            main.program(url, choice_value, selector_name, self.selected_path)
