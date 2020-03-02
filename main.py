#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import email_manager
import datetime as dt


def send_email():
    email_manager.send_message()
    print(str(dt.datetime.now()) + ' - email sent', flush=True)


def main():

    send_email()

if __name__ == "__main__":
    main()