from datetime import datetime, timedelta
from report_processing import SKU
from typing import List
import csv


def expiaration_date_analize(sku_rows: List[SKU]):
    # получаем текущую дату
    start_date = datetime.today().date()

    # задаем период предупреждения в 14 дней
    warning_period = timedelta(days=14)

    # вычисляем дату, когда должно быть предупреждение
    end_date = start_date + warning_period

    # создаем словарь, где ключом является SKU, а значением - список операций по этому SKU
    sku_dict = dict()
    for row in sku_rows:
        # Если срок годности находится между текущей датой и датой предупреждения,
        # добавляем строку в список операций по SKU в словаре sku_dict
        if start_date < row.expiration_date < end_date:
            if row.sku not in sku_dict:
                sku_dict[row.sku] = []
            sku_dict[row.sku].append(row)

    # создаем список для хранения результатов
    expiration_report = []

    # для каждого SKU из sku_dict получаем последнюю операцию и первую операцию по нему
    for key, value in sku_dict.items():
        last_operation = value[-1]

        # если последняя операция - move или first_arrival,
        # то добавляем информацию в expiration_report
        if last_operation.operation == 'move' or last_operation == 'first_arrival':
            first_operation = value[0]
            report_row = {
                'Expiration date': first_operation.expiration_date.strftime('%d-%b-%Y'),
                'SKU': first_operation.sku,
                'Warehouse': last_operation.warehouse,
                'Warehouse cell ID': last_operation.warehouse_cell_id,
                'Last operation date': last_operation.data.strftime('%d-%b-%Y'),
                'First arrival date': first_operation.data.strftime('%d-%b-%Y')
            }
            expiration_report.append(report_row)
    # записываем данные в CSV-файл
    csv_file = 'report_analizing/expiration_report.csv'
    with open(csv_file, 'w', newline='') as csvfile:
        headers = ['Expiration date', 'SKU', 'Warehouse', 'Warehouse cell ID', 'Last operation date', 'First arrival date']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for row in expiration_report:
            writer.writerow(row)






