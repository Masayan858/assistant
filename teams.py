import webbrowser as wb
import pyautogui as pug
import alsaaudio as alsa
import speechSynthesis as ss


def web(voice):
    UrlMusic = 'https://www.youtube.com/watch?v=Fvw4vOXyBPU&list=PL_ItEEnpX0y6KEr9Cj4bObVNIoK4P2vMb&index=1'
    if voice.startswith('видео'):
        you = voice.replace("видео ", '')
        url = f"https://www.youtube.com/results?search_query={you}"
        wb.open_new_tab(url)
        pug.sleep(5)
        pug.press('enter')
    elif voice == 'музыка':
        wb.open_new_tab(UrlMusic)
    elif voice.startswith('найди'):
        gog = 'https://google.com/search?q=' + voice
        wb.open_new_tab(gog)
    else:
        ss.va_speak('я не поняла')


def valume(degree):
    cmd = degree.replace('сделай', '').strip()
    mix = alsa.Mixer()
    now = mix.getvolume()
    now = now[0]
    if cmd == 'громче':
        res = now * 2
        if res > 100:
            mix.setvolume(100)
        elif res < 1:
            res += 10
            mix.setvolume(res)
        else:
            mix.setvolume(res)
    elif cmd == 'тише':
        res = now // 2
        mix.setvolume(res)
    elif cmd == 'потише':
        now -= 10
        if now < 0:
            mix.setvolume(0)
        else:
            mix.setvolume(int(now))
    elif cmd == 'погромче':
        now += 10
        if now > 100:
            mix.setvolume(100)
        else:
            mix.setvolume(int(now))
    elif cmd.startswith('громкость'):
        cmd = cmd.replace('громкость на', '').strip()
        cmd = int(cmd)
        mix.setvolume(cmd)
    else:
        ss.va_speak('я не поняла')


def scroll(bias):
    if bias == 'ниже':
        pug.scroll(-7)
    elif bias == 'выше':
        pug.scroll(7)
    else:
        bias = int(bias)
        pug.sleep(5)
        pug.scroll(bias)

# valume('сделай громкость на 0')
