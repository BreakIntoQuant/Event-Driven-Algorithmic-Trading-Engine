from data_handler import (
    DataHandler
)

from strategy import (
    MovingAverageStrategy
)

from portfolio import (
    Portfolio
)

from execution import (
    ExecutionHandler
)

from risk_manager import (
    RiskManager
)

from backtester import (
    Backtester
)

from performance import (
    calculate_sharpe_ratio,
    calculate_max_drawdown
)

from visualization import (
    plot_equity_curve
)


def main():

    print(
        "\nInitializing trading engine..."
    )

    data_handler = DataHandler(
        "AAPL",
        "2020-01-01",
        "2025-01-01"
    )

    strategy = (
        MovingAverageStrategy()
    )

    portfolio = Portfolio()

    execution_handler = (
        ExecutionHandler()
    )

    risk_manager = (
        RiskManager()
    )

    backtester = Backtester(
        data_handler,
        strategy,
        portfolio,
        execution_handler,
        risk_manager
    )

    print(
        "Running event-driven backtest..."
    )

    portfolio_values = (
        backtester.run()
    )

    sharpe_ratio = (
        calculate_sharpe_ratio(
            portfolio_values
        )
    )

    max_drawdown = (
        calculate_max_drawdown(
            portfolio_values
        )
    )

    print("\n==========")
    print("PERFORMANCE METRICS")
    print("==========")

    print(
        f"\nSharpe Ratio: {sharpe_ratio:.2f}"
    )

    print(
        f"Max Drawdown: {max_drawdown:.2%}"
    )

    print(
        "\nGenerating visualizations..."
    )

    plot_equity_curve(
        portfolio_values
    )

    print(
        "\nEvent-Driven Trading Analysis Complete."
    )


if __name__ == "__main__":
    main()