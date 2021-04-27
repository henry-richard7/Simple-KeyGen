import rstr
import re
import PySimpleGUI as sg
from threading import Thread


def pattern_gen(pattern):
    spl_characters = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
    if spl_characters.search(pattern) is not None:
        r = rstr.xeger(pattern.replace("X", "[A-Z]").replace("x", "[a-z]").replace("D", "\d"))
        r = re.sub(spl_characters, rstr.xeger("[@_!#$%^&*()<>?/\|}{~:]"), r)
        window['results'].print(r)
    else:
        r = rstr.xeger(pattern.replace("X", "[A-Z]").replace("x", "[a-z]").replace("D", "\d"))
        window['results'].print(r)


Layout = [

    [sg.Text("Python Key Generator", font=("", 40))],
    [sg.Text("Developed By Henry Richard J", font=("", 15), size=(30, 1))],
    [sg.Input(key="-sampleString-", font=("", 20))],
    [sg.Text("Number of keys to generate", size=(30, 1), font=("", 20))],
    [sg.Slider(range=(1, 100), default_value=5, size=(45, 20), font=("", 10), key="-No_Keys-",
               tooltip="Use The Slider To Choose Number Of Keys To Be Generated", orientation="horizontal")],
    [sg.Multiline(size=(100, 22), disabled=True, key="results", font=("", 10))],
    [sg.Button("Generate", key="-Generate-", font=("", 15))]

]
window = sg.Window('Python Key Generator', Layout, element_justification='center')
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-Generate-":
        replaced = re.sub(r"[A-Z]", "X", values['-sampleString-'])
        replaced = re.sub(r"[a-z]", "x", replaced)
        replaced = re.sub(r"[0-9]", "D", replaced)

        for i in range(int(values["-No_Keys-"])):
            Thread(target=pattern_gen, args=(replaced,)).start()
