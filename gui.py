# Худяков Иван Андреевич 44-22-112 вариант 26

import PySimpleGUI as sg
from calculate import calculate


layout = [
    [sg.Text("Входные данные через пробел")],
    [sg.Input(enable_events=True, key="-INPUT-")],
    [sg.Button("Рассчитать")],
    [sg.Listbox(values=[], enable_events=True, key="-LISTBOX-", size=(80, 40))]
]

window = sg.Window("Вычислить значение функции", layout, font=("Calibri, 12"))

while True:
    event, values = window.read()
    if event == "Рассчитать":
        args = values['-INPUT-'].strip().split(" ")
        results = calculate(*args)
        for i in range(len(results)):
            if results[i] is None:
                results[i] = f"{args[i]}: Ошибка вычисления"
            else:
                results[i] = f"{args[i]}: {results[i]:.4f}"
        window["-LISTBOX-"].update(results)
    if event == sg.WIN_CLOSED:
        break

window.close()