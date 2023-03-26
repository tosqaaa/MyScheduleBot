
from keys import RANGES_DAYS, RANGES_GROUPS
import openpyxl
import re
import os


pattern = re.compile(r".*\d{2}.\d{2}.\d{4}-\d{2}.\d{2}.\d{4}.*")
for file in os.listdir("./"):
    if re.match(pattern, file):
        end_week_day = (pattern.search(file).group()[9:30])
        wb = openpyxl.load_workbook(os.path.join('./', file))
        ws = wb.active      

def getMergedCellVal(sheet, cell):
    rng = [s for s in sheet.merged_cells.ranges if cell.coordinate in s]
    return sheet.cell(rng[0].min_row, rng[0].min_col).value if len(rng) != 0 else cell.value


def getCellVall(sheet, letter, num):
    return getMergedCellVal(sheet, sheet[f'{letter}{num}'])


def getDaySch(sheet, day_start, day_end, group):
    arr = []
    counter = 0
    for i in range(day_start, day_end):
        arr.append(getCellVall(sheet, group, i))

    for i in range(0, len(arr), 4):
        counter += 1
        arr.insert(i, f"\n<b>{counter} пара</b>")
    arr = [str(el) for el in arr if str(el) != "None"]
    string = "\n".join(str(e) for e in arr)

    return string




