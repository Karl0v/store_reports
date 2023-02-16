class Report:


    def __init__(self, file_name: str, qty_column: int, name_of_column: list):
        self.file_name = file_name
        self.qty_column = qty_column
        self.name_of_column = name_of_column
        self.width_of_column = list()
        self.rows = list()

    def read_report(self):
        """
        Читает файл из self.file_name и задает поле width_of_column
        :return:
        """

        for i in range(self.qty_column):
            name = self.name_of_column[i]
            list_of_column_values = list()
            list_of_column_values.append(self.name_of_column[i])
            for entry in self.rows:
                list_of_column_values.append(entry.raw[name])
            self.width_of_column.append(len(max(list_of_column_values, key=len)))



    def convert_to_txt(self, txt_filename: str):
        """
        Создаем текстовый файл опираясь на значения self.rows,
        формат записи колонок определяется остальными атрибутами класса
        :param txt_filename: файл в который будем записывать данне
        :return:
        """
        with open(txt_filename, 'w') as txt_file:
            header_columns = list()
            for name, width in zip(self.name_of_column, self.width_of_column):
                header_columns.append(name + ((width - len(name))*' '))
            txt_file.write('|'.join(header_columns) + '\n')
            for entry in self.rows:
                row_columns = list()

                for name, width in zip(self.name_of_column, self.width_of_column):
                    col_value = entry.raw[name]
                    row_columns.append(str(col_value) + ((width - len(col_value))*' '))
                txt_file.write('|'.join(row_columns) + '\n')








