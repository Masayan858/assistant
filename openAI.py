import openai


class GPT:
    def __init__(self):
        openai.api_key = "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"
        self.__messages = []
        print(self.__messages[:-1])

    def request(self, task):
        self.__messages.append({"role": "user", "content": task})
        answer = openai.ChatCompletion.create(
            model="text-davinci-002",
            messages=self.__messages
        )
        self.__messages.append({"role": "assistent", "content": answer.choices[0].message.content})
        return answer.choices[0].message.content


if __name__ == "__main__":
    assist = GPT()
    a = 0
    while a != 1:
        data = input(">>> ")
        if data == "стоп":
            a = 1
        else:
            print(f"GPT answer: {assist.request(data)}")
