import psutil
from plyer import notification
import time
import matplotlib.pyplot as plt

bat_perc = []
tps = []

while(True):
    battery = psutil.sensors_battery()
    percent = battery.percent
    localtime = time.localtime()
    
    if percent >= 40:
        notification.notify(
            title="Battery Percentage",
            message=str(percent)+"% Battery remaining",
            timeout=1,
            ticker="notif batterie"
        )
    else:
        notification.notify(
            title="Battery Percentage",
            message=str(percent)+"% Battery remaining. You need to chargeyour laptop !",
            timeout=1,
            ticker="notif batterie"
        )
    print("Battery Percentage :", str(percent), "% battery remaining at", localtime[3], 
          "h and", localtime[4], "min")
    bat_perc.append(percent)
    tps.append("%sh %smin" % (localtime[3], localtime[4]))

    plt.plot(tps, bat_perc)
    plt.show()

    time.sleep(60*30)
     
    continue
