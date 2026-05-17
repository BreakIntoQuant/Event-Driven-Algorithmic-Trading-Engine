class RiskManager:

    def __init__(
        self,
        max_position_size=100
    ):

        self.max_position_size = (
            max_position_size
        )

    def size_order(
        self,
        signal
    ):

        if signal.signal == "LONG":

            quantity = (
                self.max_position_size
            )

        else:

            quantity = (
                -self.max_position_size
            )

        return quantity