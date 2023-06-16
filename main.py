from report_processing import CRGReport
from report_processing import SKUReport
#from report_analyzing import expiaration_date_analyze
#from report_analyzing import operations_analyze
from report_analyzing import ExpirationReport, SaleReport, WarehauseAnalyze, InvoiceAnalyze
from cli_arguments import cli_arguments_parser
import os


if __name__ == '__main__':
    cli_args = cli_arguments_parser.parse_args()
    os.makedirs(cli_args.output_folder, exist_ok=True) # создаем папки для записи
    crg_report = CRGReport(os.path.join(cli_args.source_folder, 'crg.csv')) #'reports/source/CRG-2022-region-3.csv'
    crg_report.read_report()
    crg_report.convert_to_txt(os.path.join(cli_args.output_folder, 'crg.txt')) #'reports/output/txt/crg.txt'


    sku_report = SKUReport(os.path.join(cli_args.source_folder, 'sku.csv')) #'reports/source/SKU-2022-region-3.csv'
    sku_report.read_report()
    sku_report.convert_to_txt(os.path.join(cli_args.output_folder, 'sku.txt')) #'reports/output/txt/sku.txt'

    #print('expiration report')
    #expiaration_date_analyze(y.rows)
    #operations_analize(y.rows)
    #sale_analyze(y.rows)

    print('Building expiration report')

    expiration_report = ExpirationReport(sku_report.rows, start_date=cli_args.exp_start_date, warning_period_days=cli_args.exp_warning_days)
    expiration_report.read_report()
    expiration_report.convert_to_txt(os.path.join(cli_args.output_folder, 'expiration.txt'))
    sale_report = SaleReport(sku_report.rows)
    sale_report.read_report()
    sale_report.convert_to_txt(os.path.join(cli_args.output_folder, 'sale.txt'))
    warehouse_report = WarehauseAnalyze(sku_report.rows)
    warehouse_report.read_report()
    warehouse_report.convert_to_txt(os.path.join(cli_args.output_folder, 'warehouse.txt'))

    invoice_report = InvoiceAnalyze(sku_report.rows, crg_report.rows)
    invoice_report.read_report()
    invoice_report.convert_to_txt(os.path.join(cli_args.output_folder, 'invoice.txt'))


