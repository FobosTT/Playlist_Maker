from creating_playlist import *
import PySimpleGUI as PSG

PSG.set_options(border_width=0, margins=(0, 0), element_padding=(5, 3))
layout = [[PSG.Text("Bachata music:"), PSG.Input(key="-IN2-", change_submits=True), PSG.FolderBrowse(key="-IN1-")],
          [PSG.Text("Salsa music:"), PSG.Input(key="-IN4-", change_submits=True), PSG.FolderBrowse(key="-IN3-")],
          [PSG.Text("Kizomba music:"), PSG.Input(key="-IN6-", change_submits=True), PSG.FolderBrowse(key="-IN5-")],

          [PSG.Button("Create")]]

window = PSG.Window("Playlist Maker", layout, size=(600, 150))

window()

while True:
    event, values = window.read()
    print(values["-IN2-"])
    if event == PSG.WIN_CLOSED or event == "Exit":
        break
    elif event == "Create":
        bachata_dir = values["-IN1-"]
        salsa_dir = values["-IN3-"]
        kizomba_dir = values["-IN5-"]
