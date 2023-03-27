from report_processing import SKU
from typing import List
from datetime import datetime, timedelta


def operations_analyze(sku_rows: List[SKU]):
    operations = ['sale', 'first_arrival', 'dispose', 'move']
    days = [1, 3, 6, 12]
    today = datetime.today().date()

    x = input(f'\nWhat operation you want to check: {operations}\nYour choice -> ').lower()
    while x not in operations:
        print(f'Invalid input. Please choose from {operations}')
        x = input(f'Your choice -> ').lower()

    y = input(f'What period do you interested {days}months \nYour choice -> ')
    while y.isnumeric() not in days and y.isalpha():
        print(f'Invalid input. Please choose from {days}months')
        y = input(f'Your choice -> ')

    months = timedelta(days=int(y) * 30)
    period = today - months

    if not sku_rows:
        print('No data to analyze.')
    else:
        for row in sku_rows:
            if x == row.operation and today > row.data > period:
                print(f'{row.data} - {row.sku} - {row.operation} - {row.warehouse_cell_id} - {row.warehouse}')

"""def operations_analize(sku_rows: List[SKU]):
    operation_name = list()
    for row in sku_rows:
        operation_name.append(row.operation)
    x = input(f'What operation you want to check {set(operation_name)} \n -> ').lower()
    for row in sku_rows:
        if x.lower() in row.operation:
            print(f'{row.data} - {row.sku} - {row.operation}')
"""

