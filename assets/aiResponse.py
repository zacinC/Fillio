from openai import OpenAI
import pyautogui as pg
import pyperclip

options = {"excuse": "Write me an excuse for this message", "acception": "Write me an acception for this offer (write it like you're me) so I can send it to them.", "rejection": "Write me a rejection",
           "summarize": "%", 'explain': "Explain this in detail and easy to understand"}


def message_validation(message):
    # Ovdje treba dodati mogucnost prevodjenja. Samo treba vidjeti kako da se doda opcija za jezik...
    message = message.lstrip().rstrip().lower()
    start = message.find('--')
    end = message.find('--', start+2)
    message_length = len(message)
    if start != 0 and end+2 != message_length:
        response = '''the optional string must be specified at the beginning or end of the message.
                  IE. --shortly summarized-- [message text...]
                or [message text...] --excuse--  
              '''
    elif start != 0 and end+2 == message_length or start == 0 and end+2 != message_length:
        if message[start+2:end] in options.keys():
            # print(message[start+2:end])
            # print(message.replace(message[start:end+2], ''))
            prompt = message.replace(message[start:end+2], '')
            response = assistant(prompt, message[start+2:end])
    return response


def assistant(prompt, option=''):
    client = OpenAI()
    if option == 'summarize':
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional assistant capable to always summarizing the shortest way possible, summarize this in a couple of very very short sentences, or a couple words!"},
                {"role": "user", "content": prompt},
            ]
        )
    else:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant you always write messages like you are me and in Bosnian. " + option},
                {"role": "user", "content": prompt},
            ]
        )
    resMessage = response.choices[0].message
    assistants_message = response.choices[0].message.content

    return assistants_message
