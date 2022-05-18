import PySimpleGUI as sg

## Definir o conteúdo da janela

layout= [[sg.Text('Qual o seu nome?  :')],
[sg.Input(key='-INPUT-')],
[sg.Text(size=(40,1),key='-OUTPUT-')],
[sg.Button('OK'),sg.Button('Sair')]]

## Criar a janela

window= sg.Window('Título do programa',layout)

# Criar os loops e ações

while True:
    event,values= window.read()
    #Validação usuário sair ou janela for fechada
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    window['-OUTPUT-'].update('Olá ' +values['-INPUT-'] + " Gravando Saída na Interface")
    

close()