import matplotlib.pyplot as plt


def plot_equity_curve(
    portfolio_values
):

    plt.figure(figsize=(14, 7))

    plt.plot(portfolio_values)

    plt.title(
        'Portfolio Equity Curve'
    )

    plt.xlabel('Time')

    plt.ylabel('Portfolio Value')

    plt.grid(True)

    plt.savefig(
        'charts/equity_curve.png'
    )

    print(
        "Equity curve saved."
    )