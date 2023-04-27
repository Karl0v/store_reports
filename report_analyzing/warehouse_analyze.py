from report_processing import Report, SKU
from typing import List
from datetime import datetime, date
import csv


class WarehauseAnalyze(Report):

    def __init__(self, sku_rows: List[SKU]):
        super().__init__('', qty_column=6, name_of_column=['Warehouse ID','Qty SKU','Sale','Dispose',
                                                         'Max Cell_ID', 'First arrival'])
        self.sku_rows = sku_rows

    def read_report(self):
        pass
        self._analyze_warehouse()
        super().read_report()

    def _analyze_warehouse(self):
        sku_dict = dict()
        for row in self.sku_rows:
            if row.warehouse not in sku_dict:
                sku_dict[row.warehouse] = []
            sku_dict[row.warehouse].append(row)
        #print(sku_dict)
        for key, value in sku_dict.items():
            total_qty = 0
            total_sale = 0
            total_dispose = 0
            max_qty = 0
            first_arrival = None
            for row in value:
                if row.operation == 'sale':
                    total_sale += 1
                elif row.operation == 'dispose':
                    total_dispose += 1
                else:
                    total_qty += 1


            report_row = {
                'Warehouse ID': key,
                'Qty SKU': total_qty,
                'Sale': total_sale,
                'Dispose': total_dispose,
                'Max Cell_ID': "",
                'First arrival': first_arrival
            }
            self.rows.append(report_row)


"""  for key, value in sku_dict.items():
            total_qty = list()
            total_sale = list()
            total_dispose = list()
            first_arrival = None
            for row in value:                
                total_sale.append(len(row.operation['sale']))
                total_dispose.append(len(row.operation['dispose']))
                if not first_arrival:
                    first_arrival = row.operation['first_arrival'][0]
                else:
                    if row.operation['first_arrival'][0] < first_arrival:
                        first_arrival = row.operation['first_arrival'][0]
            report_row = {
                'Warehouse ID': key,
                'Qty SKU': total_qty,
                'Sale': total_sale,
                'Dispose': total_dispose,
                'First arrival': first_arrival
            }
            self.rows.append(report_row)"""

