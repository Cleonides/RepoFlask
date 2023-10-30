#https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys
import pyautogui as gui
import time

#TODO pegar o clique do mouse , ele pega a coordenada do clique do botão.
# time.sleep(5)
# print(gui.position())
#
#
gui.PAUSE = 0.3 #pausa a cada comando
gui.size()

#entrar no crhome
gui.press('win')
gui.write('chrome')
gui.press('enter')

time.sleep(1)

#entrar no link#
link = "https://www.dadosdemercado.com.br/bolsa/acoes"
gui.write(link)
gui.press('enter')

time.sleep(5)
 #clica no botão de baixar os arquivos.
gui.click(x=220, y=435)
gui.press('enter')

time.sleep(3)

gui.click(x=1191, y=695)
gui.press('enter')

# time.sleep(1)
# gui.click(x=1299, y=691)
# gui.press('enter')

time.sleep(3)

gui.press('esc')

time.sleep(3)

gui.press('esc')
