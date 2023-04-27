from report_processing import CRGReport
from report_processing import SKUReport
from report_analyzing import expiaration_date_analyze
from report_analyzing import operations_analyze
from report_analyzing import sale_analyze, ExpirationReport, SaleReport, WarehauseAnalyze




if __name__ == '__main__':

    x = CRGReport('reports/source/CRG-2022-region-3.csv')
    print(x.read_report())
    x.convert_to_txt('reports/output/crg.txt')

    y = SKUReport('reports/source/SKU-2022-region-3.csv')
    print(y.read_report())
    y.convert_to_txt('reports/output/sku.txt')

    #print('expiration report')
    #expiaration_date_analyze(y.rows)
    #operations_analize(y.rows)
    #sale_analyze(y.rows)

    #q = ExpirationReport(y.rows)
    #print(q.read_report())
    #q.convert_to_txt('reports/output/expiration.txt')
    #w = SaleReport(y.rows)
    #print(w.read_report())
    #w.convert_to_txt('reports/output/sale.txt')
    s = WarehauseAnalyze(y.rows)
    print(s.read_report())
    s.convert_to_txt('reports/output/warehouse.txt')


