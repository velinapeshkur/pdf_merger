import PySimpleGUI as sg


sg.theme("LightBrown1")

label1 = sg.Text("Select folder:")
input1 = sg.Input()
choose_button = sg.FolderBrowse("Choose", key="folder")

label2 = sg.Text("Pages per file:")
input2 = sg.Input(key="pages")

merge_button = sg.Button("Merge")
output_label = sg.Text(key="output")

window = sg.Window("PDF Merger",
                   layout=[
                       [label1], [input1, choose_button],
                       [label2], [input2], 
                       [merge_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case sg.WIN_CLOSED:
            break
        case _:
            pass

window.close()
