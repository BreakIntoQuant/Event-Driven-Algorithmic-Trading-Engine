import yfinance as yf

from event import (
    MarketEvent
)


class DataHandler:

    def __init__(
        self,
        ticker,
        start_date,
        end_date
    ):

        self.data = yf.download(
            ticker,
            start=start_date,
            end=end_date
        )['Close']

        self.data = self.data.squeeze()

        self.events = []

    def stream_next(self):

        for timestamp, price in self.data.items():

            market_event = (
                MarketEvent(
                    timestamp,
                    float(price)
                )
            )

            self.events.append(
                market_event
            )

        return self.events