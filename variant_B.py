import tkinter as tk
from tkinter import ttk, messagebox
import random
import csv

root = tk.Tk()
root ["bg"] = "purple"
root.geometry('600x400')
root.maxsize(600, 400)

class RandomDataTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Таблиця з випадковими даними")
        
    
        frame = tk.Frame(root)
        frame.pack(pady=10)
        

        self.table = ttk.Treeview(frame, columns=("A", "B", "C"), show="headings")
        self.table.heading("A", text="Колонка A")
        self.table.heading("B", text="Колонка B")
        self.table.heading("C", text="Колонка C")
        self.table.pack(pady=10)
        

        self.populate_table()
        
       
        format_a_button = tk.Button(root, text="Форматувати по A", command=self.format_by_column_a)
        format_a_button.pack(pady=5)
        
        format_b_button = tk.Button(root, text="Форматувати по B", command=self.format_by_column_b)
        format_b_button.pack(pady=5)
        
        save_button = tk.Button(root, text="Зберегти у файл", command=self.save_to_file)
        save_button.pack(pady=10)
    
    def populate_table(self):

      
        for row in self.table.get_children():
            self.table.delete(row)
        
      
        for _ in range(10):
            row = (
                random.randint(1, 100),     
                random.choice(["X", "Y", "Z"]),
                round(random.uniform(10, 99), 2) 
            )
            self.table.insert("", "end", values=row)
    
    def format_by_column_a(self):
       
        for row in self.table.get_children():
            col_a_value = int(self.table.item(row, "values")[0])
           
            if col_a_value > 50:
                self.table.item(row, tags=("highlight",))
            else:
                self.table.item(row, tags=("normal",))
        
        
        self.table.tag_configure("highlight", background="lightblue")
        self.table.tag_configure("normal", background="white")
    
    def format_by_column_b(self):
        """Format rows based on the values in Column B"""
        for row in self.table.get_children():
            col_b_value = self.table.item(row, "values")[1]
            
            if col_b_value == "X":
                self.table.item(row, tags=("highlight",))
            else:
                self.table.item(row, tags=("normal",))
        
        self.table.tag_configure("highlight", background="lightgreen")
        self.table.tag_configure("normal", background="white")
    
    def save_to_file(self):
        """Save the table data to a CSV file"""
        with open("table_data.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Колонка A", "Колонка B", "Колонка C"])
            for row in self.table.get_children():
                writer.writerow(self.table.item(row, "values"))
        
        messagebox.showinfo("Збереження", "Дані збережено у файлі 'table_data.csv'")



app = RandomDataTableApp(root)
root.mainloop()