from report_processing import SKU
from typing import List


def operations_analize(sku_rows: List[SKU]):
    operation_name = list()
    for row in sku_rows:
        operation_name.append(row.operation)
    x = input(f'What operation you want to check {set(operation_name)} \n -> ').lower()
    for row in sku_rows:
        if x.lower() in row.operation:
            print(f'{row.data} - {row.sku} - {row.operation}')

