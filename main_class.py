from music_class import*
import PySimpleGUI as sg


def __main__(b_dir, s_dir, k_dir, b_num, s_num, k_num):
    bachata = Music(b_dir, b_num, 0, [])
    salsa = Music(s_dir, s_num, 0, [])
    kizomba = Music(k_dir, k_num, 0, [])
    bachata.files()
    salsa.files()
    kizomba.files()
    while bachata.loop_index < len(bachata.music_list) \
            or salsa.loop_index < len(salsa.music_list)\
            or kizomba.loop_index < len(kizomba.music_list):
        bachata.split()
        salsa.split()
        kizomba.split()
    Music.playlist_to_file(values["-IN_NAME-"], Music.playlist)


sg.set_options(border_width=0, margins=(0, 0), element_padding=(5, 3))
layout = [[sg.Text("Bachata music:"), sg.Input(key="-IN1-", change_submits=True), sg.FolderBrowse(),
           sg.Text("Number of tracks"), sg.Input(key="-INb-")],
          [sg.Text("Salsa music:"), sg.Input(key="-IN2-", change_submits=True), sg.FolderBrowse(),
           sg.Text("Number of tracks"), sg.Input(key="-INs-")],
          [sg.Text("Kizomba music:"), sg.Input(key="-IN3-", change_submits=True), sg.FolderBrowse(),
           sg.Text("Number of tracks"), sg.Input(key="-INk-")],
          [sg.Text("Playlist Name:"), sg.Input(key="-IN_NAME-")],
          [sg.Exit()], [sg.Button("Create")]]

window = sg.Window("Playlist Maker", layout, size=(600, 150))

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Create":
        # if os.path.exists("-IN1-") or os.path.exists("-IN2-") or os.path.exists("-IN3-") is False:
        #     sg.popup_error("Check the paths")
        #     window.close()
        #     window = sg.Window("Playlist Maker", layout, size=(600, 150))
        # elif values["-INb-"].isnumeric() or values["-INs-"].isnumeric() or values["-INk-"].isnumeric() is False:
        #     sg.popup_error("Not valid numbers!")
        #     window.close()
        #     window = sg.Window("Playlist Maker", layout, size=(600, 150))
        # else:
        __main__(values["-IN1-"], values["-IN2-"], values["-IN3-"],
                 int(values["-INb-"]), int(values["-INs-"]), int(values["-INk-"]))
        window.close()
