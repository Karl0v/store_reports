from report_processing import CRGReport
from report_processing import SKUReport
from report_analizing import expiaration_date_analize
from report_analizing import operations_analize




if __name__ == '__main__':

    x = CRGReport('reports/source/CRG-2022-region-3.csv')
    print(x.read_report())
    x.convert_to_txt('reports/output/crg.txt')

    y = SKUReport('reports/source/SKU-2022-region-3.csv')
    print(y.read_report())
    y.convert_to_txt('reports/output/sku.txt')

    expiaration_date_analize(y.rows)
    operations_analize(y.rows)





