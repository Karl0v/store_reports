from report_processing import SKU
from typing import List
import csv

def sale_analyze(sku_rows: List[SKU]):
    # создаем пустой словарь, в котором будем хранить все операции для каждого SKU
    sku_dict = dict()
    for row in sku_rows:
        # если SKU не встречалось раньше, создаем новий список операций
        if row.sku not in sku_dict:
            sku_dict[row.sku] = []
        # добавляем в найденую операцию для соответствующего SKU в список
        sku_dict[row.sku].append(row)
    # создаем пустой список для отчета о продажах
    sale_report = []
    # для каждого SKU из словаря sku_dict и соответствующего ему списка операций ...
    for key, value in sku_dict.items():
        # ... получаем последнюю операция которая была sale
        last_operation = value[-1]
        if last_operation.operation == 'sale':
            #todo list comprehension позволяет сделать в одну строчку подсчет transportation_cost

            # Создаем список всех трат на транспортировку товара кроме первой и последней операции
            transportation_cost = [operation.operation_cost + 0 for operation in value[1:-1]]
            """transportation_cost = 0
            for operation in value[1:-1]:
                transportation_cost += operation.operation_cost
            print(transportation_cost))"""
            # добавляем информацию о продаже и затратах на транспортировку в отчет
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
            sale_report.append(report_row)
            #todo запись в csv
    # записывам всю полученую информацию в файл формата csv
    csv_file = 'report_analyzing/sale_analyze_report.csv'
    with open(csv_file, 'w', newline='') as csvfile:
        headers = ['SKU', 'Warehouse', 'Warehouse cell ID', 'Sale date', 'First arrival date', 'Operation_cost',
                   'Cost of transportation']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for row in sale_report:
            writer.writerow(row)