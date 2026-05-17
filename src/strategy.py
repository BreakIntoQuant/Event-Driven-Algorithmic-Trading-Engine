import pandas as pd

from event import (
    SignalEvent
)


class MovingAverageStrategy:

    def __init__(
        self,
        short_window=20,
        long_window=50
    ):

        self.short_window = (
            short_window
        )

        self.long_window = (
            long_window
        )

        self.prices = []

    def generate_signal(
        self,
        market_event
    ):

        self.prices.append(
            market_event.price
        )

        if (
            len(self.prices)
            < self.long_window
        ):

            return None

        prices_series = pd.Series(
            self.prices
        )

        short_ma = (
            prices_series
            .rolling(
                self.short_window
            )
            .mean()
            .iloc[-1]
        )

        long_ma = (
            prices_series
            .rolling(
                self.long_window
            )
            .mean()
            .iloc[-1]
        )

        if short_ma > long_ma:

            signal = "LONG"

        else:

            signal = "SHORT"

        return SignalEvent(
            market_event.timestamp,
            signal
        )