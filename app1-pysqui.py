
## Importar a Biblioteca PySimpleGUI

import PySimpleGUI as sg

layout =[[sg.Text('Olá, estou exibindo uma mensagem'),[sg.Button('Ok')]]]

## Criar a janela

window= sg.Window('Título Programa1 ',layout)

## Criar o loop do evento

while True:
    event,values =window.read()
    #Finalizar o programa quando o usuário fechar a janela ou apertar ok
    if event == 'OK' or event == sg.WIN_CLOSED:
        break

window.close()