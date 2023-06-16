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
        warehouse_id_dict = dict()
        for row in self.sku_rows:
            if row.warehouse not in warehouse_id_dict:
                warehouse_id_dict[row.warehouse] = []
            warehouse_id_dict[row.warehouse].append(row)
        #print(warehouse_id_dict)
        for key, value in warehouse_id_dict.items():
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
            for row in value:
                if row.operation == 'first_arrival':
                    if first_arrival is None or row.data < first_arrival:
                        first_arrival = row.data
            report_row = {
                'Warehouse ID': key,
                'Qty SKU': total_qty,
                'Sale': total_sale,
                'Dispose': total_dispose,
                'Max Cell_ID': self._max_cell_id(value),
                'First arrival': first_arrival
            }
            self.rows.append(report_row)

    def _max_cell_id(self, warehouse_rows: List[SKU]):
        current_load = 0
        max_load = 0
        for row in warehouse_rows:
            if row.operation == 'first_arrival' or row.operation == 'move':
                current_load += 1
                if current_load > max_load:
                    max_load = current_load
            elif row.operation == 'sale' or row.operation == 'dispose':
                current_load -= 1
        return max_load













