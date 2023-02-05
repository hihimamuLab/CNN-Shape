
import PySimpleGUI as sg

def conv_output_size(input_size_h,input_size_w,padding_size,filter_h,filter_w,stride):
    Oh = (input_size_h + padding_size * 2 - filter_h)/stride + 1
    Ow = (input_size_w + padding_size * 2 - filter_w)/stride + 1
    return Oh, Ow

layout = [
    [sg.Text('CNNの出力画像サイズを算出するアプリです')],
    [sg.Text("入力画像縦幅"),sg.InputText(key="-input_size_h-")],
    [sg.Text("入力画像横幅"),sg.InputText(key="-input_size_w-")],
    [sg.Text("パディングサイズ"),sg.InputText(key="-padding_size-")],
    [sg.Text("フィルター縦幅"),sg.InputText(key="-filter_h-")],
    [sg.Text("フィルター横幅"),sg.InputText(key="-filter_w-")],
    [sg.Text("ストライド"),sg.InputText(key="-stride-")],
    [sg.Button("実行",key="-submit-")],
    [sg.Output(size=(50,10),key="-OUTPUT-")]
]

window = sg.Window('CNNの出力画像サイズを算出',layout,size=(600,300))

while True:
    event, values = window.read()
    if event == "-submit-":
        
        input_size_h,input_size_w = int(values["-input_size_h-"]),int(values["-input_size_w-"])
        
        padding_size = int(values["-padding_size-"])
        
        filter_h,filter_w = int(values["-filter_h-"]),int(values["-filter_w-"])
        
        stride = int(values["-stride-"])
        
        Oh,Ow = conv_output_size(input_size_h,input_size_w,padding_size,filter_h,filter_w,stride)
        window["-OUTPUT-"].update("")
        print(f"出力画像横幅{int(Ow)}")
        print(f"出力画像縦幅{int(Oh)}")
    if event == sg.WIN_CLOSED:
        break