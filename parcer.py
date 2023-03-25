import requests
import re
import os
from keys import exec_time
from xls2xlsx import XLS2XLSX
from bs4 import BeautifulSoup
from keys import SITE_LINK


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
        
        
        
def check_and_download():
    # response = 
    pass
download_file(get_schedule_url())