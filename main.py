import time
import pyautogui


def write_file(name):
    f = open("cs.txt", "w", encoding="utf-8")
    f.write(name)
    f.close()
    return


old = ""
while True:
    pot = pyautogui.getWindowsWithTitle("PotPlayer")
    if pot != []:
        now = pot[0].title
        if now != old:
            old = now
            idx = now.find(".mp3")
            if idx == -1:
                idx = now.find(".m4a")
                if idx == -1:
                    idx = now.find(".flac")
            if idx != -1:
                name = "Current Song: " + now[:idx]
                write_file(name)
    time.sleep(3)
