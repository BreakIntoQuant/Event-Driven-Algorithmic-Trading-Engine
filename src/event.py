class Event:
    pass


class MarketEvent(Event):

    def __init__(
        self,
        timestamp,
        price
    ):

        self.type = "MARKET"
        self.timestamp = timestamp
        self.price = price


class SignalEvent(Event):

    def __init__(
        self,
        timestamp,
        signal
    ):

        self.type = "SIGNAL"
        self.timestamp = timestamp
        self.signal = signal


class OrderEvent(Event):

    def __init__(
        self,
        timestamp,
        order_type,
        quantity
    ):

        self.type = "ORDER"
        self.timestamp = timestamp
        self.order_type = order_type
        self.quantity = quantity


class FillEvent(Event):

    def __init__(
        self,
        timestamp,
        fill_price,
        quantity
    ):

        self.type = "FILL"
        self.timestamp = timestamp
        self.fill_price = fill_price
        self.quantity = quantity