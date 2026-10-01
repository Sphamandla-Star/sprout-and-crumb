# summarise_orders.py
#
# Reads preorders.csv and prints two summaries:
#   1. Total quantity ordered for each menu item
#   2. Number of orders for each pickup date
#
# No third-party libraries needed — only Python's built-in "csv" module.
# Run it from the terminal with:
#   python summarise_orders.py

import csv  # Built-in module for reading and writing CSV files

# ── Step 1: Set up empty dictionaries to hold our totals ──────────────────────
#
# A dictionary stores pairs of: key → value
# We'll use two:
#   item_totals    maps  item name  →  total quantity ordered
#   date_counts    maps  pickup date → number of orders on that date

item_totals = {}  # e.g. {"Seeded Sourdough": 7, "Almond Croissant": 13, ...}
date_counts = {}  # e.g. {"2025-07-22": 3, "2025-07-23": 3, ...}


# ── Step 2: Open the CSV file and read it row by row ──────────────────────────
#
# "with open(...)" automatically closes the file when we're done —
# you don't need to remember to close it yourself.
#
# csv.DictReader reads each row as a dictionary, so we can access
# values by column name instead of by position number.
# e.g. row["name"], row["item"], row["quantity"], row["pickup_date"]

with open("preorders.csv", newline="", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        # Pull the values we need from this row
        item     = row["item"]
        quantity = int(row["quantity"])  # Convert from text to a whole number
        date     = row["pickup_date"]

        # ── Tally quantities per item ─────────────────────────────────────
        # If this item has been seen before, add to its running total.
        # If it's the first time we've seen it, start the total at 0 then add.
        if item in item_totals:
            item_totals[item] += quantity
        else:
            item_totals[item] = quantity

        # ── Count orders per pickup date ──────────────────────────────────
        # Each row is one order, so we add 1 for every row we read.
        if date in date_counts:
            date_counts[date] += 1
        else:
            date_counts[date] = 1


# ── Step 3: Print the results ─────────────────────────────────────────────────
#
# sorted(...) returns items in alphabetical / numerical order.
# .items() gives us each key-value pair as a tuple, e.g. ("Almond Croissant", 13)
# so we unpack it as (item, total) or (date, count).

print("=" * 45)
print("  TOTAL QUANTITY PER ITEM")
print("=" * 45)

for item, total in sorted(item_totals.items()):
    # f-strings let us insert variables directly into a string using {}
    # The :<30 part pads the item name to 30 characters so the numbers line up neatly
    print(f"  {item:<30} {total:>3} units")

print()  # Blank line for spacing

print("=" * 45)
print("  NUMBER OF ORDERS PER PICKUP DATE")
print("=" * 45)

for date, count in sorted(date_counts.items()):
    # "order" vs "orders" — small touch so the grammar is always correct
    label = "order" if count == 1 else "orders"
    print(f"  {date}    {count} {label}")

print()
print("Done! Summary complete.")
