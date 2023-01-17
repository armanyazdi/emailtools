from persian_names import fullname_en
from random import randrange
from re import compile, findall
from datetime import date
from .providers import *

providers_list = ['gmail', 'yahoo', 'outlook', 'proton']
random_provider = providers_list[randrange(len(providers_list))]
random_name = fullname_en('r').split()
this_year = date.today().year


def generate(provider=random_provider, firstname=random_name[0], lastname=random_name[1], birthyear=this_year):
    characters = ['', '.', '_', '-']
    first_char = characters[randrange(len(characters))]
    random_num = ['', birthyear, randrange(10)][randrange(3)]
    names_order = [firstname, lastname][randrange(2)]

    if random_num == '':
        second_char = ''
    else:
        second_char = characters[randrange(len(characters))]

    if names_order == firstname:
        first = firstname
        second = lastname
    else:
        first = lastname
        second = firstname

    if '.' in provider:
        domain = provider.strip('@ ').lower()
    else:
        domain = providers[provider.strip('@ ').replace(' ', '').lower()]

    username = first + first_char + second + second_char + str(random_num)
    email = username + '@' + domain
    return email


def validate(email):
    is_valid = compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    username = findall(r'(.*)@', email)

    if is_valid.match(email) and len(str(username[0])) <= 64:
        return True
    else:
        return False
