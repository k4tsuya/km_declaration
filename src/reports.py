"""Module for generating reports."""

import pandas as pd

from .app import count_shop_visits, shop_distance


def generate_report() -> str:
    """Generate and print a report."""
    report_data = {}

    report_data["Visit count"] = count_shop_visits()
    report_data["Distance"] = shop_distance()
    report_data["Subtotal km"] = {
        shop: report_data["Visit count"][shop] * report_data["Distance"][shop]
        for shop in report_data["Visit count"]
    }

    df = pd.DataFrame(report_data)

    total = {
        "Subtotal km": sum(report_data["Subtotal km"].values()),
    }

    data = ""

    with open("report.txt", "w") as f:
        data += "KM Declaration Report\n"
        data += "_" * 50 + "\n"
        data += f"{df.to_string(justify='right')}\n"
        data += "_" * 50 + "\n"
        data += f"Total KM: {total['Subtotal km']} KM\n"
        f.write("KM Declaration Report\n")
        f.write("_" * 50 + "\n")
        f.write(f"{df.to_string(justify='right')}\n")
        f.write("_" * 50 + "\n\n")
        f.write(f"Total KM: {total['Subtotal km']} KM\n")

    return data
