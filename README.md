繼上篇→ [取得目前播放的歌曲 顯示於視窗提供直播擷取](https://hackmd.io/@IBM5100/rJvd9mgk6)  
由於我發現OBS的文字來源其實可以讀檔，而且是會即時更新的(如下)  

![](https://hackmd.io/_uploads/rJOhqR9ya.png)

所以就弄了一個文字版，省了產生panel的麻煩，也少一個視窗和吃的資源  
code很短就直接貼了  
```
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
```
主要邏輯跟上篇一樣，只是變成產生完文字檔就沒事了，之後就交給OBS處理  
基本上只會吃20MB左右的記憶體  
![](https://hackmd.io/_uploads/rJkk3A51p.png)  

就這樣，沒了，8888888888