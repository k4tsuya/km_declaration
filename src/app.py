"""Main application logic for KM declaration."""

import csv

bank_data = []

# NOTE: The path is based on the CWD's execution path from main.py.
# Rabobank uses Windows-1252 encoding.
try:
    with open("./bank_data.csv", encoding="windows-1252") as f:
        data = csv.reader(f)
        bank_data: list[list[str]] = list(data)
except FileNotFoundError:
    print("Please ensure 'bank_data.csv' is in the project root directory.")


class ShopTerminal:
    """Shop terminal names."""

    hanos: str = "Hanos Heerlen"
    sligro: str = "Sligro ZB 5032"
    makro: str = "Makro Nuth"
    horeca_plus: str = "Horeca-Plus Nuth"
    eldee: str = "BCK*Eldee Pak Pak"


def count_shop_visits() -> dict[str, int]:
    """Count visits to each shop in the shop list."""
    store_count: dict[str, int] = {
        "Hanos": 0,
        "Sligro": 0,
        "Makro": 0,
        "Horeca-Plus": 0,
        "Eldee": 0,
    }

    for item in bank_data:
        terminal_name = item[9]

        if terminal_name == ShopTerminal.hanos:
            store_count["Hanos"] += 1
        elif terminal_name == ShopTerminal.sligro:
            store_count["Sligro"] += 1
        elif terminal_name == ShopTerminal.makro:
            store_count["Makro"] += 1
        elif terminal_name == ShopTerminal.horeca_plus:
            store_count["Horeca-Plus"] += 1
        elif terminal_name == ShopTerminal.eldee:
            store_count["Eldee"] += 1

    return store_count


class ShopDistance:
    """Shop location distances."""

    hanos = 6.0
    sligro = 4.8
    makro = 9.5
    horeca_plus = 11.8
    eldee = 4.3


def shop_distance() -> dict[str, float]:
    """Calculate the roundtrip distance to each shop."""
    roundtrip = 2  # roundtrip multiplier - 2 for round trip and 1 for one way.

    distance: dict[str, float] = {
        "Hanos": round(ShopDistance.hanos * roundtrip),
        "Sligro": round(ShopDistance.sligro * roundtrip),
        "Makro": round(ShopDistance.makro * roundtrip),
        "Horeca-Plus": round(ShopDistance.horeca_plus * roundtrip),
        "Eldee": round(ShopDistance.eldee * roundtrip),
    }

    return distance


valid_names: dict[str, str] = {
    "Hanos": ShopTerminal.hanos,
    "Sligro": ShopTerminal.sligro,
    "Makro": ShopTerminal.makro,
    "Horeca-Plus": ShopTerminal.horeca_plus,
    "Eldee": ShopTerminal.eldee,
}


def purchase_dates(shop_name: str) -> dict[str, list[dict[str, str]]]:
    """
    Get a list of purchase dates and transaction IDs for a given shop.

    Args:
        shop_name (str): The name of the shop.

    """
    shop_name = shop_name.title()

    details: dict[str, list[dict[str, str]]] = {shop_name: []}

    if shop_name not in valid_names:
        msg = f"Shop '{shop_name}' is not recognized."
        raise ValueError(msg)

    for item in bank_data:
        date = item[4]
        terminal_name = item[9]
        transaction_id = item[15]

        if terminal_name in (
            ShopTerminal.hanos,
            ShopTerminal.sligro,
            ShopTerminal.makro,
            ShopTerminal.horeca_plus,
            ShopTerminal.eldee,
        ):
            details[shop_name].append(
                {"date": date, "transaction_id": transaction_id},
            )

    return details
