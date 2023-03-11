from datetime import datetime, timedelta
from report_processing import Report, SKUReport, SKU
from typing import List


def expiaration_date_analize(sku_rows: List[SKU]):
    start_date = datetime.today().date() # указываем переменную - сегодняшняя дата
    warning_period = timedelta(days=14) # указываем переменную - 14 дней
    end_date = start_date + warning_period # указываем переменную - сегодняшняя дата + 14 дней
    expiring_sku_info = [] # указываем список
    sku_set = set()
    # print(today)
    # print(sku_rows[1].expiration_date, len(sku_rows))
    # print(type(today))
    for row in sku_rows:
        # print(type(row.expiration_date))
        # условие если дата сегодня меньше даты в файле, но не больше даты сегодня + 14дней
        if start_date < row.expiration_date < end_date and row.sku not in sku_set:
            sku_set.add(row.sku)
            expiring_sku_info.append(row)
        else:
            pass
            # print(f'{row.expiration_date} {row.sku} Срок не важно')
    expiring_sku_info.sort(key=lambda x: x.expiration_date)
    for row in expiring_sku_info:
        print(f'{row.expiration_date} {row.sku} Срок годности скоро истекает')
