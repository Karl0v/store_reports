import datetime


class CRG:
    def __init__(
            self,
            data: datetime.date,
            time: datetime.time,
            invoice_number: str,
            weight: float,
            sender: str,
            recipient: str,
            cost_of_delivery: float,
            purchase_cost: float):
        self.data = data
        self.time = time
        self.invoice_number = invoice_number
        self.weight = weight
        self.sender = sender
        self.recipient = recipient
        self.cost_of_delivery = cost_of_delivery
        self.purchase_cost = purchase_cost