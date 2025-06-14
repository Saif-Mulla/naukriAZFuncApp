import azure.functions as func
import datetime
import json
import logging
from naukri import run

app = func.FunctionApp()

@app.timer_trigger(schedule="0 35 5 * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def DailyTrigger(myTimer: func.TimerRequest) -> None:
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed at: %s',datetime.datetime.utcnow())
    run()