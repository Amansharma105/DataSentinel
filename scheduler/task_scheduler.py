from apscheduler.schedulers.background import BackgroundScheduler


class TaskScheduler:

    def __init__(self):

        self.scheduler = BackgroundScheduler()

    def start(self):

        self.scheduler.start()

        print("Scheduler Started")
