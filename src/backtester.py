from event import (
    OrderEvent
)


class Backtester:

    def __init__(
        self,
        data_handler,
        strategy,
        portfolio,
        execution_handler,
        risk_manager
    ):

        self.data_handler = (
            data_handler
        )

        self.strategy = strategy

        self.portfolio = (
            portfolio
        )

        self.execution_handler = (
            execution_handler
        )

        self.risk_manager = (
            risk_manager
        )

    def run(self):

        events = (
            self.data_handler
            .stream_next()
        )

        for market_event in events:

            signal = (
                self.strategy
                .generate_signal(
                    market_event
                )
            )

            if signal:

                quantity = (
                    self.risk_manager
                    .size_order(
                        signal
                    )
                )

                order = OrderEvent(
                    signal.timestamp,
                    signal.signal,
                    quantity
                )

                fill = (
                    self.execution_handler
                    .execute_order(
                        order,
                        market_event.price
                    )
                )

                self.portfolio.update_fill(
                    fill
                )

            self.portfolio.update_market_value(
                market_event.price
            )

        return (
            self.portfolio
            .portfolio_values
        )