from report_processing import Report, SKU, CRG
from typing import List
from datetime import datetime, date
import csv


class InvoiceAnalyze(Report):

    def __init__(self, sku_rows: List[SKU], crg_rows: List[CRG]):
        super().__init__('', qty_column=7, name_of_column=['invoice','date','SKU count','SKU Sale','SKU Dispose',
                                                         'Total delivery cost', 'Saldo'])
        self.sku_rows = sku_rows
        self.crg_rows = crg_rows


    def read_report(self):
        self._analyze_invoice()
        super().read_report()

    def _analyze_invoice(self):
        invoice_dict = dict()
        delivery_cost_dict = dict()
        for row in self.crg_rows:
            if row.purchase_cost > 0:
                invoice_dict[row.invoice_number] = {
                    'Invoice_info': row,
                    'SKU_info': dict()
                }

        sku_to_invoice = dict()
        for row in self.sku_rows:
            # Фиксируем событие 'first_arrival'
            if row.operation == 'first_arrival':
                # запоминаем в каком инвойесе этот SKU - 'first_arrival'
                sku_to_invoice[row.sku] = row.invoice
                # по инвойсу создаем список для хранения историй движений по этому SKU
                invoice_dict[row.invoice]['SKU_info'][row.sku] = [row]
            # отбираем корректные SKU
            elif row.sku in sku_to_invoice:
                # вспоминаем в каком инвойесе этот SKU - 'first_arrival'
                invoice = sku_to_invoice[row.sku]
                # по инвойсу наполняем список для хранения историй движений по этому SKU
                invoice_dict[invoice]['SKU_info'][row.sku].append(row)
            # отрезаем ошибки в данных
            else:
                print(f'{row.sku} такой SKU без события "firs_arrival"')

        for key, value in invoice_dict.items():
            if key == '73403713':
                print('')
            total_delivery_cost = value['Invoice_info'].cost_of_delivery
            sku_count = len(value['SKU_info'])
            sku_sale = 0
            sku_dispose = 0
            saldo = -value['Invoice_info'].cost_of_delivery - value['Invoice_info'].purchase_cost
            for sku, sku_info in value['SKU_info'].items():
                for x in sku_info:
                    if x.operation == 'sale':
                        sku_sale += 1
                        saldo += x.operation_cost
                    elif x.operation == 'dispose':
                        sku_dispose += 1
                        saldo += x.operation_cost
                    elif x.operation == 'move':
                        total_delivery_cost += abs(x.operation_cost)
                        saldo += x.operation_cost
            # 'Total delivery cost' = crg.cost_of_delivery + sum(sku['move_operation].operation_cost)
            report_row = {
                'invoice': key,
                'date': value['Invoice_info'].data,
                'SKU count': sku_count,   #ДЗ
                'SKU Sale': sku_sale,    #ДЗ
                'SKU Dispose': sku_dispose, #ДЗ
                'Total delivery cost': round(total_delivery_cost, 2), #round(total_delivery_cost/len_delivery_cost, 2)
                'Saldo': round(saldo, 2)
            }
            self.rows.append(report_row)

        sum_sku_count = list()
        sum_sku_sale = list()
        sum_sku_dispose = list()
        sum_total_delivery_cost = list()
        sum_saldo = list()

        for row in self.rows:
            sum_sku_count.append(row['SKU count'])
            sum_sku_sale.append(row['SKU Sale'])
            sum_sku_dispose.append(row['SKU Dispose'])
            sum_total_delivery_cost.append(row['Total delivery cost'])
            sum_saldo.append(row['Saldo'])

        report_row = {
            'invoice': 'Total',
            'date': datetime.today().date(),
            'SKU count': sum(sum_sku_count),  # ДЗ
            'SKU Sale': sum(sum_sku_sale),  # ДЗ
            'SKU Dispose': sum(sum_sku_dispose),  # ДЗ
            'Total delivery cost': sum(sum_total_delivery_cost),  # round(total_delivery_cost/len_delivery_cost, 2)
            'Saldo': round(sum(sum_saldo), 2)
        }
        self.rows.append(report_row)

