import PySimpleGUI as sg

layout = [[sg.Text("test")]]
window = sg.Window("テストアプリ",layout,size=(300,150))

window.read()