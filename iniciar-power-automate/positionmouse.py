import pyautogui
import time

# Loop infinito para atualizar continuamente a posição do mouse
while True:
    # Obtém e imprime a posição atual do mouse
    x, y = pyautogui.position()
    print('X = {}, Y = {}'.format(x, y))
    time.sleep(1)