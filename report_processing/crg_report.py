from .report import Report
import datetime
import csv
from .crg import CRG

class CRGReport(Report):

    def __init__(self, file_name: str):
        super().__init__(file_name, qty_column=8, name_of_column=['date','time','invoice','weight','from','warehouse','delivery_cost','purchase_cost'])

    def read_report(self):
        """
        Читает файл CRG report типа CSV
        на каждый ряд в отчете создает обьект типа CRG и хранит его
        задает поле width_of_column
        :return:
        """
        crgs = []
        with open(self.file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                self.rows.append(CRG(
                    data=datetime.datetime.strptime(row['date'], '%d-%b-%Y').date(),
                    time=datetime.datetime.strptime(row['time'], '%H:%M:%S').time(),
                    invoice_number=str(row['invoice']),
                    weight=float(row['weight']),
                    sender=str(row['from']),
                    recipient=str(row['warehouse']),
                    cost_of_delivery=float(row['delivery_cost']),
                    purchase_cost=float(row['purchase_cost'])
                    ))

        return self.rows

"""{'date': '16-Dec-2022', 'time': '18:07:21', 'invoice': '14291824', 'weight': '43.4', 'from': 'City D', 'warehouse': 'A39', 'delivery_cost': '49.23', 'purchase_cost': '27788.36'}"""


