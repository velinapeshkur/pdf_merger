import PySimpleGUI as sg
from app import merge_pdf


sg.theme("LightGrey1")

label1 = sg.Text("Select folder:")
input1 = sg.Input()
choose_button = sg.FolderBrowse("Browse", key="folder")

label2 = sg.Text("Files per output file:")
input2 = sg.Input(key="files")

merge_button = sg.Button("Merge", pad=(5,13))
output_label = sg.Text(key="output")

window = sg.Window("PDF Merger",
                   layout=[
                       [label1], [input1, choose_button],
                       [label2], [input2], 
                       [merge_button, output_label]],
                   font=("San Francisco", 14))

while True:
    event, values = window.read()
    match event:
        case sg.WIN_CLOSED:
            break
        case _:        
            folder_path = values["folder"]
            files_per_file = values["files"]
            response = merge_pdf(folder_path, files_per_file)
            
            if response["success"]:
                window["output"].update(value="Merge completed", 
                                        text_color="green")
            else:
                window["output"].update(value=response["error"], 
                                        text_color="red")

window.close()
