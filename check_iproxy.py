import requests
import json
from datetime import datetime
import colorama
from colorama import Fore, Style
colorama.init()

def rent_date():
    url = "https://api.iproxy.online/v1/connections"
    headers = {"authorization": "PRXH8PT7CXHRCFG2P7GYCT2"}

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    results = data['result']  # get the 'result' list
    today = datetime.now().date()

    # create a list of tuples, where each tuple contains the element, its number of days left till the expiry date, and its number of days left till the date in the element's name
    elements_with_days = [(element['name'], (datetime.strptime(element['planDetails']['message'][-10:], '%d.%m.%Y').date() - today).days, (datetime.strptime(
        element['name'].split('-')[-1].strip(), '%d/%m/%Y').date() - today).days) for element in results if element.get('description', '') != '']

    # sort the list by number of days till the expiry date in ascending order
    sorted_elements_with_days = sorted(elements_with_days, key=lambda x: x[1])

    print(f"{Style.BRIGHT}{'Proxy': <21} {'Iproxy rent': <13} {'User rent': <16}{Style.RESET_ALL}\n")

    # print the sorted list in three columns
    for element, expiry_days, name_days in sorted_elements_with_days:
        if expiry_days <= 2:
            print(f"{element: <20}{Style.BRIGHT}{Fore.RED} {expiry_days:>3} days left {Style.RESET_ALL}{Fore.RESET} {Style.BRIGHT}{Fore.GREEN}{name_days:>3} days left{Style.RESET_ALL}{Fore.RESET}" if name_days <=
                  2 else f"{element: <20}{Style.BRIGHT}{Fore.RED}{expiry_days:>3} days left {Style.RESET_ALL}{Fore.RESET} {name_days:>3} days left")
        else:
            print(f"{element: <20} {expiry_days:>3} days left {Style.BRIGHT}{Fore.GREEN}{name_days:>3} days left{Style.RESET_ALL}{Fore.RESET}" if name_days <=
                  2 else f"{element: <20} {expiry_days:>3} days left {name_days:>3} days left")
