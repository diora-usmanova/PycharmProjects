#CLOCK COUNTDOWN

import time
seconds = eval(input("Enter the number of seconds"))
time.sleep(seconds)
if seconds >= seconds - 1:
    print(seconds - 1, "Seconds remaining")
    if seconds >= seconds - 2:
        print(seconds - 2 , "Seconds remaining")
    if seconds == seconds:
        print("Stopped")



