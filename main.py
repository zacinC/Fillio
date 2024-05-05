from openai import OpenAI
import pyautogui as pg
import pyperclip

options = {"excuse": "Write me an excuse for this message", "acception": "Write me an acception", "rejection": "Write me an rejection",
           "shortly summarized": "summarize this message into a couple of short sentences"}


def message_validation(message):
    # Ovdje treba dodati mogucnost prevodjenja. Samo treba vidjeti kako da se doda opcija za jezik...
    message = message.lstrip().rstrip()
    start = message.find('--')
    end = message.find('--', start+2)
    message_length = len(message)
    if start != 0 and end+2 != message_length:
        print('''the optional string must be specified at the beginning or end of the message.
                  IE. --shortly summarized-- [message text...]
                or [message text...] --excuse--  
              ''')
        return False
    elif start != 0 and end+2 == message_length or start == 0 and end+2 != message_length:
        if message[start+2:end] in options.keys():
            # print(message[start+2:end])
            # print(message.replace(message[start:end+2], ''))
            prompt = message.replace(message[start:end+2], '')
            assistant(prompt, message[start+2:end])
        return True


def assistant(prompt, option=''):
    client = OpenAI()
    # Treba razdvojiti ovo po iffovima za opcije iz prompta jer se tako stedi na tokenima, a i povecava mogucnost za dobijanje preciznijeg odgovora
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant you always write messages like you are me and in Bosnian. " + option},
            {"role": "user", "content": prompt},
        ]
    )
    resMessage = response.choices[0].message
    assistants_message = response.choices[0].message.content
    # print(resMessage)
    # print('----------------------------------------------')
    print(assistants_message)
    pyperclip.copy(assistants_message)
    # pg.hotkey('ctrl', 'v')


# message = '''
# Tate Reeves✔
# Just Now
# Friends (hint: this is one of the long ones) I want you to know what our team is doing on behalf of our fellow Mississippians.
# ...
# #1 we are not panicking. As we do with every emergency (tornado, hurricane, flooding, ice storm, and this pandemic), we are calmly making decisions based on the best available data to manage the situation and mitigate its impact on our people.
# My number one goal from day one of this pandemic has always been to protect the integrity of our health care system. The current phase of the pandemic seems more and more like a "pandemic of the unvaccinated" - as the Delta variant has had very few breakthrough cases amongst those who have "gotten the shot" - but the goal remains the same: ensure everyone that can get better with quality care receives that quality care!
# Total hospitalizations remain below where they were at our peak from August of 2020. Total number of patients in ICU beds remains at or near our peak levels from August of 2020.
# Honestly, the real challenge is NOT the physical beds - hospital beds or ICU beds. The challenge is our hospitals may not have an adequate number of health care professionals (docs, nurses, respiratory therapists, etc.) to staff those beds. Unfortunately, I've been advised hospitals throughout Mississippi have lost nearly 2,000 nurses over the last year. There is a labor shortage in most industries throughout America today and health care is no different. Some hospitals lost staff because they laid off employees that never came back. Some staff left due to administrative decisions (such as mandating vaccines). But the reason for the shortage can be debated in the future.....the task at hand is to help backfill these vacancies to protect the integrity of our healthcare system.
# --shortly summarized--
# '''
# message_validation(message)
message_validation("Ajde na fudbal veceras ako mozes? --rejection--")
