import PySimpleGUI as sg
from app import merge_pdf


sg.theme("LightGrey1")

select_folder_label = sg.Text("Select folder:")
select_folder_input = sg.Input()
browse_button = sg.FolderBrowse("Browse", key="folder")

files_per_output_label = sg.Text("Files per output file:")
files_per_output_input = sg.Input(key="files")

merge_button = sg.Button("Merge", pad=(5,13))
output_label = sg.Text(key="output")

window = sg.Window("PDF Merger",
                   layout=[
                       [select_folder_label], 
                       [select_folder_input, browse_button],
                       [files_per_output_label], 
                       [files_per_output_input], 
                       [merge_button, output_label]],
                   font=("San Francisco", 14))

while True:
    event, values = window.read()
    match event:
        case sg.WIN_CLOSED:
            break
        case _:      
            folder_path = values["folder"]
            files_per_file_input = values["files"]
            response = merge_pdf(folder_path, files_per_file_input)
            
            if response["success"]:
                window["output"].update(value="Merge completed", 
                                        text_color="green")
            else:
                window["output"].update(value=response["error"], 
                                        text_color="red")

window.close()
