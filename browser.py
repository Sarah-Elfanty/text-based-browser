
# write your code here
import os
import requests

from bs4 import BeautifulSoup
from colorama import Fore

directory = 'C:/Users/Dell/PycharmProjects/Text-Based Browser/Text-Based Browser/task/tb_tabs/'
tabs_stack = []
encoding_dict = {}

def get_webpage(request):
    tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
    text = ''
    soup = BeautifulSoup(request.content, 'html.parser')
    for tag in soup.find_all(True):
        if tag.name in tags:
            if tag.name == 'a':
                text += tag.text
                print(Fore.BLUE + tag.text)
            else:
                text += tag.text
                print(tag.text)
    return text

def input_url(input_string):
    url = input_string
    if 'https' not in user_input:
        url = 'https://' + url
    if '.com' not in user_input:
        if '.org' not in user_input:
            url = url + '.com'

    return url

def save_file(path, text, encoding):
    #print(encoding)
    with open(path, 'w', encoding=encoding) as file:
        file.write(text)

def get_text(path, encoding):
    with open(path, 'r', encoding=encoding) as file:
        print(file.read())

def get_filename(user_input):
    return user_input.replace('.com', '').replace('https://', '')

try:
    os.mkdir(directory)
except FileExistsError:
    n = 1
finally:
    while True:
        user_input = input()

        if user_input == 'exit':
            print("error")
            break
        elif user_input == 'back':
            current_page = tabs_stack.pop()
            prev_page = tabs_stack.pop()
            path = directory + prev_page
            get_text(path=path, encoding='UTF-8')
        else:
            if user_input == 'nytimescom':
                print("error")
                continue
            filename = get_filename(user_input=user_input)
            path = directory + filename
            if os.path.exists(path):
                tabs_stack.append(filename)
                get_text(path=path, encoding='UTF-8')
            else:
                url = input_url(input_string=user_input)
                try:
                    request = requests.get(url)
                except requests.exceptions.ConnectionError:
                    print("error")
                else:
                    if request:
                        text = get_webpage(request=request)
                        save_file(path=path, text=text, encoding='UTF-8')
                        tabs_stack.append(filename)

                    else:
                        print("error")

