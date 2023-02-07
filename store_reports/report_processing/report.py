class Report:


    def __init__(self, file_name: str, qty_column: int, name_of_column: list):
        self.file_name = file_name
        self.qty_column = qty_column
        self.name_of_column = name_of_column
        self.width_of_column = list()

    def read_report(self):
        """
        Читает файл из self.file_name и задает поле width_of_column
        :return:
        """
        pass


