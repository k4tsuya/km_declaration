"""Module for filtering data from bank transactions."""

import pandas as pd

from .app import bank_data, count_shop_visits, purchase_dates, shop_distance


def generate_declaration_data() -> pd.DataFrame:
    """Generate and print a report."""
    report_data = {}

    report_data["Visit count"] = count_shop_visits()
    report_data["Distance"] = shop_distance()
    report_data["Subtotal km"] = {
        shop: report_data["Visit count"][shop] * report_data["Distance"][shop]
        for shop in report_data["Visit count"]
    }

    return pd.DataFrame(report_data)


def filter_purchase_data(
    shop_name: str,
) -> pd.DataFrame:
    """Generate and print a purchase report for a specific shop."""
    report_data = purchase_dates(shop_name)

    return pd.DataFrame(report_data[shop_name])


def filter_dates(
    start_date: str,
    end_date: str | None,
) -> pd.DataFrame:
    """Filter bank data for a specific date."""
    end_date = end_date if end_date else start_date
    data = {"Filtered Purchases": []}

    for item in bank_data:
        date = item[4]
        counter_iban = item[8]
        counter_party = item[9]
        amount = item[6]
        description = item[19]
        if start_date <= date <= end_date:
            data["Filtered Purchases"].append(
                {
                    "Date": date,
                    "Counter Party": counter_party,
                    "Amount": amount,
                    "IBAN": counter_iban,
                    "Description": description,
                },
            )
    return pd.DataFrame(data["Filtered Purchases"])


def filter_bank_number(iban: str) -> pd.DataFrame:
    """Filter bank data for a specific IBAN number."""
    data = {iban: []}

    for item in bank_data:
        counter_party_iban = item[8]
        date = item[4]
        counter_party = item[9]
        amount = item[6]
        description = item[19]
        if iban in counter_party_iban:
            data[iban].append(
                {
                    "IBAN": counter_party_iban,
                    "Date": date,
                    "Counter Party": counter_party,
                    "Amount": amount,
                    "Description": description,
                },
            )

    return pd.DataFrame(data[iban])


def filter_name(name: str) -> pd.DataFrame:
    """Filter bank data for a specific name."""
    data = {name: []}

    for item in bank_data:
        counter_party_name = item[9]
        date = item[4]
        iban = item[8]
        amount = item[6]
        description = item[19]
        if name.lower() in counter_party_name.lower():
            data[name].append(
                {
                    "IBAN": iban,
                    "Name": counter_party_name,
                    "Date": date,
                    "Amount": amount,
                    "Description": description,
                },
            )
    return pd.DataFrame(data[name])
