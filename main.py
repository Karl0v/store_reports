from report_processing import CRGReport

if __name__ == '__main__':

    x = CRGReport('reports/source/CRG-2022-region-3.csv')
    x.read_report()
