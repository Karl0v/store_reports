class Report:

    def __init__(self, file_name: str, qty_column: int, name_of_column: list):
        self.file_name = file_name
        self.qty_column = qty_column
        self.name_of_column = name_of_column
        self.width_of_column = list()
        self.rows = list()

def read_report(self):
    for i in range(self.qty_column):
        name = self.name_of_column[i]
        list_of_column_values = list()
        list_of_column_values.append(self.name_of_column[i])
        for entry in self.rows:
            if isinstance(entry, dict):
                list_of_column_values.append(str(entry[name]))
            else:
                list_of_column_values.append(entry.raw[name])
        self.width_of_column.append(len(max(list_of_column_values, key=len)))

def convert_to_txt(self, txt_filename: str):
    header_columns = list()
    for name, width in zip(self.name_of_column, self.width_of_column):
        header_columns.append(name + ((width - len(name)) * ' '))
    with open(txt_filename, 'w') as txt_file:
        txt_file.write('|'.join(header_columns) + '\n')
        for entry in self.rows:
            row_columns = list()
            for name, width in zip(self.name_of_column,self.width_of_column):
                if isinstance(entry, dict):
                    col_value = entry[name]
                else:
                    col_value = entry.raw[name]
                row_columns.append(str(col_value) + ((width - len(str(col_value))) * ' '))
            txt_file.write('|'.join(row_columns) + '\n')


from .report import Report
import datetime
import csv
from .sku import SKU

class SKUReport(Report):

def __init__(self, file_name: str):
    super().__init__(file_name, qty_column=10, name_of_column=['date','time','sku','warehouse','warehouse_cell_id','operation','invoice','expiration_date','operation_cost','comment'])

    def read_report(self):
        with open(self.file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                self.rows.append(SKU(
                    data=datetime.datetime.strptime(row['date'], '%d-%b-%Y').date(),
                    time=datetime.datetime.strptime(row['time'], '%H:%M:%S').time(),
                    sku=str(row['sku']),
                    warehouse=str(row['warehouse']),
                    warehouse_cell_id=str(row['warehouse_cell_id']),
                    operation=str(row['operation']),
                    invoice=str(row['invoice']),
                    expiration_date=datetime.datetime.strptime(row['expiration_date'], '%d-%b-%Y').date(),
                    operation_cost=float(row['operation_cost']),
                    comment=str(row['comment']),
                    raw=row
                ))
        super().read_report()
        return self.rows

import datetime

class SKU:

    def __init__(
            self,
            data: datetime.date,
            time: datetime.time,
            sku: str,
            warehouse: str,
            warehouse_cell_id: str,
            operation: str,
            invoice: str,
            expiration_date: datetime.date,
            operation_cost: float,
            comment: str,
            raw: dict
            ):
        self.data = data
        self.time = time
        self.sku = sku
        self.warehouse = warehouse
        self.warehouse_cell_id = warehouse_cell_id
        self.operation = operation
        self.invoice = invoice
        self.expiration_date = expiration_date
        self.operation_cost = operation_cost
        self.comment = comment
        self.raw = raw

from report_processing import Report, SKU
from typing import List

class SaleReport(Report):

    def __init__(self, sku_rows: List[SKU]):
        super().__init__('', qty_column=7, name_of_column=['SKU', 'Warehouse', 'Warehouse cell ID', 'Sale date',
                                                           'First arrival date', 'Operation_cost', 'Cost of transportation'])
        self.sku_rows = sku_rows

    def read_report(self):
        self._analyze_sale()
        super().read_report()

    def _analyze_sale(self):
        sku_dict = dict()
        for row in self.sku_rows:
            if row.sku not in sku_dict:
                sku_dict[row.sku] = []
            sku_dict[row.sku].append(row)
        for key, value in sku_dict.items():
            last_operation = value[-1]
            if last_operation.operation == 'sale':
                transportation_cost = round(sum([operation.operation_cost + 0 for operation in value[1:-1]]),2)
                first_operation = value[0]
                report_row = {
                    'SKU': first_operation.sku,
                    'Warehouse': last_operation.warehouse,
                    'Warehouse cell ID': last_operation.warehouse_cell_id,
                    'Sale date': last_operation.data.strftime('%d-%b-%Y'),
                    'First arrival date': first_operation.data.strftime('%d-%b-%Y'),
                    'Operation_cost': last_operation.operation_cost,
                    'Cost of transportation': f'{transportation_cost:.2f}',
                    'sale_date_for_sort': last_operation.data
                }
                self.rows.append(report_row)
        self.rows.sort(key=lambda x: x['sale_date_for_sort'])
