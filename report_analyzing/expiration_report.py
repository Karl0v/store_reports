from report_processing import Report, SKU
from datetime import datetime, timedelta, date
from typing import List
import csv

class ExpirationReport(Report):


    def __init__(self, sku_rows: List[SKU], star_date: date = datetime.today().date(), warning_period_days: int = 14):
        super().__init__('', qty_column=6, name_of_column=['Expiration date', 'SKU', 'Warehouse', 'Warehouse cell ID',
                                                           'Last operation date', 'First arrival date'])
        self.sku_rows = sku_rows
        #fixme вернуть присвоение входного параметра на start_date
        self.start_date = date(2023, 3, 26)
        self.end_date = self.start_date + timedelta(days=warning_period_days)

    def read_report(self):
        self._analyze_data()
        super().read_report()


    def _analyze_data(self):
        # создаем словарь, где ключом является SKU, а значением - список операций по этому SKU
        sku_dict = dict()
        for row in self.sku_rows:
            # Если срок годности находится между текущей датой и датой предупреждения,
            # добавляем строку в список операций по SKU в словаре sku_dict
            if self.start_date < row.expiration_date < self.end_date:
                if row.sku not in sku_dict:
                    sku_dict[row.sku] = []
                sku_dict[row.sku].append(row)

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
                self.rows.append(report_row)

    def write_to_csv(self):
        csv_file = 'report_analyzing/expiration_report.csv'
        with open(csv_file, 'w', newline='') as csvfile:
            headers = ['Expiration date', 'SKU', 'Warehouse', 'Warehouse cell ID', 'Last operation date',
                       'First arrival date']
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for row in self.rows:
                writer.writerow(row)