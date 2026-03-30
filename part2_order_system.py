# Task 1 – Explore the Menu

# Provided Data
menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

# ---------------- Step 1: Print menu grouped by category ----------------
print("\n===== FULL MENU =====\n")

# Get unique categories
categories = set(item["category"] for item in menu.values())

for category in categories:
    print(f"===== {category} =====")
    for item_name, details in menu.items():
        if details["category"] == category:
            availability = "[Available]" if details["available"] else "[Unavailable]"
            print(f"{item_name:<15} ₹{details['price']:.2f}   {availability}")
    print()  # Empty line after each category

# ---------------- Step 2: Dictionary computations ----------------
# Total number of items
total_items = len(menu)

# Total number of available items
available_items = sum(1 for item in menu.values() if item["available"])

# Most expensive item
most_expensive_item = max(menu.items(), key=lambda x: x[1]["price"])
most_exp_name = most_expensive_item[0]
most_exp_price = most_expensive_item[1]["price"]

# Items priced under ₹150
under_150 = [(name, details["price"]) for name, details in menu.items() if details["price"] < 150]

# ---------------- Step 3: Print summary ----------------
print("----- SUMMARY -----")
print(f"Total menu items         : {total_items}")
print(f"Total available items    : {available_items}")
print(f"Most expensive item      : {most_exp_name} (₹{most_exp_price:.2f})")
print("Items priced under ₹150  :")
for name, price in under_150:
    print(f" - {name} (₹{price:.2f})")
    
    # Task 2 — Cart Operations

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

cart = []

# ---------- Function to add items to cart ----------
def add_to_cart(item_name, quantity):
    if item_name not in menu:
        print(f"⚠ '{item_name}' does not exist in the menu.")
        return
    if not menu[item_name]["available"]:
        print(f"⚠ '{item_name}' is currently unavailable.")
        return
    
    # Check if already in cart
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] += quantity
            print(f"Updated '{item_name}' quantity to {entry['quantity']}")
            return
    
    # Add new entry
    cart.append({"item": item_name, "quantity": quantity, "price": menu[item_name]["price"]})
    print(f"Added '{item_name}' ×{quantity} to cart.")

# ---------- Function to remove items from cart ----------
def remove_from_cart(item_name):
    for entry in cart:
        if entry["item"] == item_name:
            cart.remove(entry)
            print(f"Removed '{item_name}' from cart.")
            return
    print(f"⚠ '{item_name}' not found in cart.")

# ---------- Function to print cart ----------
def print_cart():
    if not cart:
        print("Cart is empty.")
        return
    print("\nCurrent Cart:")
    for entry in cart:
        total_price = entry["quantity"] * entry["price"]
        print(f"{entry['item']:<15} x{entry['quantity']}  ₹{total_price:.2f}")
    print()

# ---------- Simulate the sequence ----------
print("---- Adding Items ----")
add_to_cart("Paneer Tikka", 2)
print_cart()

add_to_cart("Gulab Jamun", 1)
print_cart()

add_to_cart("Paneer Tikka", 1)  # Should update quantity
print_cart()

add_to_cart("Mystery Burger", 1)  # Does not exist
print_cart()

add_to_cart("Chicken Wings", 1)   # Unavailable
print_cart()

remove_from_cart("Gulab Jamun")
print_cart()

# ---------- Order Summary ----------
print("========== Order Summary ==========")
subtotal = 0
for entry in cart:
    total_price = entry["quantity"] * entry["price"]
    subtotal += total_price
    print(f"{entry['item']:<15} x{entry['quantity']}  ₹{total_price:.2f}")

gst = subtotal * 0.05
total_payable = subtotal + gst

print("------------------------------------")
print(f"Subtotal:                ₹{subtotal:.2f}")
print(f"GST (5%):                ₹{gst:.2f}")
print(f"Total Payable:           ₹{total_payable:.2f}")
print("====================================")

# Task 3 — Inventory Tracker with Deep Copy
import copy

# Provided inventory data
inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

# Assume cart from Task 2
cart = [
    {"item": "Paneer Tikka", "quantity": 3, "price": 180.0}
]

# ---------------- Step 1: Deep copy ----------------
inventory_backup = copy.deepcopy(inventory)

# Demonstrate deep copy works
print("----- Before manual change -----")
print("Inventory:", inventory["Paneer Tikka"])
print("Inventory Backup:", inventory_backup["Paneer Tikka"])

# Change stock manually
inventory["Paneer Tikka"]["stock"] = 5
print("\n----- After manual change -----")
print("Inventory:", inventory["Paneer Tikka"])
print("Inventory Backup:", inventory_backup["Paneer Tikka"])  # Should remain 10

# Restore inventory to original
inventory = copy.deepcopy(inventory_backup)

# ---------------- Step 2: Fulfill cart orders ----------------
for entry in cart:
    item_name = entry["item"]
    order_qty = entry["quantity"]
    
    if item_name not in inventory:
        print(f"⚠ {item_name} not found in inventory.")
        continue
    
    available_stock = inventory[item_name]["stock"]
    
    if order_qty > available_stock:
        print(f"⚠ Only {available_stock} unit(s) of {item_name} available. Deducting what is possible.")
        inventory[item_name]["stock"] = 0
    else:
        inventory[item_name]["stock"] -= order_qty

# ---------------- Step 3: Check for Reorder Alerts ----------------
print("\n----- Reorder Alerts -----")
for item_name, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print(f"⚠ Reorder Alert: {item_name} — Only {details['stock']} unit(s) left (reorder level: {details['reorder_level']})")

# ---------------- Step 4: Print final inventories ----------------
print("\n----- Final Inventory -----")
for item, details in inventory.items():
    print(f"{item}: {details}")

print("\n----- Inventory Backup (unchanged) -----")
for item, details in inventory_backup.items():
    print(f"{item}: {details}")
    
    # Task 4 — Daily Sales Log Analysis

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

# ---------------- Step 1: Total revenue per day ----------------
print("----- Total Revenue Per Day -----")
daily_revenue = {}
for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total
    print(f"{date}: ₹{total:.2f}")

# ---------------- Step 2: Best-selling day ----------------
best_day = max(daily_revenue.items(), key=lambda x: x[1])
print(f"\nBest-selling day: {best_day[0]} — ₹{best_day[1]:.2f}")

# ---------------- Step 3: Most ordered item ----------------
item_count = {}
for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            item_count[item] = item_count.get(item, 0) + 1

most_ordered_item = max(item_count.items(), key=lambda x: x[1])
print(f"Most ordered item: {most_ordered_item[0]} — Appeared in {most_ordered_item[1]} orders")

# ---------------- Step 4: Add new day ----------------
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

# Recompute daily revenue
print("\n----- Updated Total Revenue Per Day -----")
daily_revenue = {}
for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total
    print(f"{date}: ₹{total:.2f}")

best_day = max(daily_revenue.items(), key=lambda x: x[1])
print(f"\nUpdated best-selling day: {best_day[0]} — ₹{best_day[1]:.2f}")

# ---------------- Step 5: Numbered list of all orders ----------------
print("\n----- Numbered Orders Across All Dates -----")
order_number = 1
for date, orders in sales_log.items():
    for order in orders:
        items_str = ", ".join(order["items"])
        print(f"{order_number}.  [{date}] Order #{order['order_id']}  — ₹{order['total']:.2f} — Items: {items_str}")
        order_number += 1