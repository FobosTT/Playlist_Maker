from creating_playlist import *
import PySimpleGUI as sg


def __main__(b_dir, s_dir, k_dir, b_num, s_num, k_num):
    audio_files_result = audio_files_lists(b_dir, s_dir, k_dir)
    organized_playlist = split_and_append(b_num, s_num, k_num, audio_files_result[0], audio_files_result[1], audio_files_result[2])
    playlist_to_file(values["-IN_NAME-"]+'.m3u', organized_playlist)


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
        # if os.path.isdir("-IN1-") or os.path.isdir("-IN2-") or os.path.isdir("-IN3-") is False:
        #     sg.popup_error("Check the paths")
        #     exit()
        # 
        # elif values["-INb-"].isdigit() or values["-INs-"].isdigit() or values["-INk-"].isdigit() is False:
        #     sg.popup_error("Not valid numbers!")
        #     exit()
        # 
        # else:
        __main__(values["-IN1-"], values["-IN2-"], values["-IN3-"],
                 int(values["-INb-"]), int(values["-INs-"]), int(values["-INk-"]))
        window.close()
        