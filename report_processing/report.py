class Report:

    def __init__(self, file_name: str, qty_column: int, name_of_column: list):
        self.file_name = file_name
        self.qty_column = qty_column
        self.name_of_column = name_of_column
        self.width_of_column = list()
        self.rows = list()

    def read_report(self):
        """
        задает поле width_of_column, rows заполняется в наследниках
        :return:
        """
        print('')
        for i in range(self.qty_column):
            name = self.name_of_column[i]
            list_of_column_values = list()
            list_of_column_values.append(self.name_of_column[i])
            for entry in self.rows:
                if isinstance(entry, dict):
                    list_of_column_values.append(entry[name])
                else:
                    list_of_column_values.append(entry.raw[name])
            self.width_of_column.append(len(max(list_of_column_values, key=len)))

    def convert_to_txt(self, txt_filename: str):
        """
        Создаем текстовый файл опираясь на значения self.rows,
        формат записи колонок определяется остальными атрибутами класса
        :param txt_filename: файл в который будем записывать данные
        :return:
        """
        header_columns = list()
        # Создает список header_columns, который будет содержать названия всех колонок таблицы, а также добавляет
        # пробелы для каждой колонки, чтобы каждая колонка была одинаковой ширины.
        for name, width in zip(self.name_of_column, self.width_of_column):
            header_columns.append(name + ((width - len(name)) * ' '))
        with open(txt_filename, 'w') as txt_file:  # Открывает новый текстовый файл для записи
            # Записывает заголовки колонок в первой строке файла, разделяя каждую колонку символом |:
            txt_file.write('|'.join(header_columns) + '\n')
            for entry in self.rows:
                row_columns = list()
                # Создает список, который будет содержать данные всех колонок таблицы, а также добавляет пробелы
                # для каждой колонки, чтобы каждая колонка была одинаковой ширины.
                for name, width in zip(self.name_of_column,self.width_of_column):
                    if isinstance(entry, dict):
                        col_value = entry[name]
                    else:
                        col_value = entry.raw[name]
                    row_columns.append(str(col_value) + ((width - len(str(col_value))) * ' '))
                    # при конвертации в sale_report выдавало ошибку так как переменная operation_cost есть float, обернул так str(col_value)
                txt_file.write(
                    '|'.join(row_columns) + '\n')  # Записывает данные колонок, разделяя каждую колонку символом |:
