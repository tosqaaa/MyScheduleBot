import requests
from bs4 import BeautifulSoup
import re
import os
from keys import exec_time
from xls2xlsx import XLS2XLSX
from bs4 import BeautifulSoup
from keys import SITE_LINK, MENU_LINK
import asyncio


def get_schedule_url():
    try:
        response = requests.get(url=SITE_LINK)
        response.raise_for_status()
    except Exception as ex:
        print(ex)

    soup = BeautifulSoup(response.text, "lxml")
    table = soup.find('table', {"class": "table table-bordered"})
    tbody = table.find('tbody')
    td = tbody.find("td")

    pattern = re.compile(".*Расписание_занятий_1_курс.*")
    result = next((link.get('href') for link in td.find_all('a')
                  if pattern.match(link.get('href'))), None)

    if result:
        return "https://vsu.by" + result
    else:
        return None


@exec_time
def download_file(link_to_file):
    try:
        pattern = re.compile(r"\d{2}.\d{2}.\d{4}-\d{2}.\d{2}.\d{4}")
        date = pattern.search(link_to_file)
        r = requests.get(link_to_file)
        with open(f"schedule({date.group()}).xls", "wb") as file:
            file.write(r.content)
        x2x = XLS2XLSX(f"schedule({date.group()}).xls")
        x2x.to_xlsx(f"schedule({date.group()}).xlsx")
        os.remove(f"schedule({date.group()}).xls")
        print("Успешно скачан файл с расписанием")
    except Exception as ex:
        print(ex)


async def get_file_name(SITE_LINK):

    response = requests.get(url=SITE_LINK)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    table = soup.find('table', {"class": "table table-bordered"})
    tbody = table.find('tbody')
    td = tbody.find("td")
    pattern = re.compile(".*Расписание_занятий_1_курс.*")
    link = next((link.get('href') for link in td.find_all('a')
                 if pattern.match(link.get('href'))), None)
    pattern = re.compile(r"\d{2}.\d{2}.\d{4}-\d{2}.\d{2}.\d{4}")
    result = pattern.search(link)
    # print(result.group())
    return result.group()


def get_menu(LINK=MENU_LINK):
    response = requests.get(url=MENU_LINK)
    soup = BeautifulSoup(response.text, "lxml")
    table = soup.find('table',{'class':"table table-bordered"})
    tds = table.find_all('td')
    for item in tds:
        yield item.text
    
    

# if __name__ == "__main__":
#     # get_menu()
#     download_file(get_schedule_url())