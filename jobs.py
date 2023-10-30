from apscheduler.schedulers.background import BackgroundScheduler
# #https://apscheduler.readthedocs.io/en/3.x/userguide.html api importante ler se tiver dúvida
import time
import json
#***************************************JOB****************************************************
def job():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

#use quando você não estiver usando nenhuma das estruturas abaixo
#   e quiser que o agendador seja executado em segundo plano dentro do seu aplicativo

def inicializar_job():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=job, trigger='cron', hour=10, minute=47)
    scheduler.start()
    # scheduler.add_job(job, 'date', run_date='2023-09-24 15:41:00')
    # schedule.every().day.at("15:36").do(job)
    #cron tab

#**********************************************************************************************
#************************************PROGRESS BAR**********************************************
class Config:
    num_bars = 1
    prog_inc = 10
    update_rate = 1

# Instantiate app_config
app_cfg = Config

def progress_bar():
    def generate():
        x = 0
        while x <= 100:
            #vid_dict['suresh']="0"
            vid_dict = {}
            for bar in range(0,app_cfg.num_bars):
                vid_dict[bar] = min(x+bar*app_cfg.prog_inc,100)
            #yield "data:" + str(x) + "\n\n"
            ret_string = "data:" + json.dumps(vid_dict) + "\n\n"
            print(ret_string)
            yield ret_string
            x = x + 10
            time.sleep(app_cfg.update_rate)
    return generate()
#**********************************************************************************************