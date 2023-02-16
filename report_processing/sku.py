import datetime


class SKU:

    def __init__(
            self,
            data: datetime.date,
            time: datetime.time,
            sku: str,
            warehouse: str,
            warehouse_cell_id: str,
            operation: str,
            invoice: str,
            expiration_date: datetime.date,
            operation_cost: float,
            comment: str,
            raw: dict
            ):
        self.data = data
        self.time = time
        self.sku = sku
        self.warehouse = warehouse
        self.warehouse_cell_id = warehouse_cell_id
        self.operation = operation
        self.invoice = invoice
        self.expiration_date = expiration_date
        self.operation_cost = operation_cost
        self.comment = comment
        self.raw = raw

