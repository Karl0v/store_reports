from .report import Report
import datetime
import csv
from

class SKUReport(Report):

    def __init__(self, file_name: str):
        super().__init__(file_name, qty_column=10, name_of_column=['date','time','sku','warehouse','warehouse_cell_id','operation','invoice','expiration_date','operation_cost','comment'])

    def read_report(self):
        """
        Читает файл CRG report типа CSV
        на каждый ряд в отчете создает обьект типа SKU и хранит его
        задает поле width_of_column
        :return:
        """
        with open(self.file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                S(