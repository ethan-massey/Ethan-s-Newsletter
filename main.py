#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import email_manager
import datetime as dt
import time

def send_email():
    email_manager.send_message()
    print('email sent at ' + str(dt.datetime.now()))

def send_email_at(send_time):
    time.sleep(send_time.timestamp() - time.time())
    send_email()

def main():
    first_email_time = dt.datetime(2020, 2, 18, 23, 7, 0)
    interval = dt.timedelta(minutes=60*24*7)  # interval = every week

    send_time = first_email_time
    while True:
        try:
            send_email_at(send_time)
            send_time = send_time + interval
        except:
            # send email one minute from now
            now = dt.datetime.now()
            send_time = now + dt.timedelta(minutes=1)
            send_email_at(send_time)

            # calculate next monday, 8:00am
            while now.weekday() != 2:
                now += dt.timedelta(days=1)
            while now.hour != 19:
                now += dt.timedelta(hours=1)
            while now.minute != 45:
                now += dt.timedelta(minutes=1)
            send_time = now + interval


if __name__ == "__main__":
    main()