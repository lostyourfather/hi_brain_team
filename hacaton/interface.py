import json
from tkinter import *
import requests


def getElement(event):
    selection = event.widget.curselection()
    index = selection[0]
    value = event.widget.get(index)
    text.delete("1.0", "end")
    print(value)
    response = requests.get(f"http://0.0.0.0:7000/hacaton_endpoint?category={value}")
    text.insert(END, response.text)


root = Tk()
root.title("Рекомендательная система")
box = Listbox(selectmode=EXTENDED)
box.pack(side=LEFT)
categories = ["ML", "AR/VR", "аналитик данных", "Специалист по обласным вычислениям и распределенным системам", "геймдизайнер", "Образовательный дата-инженер"]
for category in categories:
    box.insert(END, category)
scroll = Scrollbar(command=box.yview)
scroll.pack(side=LEFT, fill=Y)
box.config(yscrollcommand=scroll.set)
f = Frame()
f.pack(side=LEFT, padx=10)
text = Text()
text.pack(side=RIGHT, padx=10)
box.bind('<<ListboxSelect>>', getElement)
root.mainloop()