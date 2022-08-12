import camera as c
import time
import tftest
import lock 


lock.unlock()
if __name__ == "__main__":
    password = ["575:golf ball","505:coffee mug","575:golf ball"]
    c.configCamera()
    while (True):
        c.runVision()
        tftest.runVision()
        time.sleep(0.5)
        #
        startTime = time.monotonic()
        progress = 0

        while ((time.monotonic() - startTime) < 10):
            perc,name = tftest.runVision()
            print(f"{name}, {password[progress]}")
            if (name == password[progress]):
                progress += 1
                startTime = time.monotonic()
                if (progress == len(password)):
                    lock.lock()
                    break


        time.sleep(4)
        lock.lock()
        break

        