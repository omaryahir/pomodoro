from datetime import datetime, timedelta
from os import system

a = datetime.today() + timedelta(minutes=20)
continuar = True;

seconds = 0
diff = 0
while continuar:
    b = datetime.today()
    if b >= a:
        continuar = False
    else: 
        #system("clear")
        diff = a - b
        minutes = (diff.seconds + diff.microseconds / 1000000) / 60

        if seconds != diff.seconds:
            seconds = diff.seconds
            msg = "%s" % diff
            system("clear")
            print  " Counting ...     %s" % msg[0:-7]
            #print "%s" % (minutes)


msg="Ready, I count 20 minutes."
command="%s %s" % ("spd-say",msg)
system(command)