from persian_names import fullname_en
from random import randrange
from re import compile, findall
from datetime import date
from .providers import *

providersArray = ['gmail', 'yahoo', 'outlook', 'proton']
randomProvider = providersArray[randrange(len(providersArray))]
randomName = fullname_en('r').split()
thisYear = date.today().year


def generate(emailProvider=randomProvider, firstName=randomName[0], lastName=randomName[1], birthYear=thisYear):
    specialCharacters = ['', '.', '_', '-']
    firstCharacter = specialCharacters[randrange(len(specialCharacters))]
    randomNumber = ['', birthYear, randrange(10)][randrange(3)]
    namesOrder = [firstName, lastName][randrange(2)]

    if randomNumber == '':
        secondCharacter = ''
    else:
        secondCharacter = specialCharacters[randrange(len(specialCharacters))]

    if namesOrder == firstName:
        first = firstName
        second = lastName
    else:
        first = lastName
        second = firstName

    if '.' in emailProvider:
        providerDomain = emailProvider.strip('@ ').lower()
    else:
        providerDomain = providers[emailProvider.strip('@ ').replace(' ', '').lower()]

    userName = first + firstCharacter + second + secondCharacter + str(randomNumber)
    emailAddress = userName + '@' + providerDomain
    return emailAddress


def validate(emailAddress):
    checkValidation = compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    userName = findall(r'(.*)@', emailAddress)

    if checkValidation.match(emailAddress) and len(str(userName[0])) <= 64:
        return True
    else:
        return False
