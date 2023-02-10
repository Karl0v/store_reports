from report_processing import CRGReport
from report_processing import SKUReport

if __name__ == '__main__':

    x = CRGReport('reports/source/CRG-2022-region-3.csv')
    print(len(x.read_report()))

    y = SKUReport('reports/source/SKU-2022-region-3.csv')
    print(len(y.read_report()))



