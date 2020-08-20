#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import datetime as dt
import urllib.request


# connected to internet?
def is_connected(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


def main():
    if is_connected():
        # send email
        import email_manager
        email_manager.send_message()
        print(str(dt.datetime.now()) + ' - email sent', flush=True)
    else:
        # print error message
        print(str(dt.datetime.now()) + ' - ERROR: No internet connection', flush=True)


if __name__ == "__main__":
    main()
