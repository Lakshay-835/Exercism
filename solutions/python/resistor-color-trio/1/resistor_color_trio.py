COLORS = (
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
)

METRIC_UNITS = (
    (1_000_000_000, "gigaohms"),
    (1_000_000, "megaohms"),
    (1_000, "kiloohms"),
)


def label(colors: list[str]) -> str:
    first, second, multiplier, *_ = colors
    resistance = (COLORS.index(first) * 10 + COLORS.index(second)) * (
        10 ** COLORS.index(multiplier)
    )

    for factor, unit in METRIC_UNITS:
        if resistance >= factor and resistance % factor == 0:
            return f"{resistance // factor} {unit}"

    return f"{resistance} ohms"