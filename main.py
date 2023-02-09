from report_processing import CRGReport
from report_processing import SKUReport

if __name__ == '__main__':

    y = SKUReport('reports/source/SKU-2022-region-3.csv')
    y.read_report()

"""x = CRGReport('reports/source/CRG-2022-region-3.csv')
    print(x.read_report())"""


