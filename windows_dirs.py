import PySimpleGUI as sg
import os
import subprocess
import threading

from PySimpleGUI.PySimpleGUI import WIN_CLOSED

current_dir = os.getcwd()

def command(command):      
    try:
        output = subprocess.check_output(f"{os.system(command)}".format(), stderr=subprocess.STDOUT, shell=True)
    except:
        output = "Failed to execute"
    #print(output)
    return output

layout = [
    [sg.Text(current_dir)],
    [sg.Text("Input a command:")],
    [sg.Input()],
    [sg.Button("Submit")],
]

window = sg.Window("window", layout)

def gui_thread():
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Submit":
            try:
                cmd_thread = threading.Thread(target=command, args=(values[0],)).start()
            except KeyboardInterrupt:
                print("Quitting command thread")
            if WIN_CLOSED and not cmd_thread:
                print("Closed")


if __name__ == '__main__':
    try:
        gui_thread()
    except KeyboardInterrupt:
        print("Exiting program")
        print("Closed")