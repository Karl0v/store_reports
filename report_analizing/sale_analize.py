from report_processing import SKU
from typing import List


def sale_analize(sku_rows: List[SKU]):
    sku_dict = dict()
    for row in sku_rows:
        if row.sku not in sku_dict:
            sku_dict[row.sku] = []
        sku_dict[row.sku].append(row)

    sale_report = []
    for key, value in sku_dict.items():
        last_operation = value[-1]
        if last_operation.operation == 'sale':
            transportation_cost = 0
            #todo list comprehension позволяет сделать в одну строчку подсчет transportation_cost
            for operation in value[1:-1]:
                transportation_cost += operation.operation_cost
            first_operation = value[0]
            report_row = {
                'SKU': first_operation.sku,
                'Warehouse': last_operation.warehouse,
                'Warehouse cell ID': last_operation.warehouse_cell_id,
                'Sale date': last_operation.data.strftime('%d-%b-%Y'),
                'First arrival date': first_operation.data.strftime('%d-%b-%Y'),
                'Operation_cost': last_operation.operation_cost,
                'Cost of transportation': transportation_cost
            }

            #todo запись в csv
