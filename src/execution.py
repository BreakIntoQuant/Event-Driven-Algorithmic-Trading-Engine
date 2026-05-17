from event import (
    FillEvent
)


class ExecutionHandler:

    def execute_order(
        self,
        order_event,
        market_price
    ):

        fill_event = FillEvent(
            order_event.timestamp,
            market_price,
            order_event.quantity
        )

        return fill_event