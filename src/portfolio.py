class Portfolio:

    def __init__(
        self,
        initial_capital=100000
    ):

        self.cash = (
            initial_capital
        )

        self.position = 0

        self.portfolio_values = []

    def update_fill(
        self,
        fill_event
    ):

        cost = (
            fill_event.fill_price
            * fill_event.quantity
        )

        self.cash -= cost

        self.position += (
            fill_event.quantity
        )

    def update_market_value(
        self,
        current_price
    ):

        total_value = (
            self.cash
            + self.position
            * current_price
        )

        self.portfolio_values.append(
            total_value
        )

        return total_value