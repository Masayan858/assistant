import config
import speechRecognition as sr
import speechSynthesis as ss
import random
import teams
import openAI


def s_s(voices):
    res = filters(voices)
    print(res)
    gpt(res)


def gpt(request):
    answer = openAI.GPT()
    res = answer.request(request)
    ss.va_speak(res)


def filters(cmd):
    cmd = cmd.lower()
    for x in config.VA_APPEAL:
        cmd = cmd.replace(x, "").strip()
    for y in config.sort:
        cmd = cmd.replace(y, "").strip()
    return cmd


def va_respond(voice: str):
    if voice.startswith(config.VA_APPEAL):
        ss.va_speak(random.choice(config.ANSWER))


# начать прослушивание команд
sr.va_listen(va_respond)