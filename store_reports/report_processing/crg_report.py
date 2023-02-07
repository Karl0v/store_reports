from report import Report

class CRGReport(Report):

    def __init__(self, file_name: str):
        super().__init__(file_name, qty_column=8, name_of_column=['date','time','invoice','weight','from','warehouse','delivery_cost','purchase_cost'
])