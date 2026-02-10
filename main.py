from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException 
from fpdf import FPDF
from tkinter import messagebox
import time
import json
import os
import sys
import gui

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def program(url, selector_type,  selector_item, path):

    selector_options = {
        1 : By.TAG_NAME,
        2 : By.CLASS_NAME,
        3 : By.CSS_SELECTOR,
    }


    driver = webdriver.Chrome()

    driver.get(f"{url}")

    time.sleep(1)

    while True:
        old_pos = driver.execute_script("return window.scrollY")
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(1)

        new_pos = driver.execute_script("return window.scrollY")

        if new_pos == old_pos:
            break
   
    results = driver.find_elements(selector_options[selector_type], selector_item)

    with open(resource_path('output.json'), 'r', encoding='utf-8') as file:
        data = json.load(file)

    data_to_load = {}

    num = 1

    for r in results:
        data_to_load[f"{num}"] = r.text
        num = num + 1 
        print(num,r.text)

    if len(results) == 0:
        driver.close()
        messagebox.showerror("Error", "Parser did not find any entries selector")

    else:
        with open(resource_path('output.json'), 'w', encoding='utf-8') as file:
            json.dump(data_to_load, file, indent=4, ensure_ascii=False)

        driver.close()

        convert(path)

def convert(path):
    try:
        with open(resource_path('output.json'), 'r', encoding='utf-8') as file:
            doc = json.load(file)
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font("DejaVuSans", "", resource_path("DejaVuSans.ttf"), uni=True) 
        pdf.set_font("DejaVuSans", size = 12)
        for key, val in doc.items():
            pdf.multi_cell(w=0,h=10, txt=f"{val}", align="L")
            pdf.ln(2)

        base_name = "output.pdf"
        file_name = base_name
        counter = 1
        while os.path.exists(os.path.join(path, file_name)):
            file_name = f"output{counter}.pdf"
            counter = counter + 1

        full_path = os.path.join(path, file_name)

        pdf.output(full_path)
        messagebox.showinfo("Status", "Your parsing is done!")
        os.startfile(full_path)
    except IndexError:
        messagebox.showerror("Error", "Failed to convert font to PDF")

if __name__ == "__main__":
    app = gui.App()
    app.mainloop()