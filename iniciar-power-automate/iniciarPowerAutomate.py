import pyautogui
import subprocess
import os
import time
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

def executarAutomate():
    print("Começou!!!")
    time.sleep(10)

    x1 = 256
    y1 = 53

    pyautogui.click(x1,y1)
    print("Operação Concluída com Sucesso!")

scheduler.add_job(executarAutomate, 'cron', hour='23', minute='30')

scheduler.start()

