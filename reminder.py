import time
#import datetime
#current_time = datetime.datetime.now()
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title = ("Submit Java Observation Sheet"),#message=("Deadline : 11:59 PM  ",current_time.day),
        #app_icon ="C:\Users\chaud\VSCODe\icons8-java-100.ico",
        timeout=10

    )