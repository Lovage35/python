import tkinter as tk
root = tk.Tk()
root ["bg"] = "black"
root.geometry('600x600')
root.maxsize(600, 600)
root.title('країни')



countries = [
    ("Україна", "Зеленський"),
    ("США", "Трамп"),
    ("Франція", "Макрон"),
    ("Німеччина", "Штайнмаєр"),
    ("Китай", "Сі"),
    ("Японія", "Кішіда"),
    ("Індія", "Мурму"),
    ("Канада", "Трюдо"),
    ("Бразилія", "Лула"),
    ("Велика Британія", "Сунак"),
    ("Італія", "Маттарелла"),
    ("Ізраїль", "Герцог")
]

class CountryApp:
    def __init__(self, root):
        self.root = root
        
        self.buttons = []
        for country, president in countries:
            button = tk.Button(root, text=country, font=("Arial", 14), command=lambda c=country, p=president: self.select_country(c, p))
            button.pack(pady=5)
            self.buttons.append((button, country))

    def select_country(self, selected_country, president):
        
        for button, country in self.buttons:
            if country == selected_country:
                button.config(text=f"{country} ({president})", font=("Arial", 14, "bold"))
            else:
                
                button.config(font=("Arial", 7))



app = CountryApp(root)
root.mainloop()