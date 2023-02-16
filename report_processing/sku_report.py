from .report import Report
import datetime
import csv
from .sku import SKU


class SKUReport(Report):

    def __init__(self, file_name: str):
        super().__init__(file_name, qty_column=10, name_of_column=['date','time','sku','warehouse','warehouse_cell_id','operation','invoice','expiration_date','operation_cost','comment'])

    def read_report(self):
        """
        Читает файл SKU report типа CSV
        на каждый ряд в отчете создает обьект типа SKU и хранит его
        задает поле width_of_column
        :return:
        """

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
        # вызываем с родительского класса метод read_report
        super().read_report()
        return self.rows