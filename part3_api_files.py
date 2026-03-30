# ===============================
# Task 1 — File Read & Write Basics
# ===============================

# Part A — Write
file_name = "python_notes.txt"

# Lines to write initially
notes = [
    "Topic 1: Variables store data. Python is dynamically typed.",
    "Topic 2: Lists are ordered and mutable.",
    "Topic 3: Dictionaries store key-value pairs.",
    "Topic 4: Loops automate repetitive tasks.",
    "Topic 5: Exception handling prevents crashes."
]

# Writing the initial lines
with open(file_name, 'w', encoding="utf-8") as f:
    for line in notes:
        f.write(line + "\n")
print("File written successfully.")

# Append two more lines of your own
additional_notes = [
    "Topic 6: Functions help in code reuse.",
    "Topic 7: Modules organize Python code logically."
]

with open(file_name, 'a', encoding="utf-8") as f:
    for line in additional_notes:
        f.write(line + "\n")
print("Lines appended successfully.")

# Part B — Read
try:
    with open(file_name, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    # Print each line numbered
    print("\n----- File Contents -----")
    for idx, line in enumerate(lines, 1):
        print(f"{idx}. {line.strip()}")

    # Total number of lines
    print(f"\nTotal number of lines: {len(lines)}")

    # Search for keyword
    keyword = input("\nEnter a keyword to search for: ").strip().lower()
    found = False
    print(f"\nLines containing '{keyword}':")
    for line in lines:
        if keyword in line.lower():
            print(line.strip())
            found = True
    if not found:
        print(f"No lines found containing '{keyword}'.")
        
except FileNotFoundError:
    print(f"Error: {file_name} does not exist.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
    
    # ===============================
# Task 2 — API Integration
# ===============================

import requests
import json

# ---------------- Step 1: Fetch 20 products ----------------
print("----- Step 1: Fetch 20 Products -----")
url_products = "https://dummyjson.com/products?limit=20"
try:
    response = requests.get(url_products)
    response.raise_for_status()  # Raise error for bad responses
    data = response.json()
    products = data.get("products", [])

    # Print formatted table header
    print(f"{'ID':<3} | {'Title':<30} | {'Category':<15} | {'Price':<8} | {'Rating'}")
    print("-"*70)
    for product in products:
        print(f"{product['id']:<3} | {product['title']:<30} | {product['category']:<15} | ${product['price']:<7} | {product['rating']}")
except requests.RequestException as e:
    print("Error fetching products:", e)

# ---------------- Step 2: Filter & Sort ----------------
print("\n----- Step 2: Products with rating >= 4.5, sorted by price desc -----")
filtered = [p for p in products if p["rating"] >= 4.5]
sorted_filtered = sorted(filtered, key=lambda x: x["price"], reverse=True)

for product in sorted_filtered:
    print(f"{product['title']} — ${product['price']} — Rating: {product['rating']}")

# ---------------- Step 3: Search by Category (Laptops) ----------------
print("\n----- Step 3: Laptops Category -----")
url_laptops = "https://dummyjson.com/products/category/laptops"
try:
    response = requests.get(url_laptops)
    response.raise_for_status()
    laptops = response.json().get("products", [])
    for laptop in laptops:
        print(f"{laptop['title']} — ${laptop['price']}")
except requests.RequestException as e:
    print("Error fetching laptops:", e)

# ---------------- Step 4: POST Request (Simulated) ----------------
print("\n----- Step 4: POST a Custom Product -----")
url_post = "https://dummyjson.com/products/add"
payload = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

try:
    response = requests.post(url_post, json=payload)
    response.raise_for_status()
    post_result = response.json()
    print("POST Response:")
    print(json.dumps(post_result, indent=4))
except requests.RequestException as e:
    print("Error sending POST request:", e)
    
    # ===============================
# Task 3 — Exception Handling
# ===============================

import requests

# ---------------- Part A: Guarded Calculator ----------------
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

# Test safe_divide
print("---- Part A: Guarded Calculator ----")
print("10 / 2 =", safe_divide(10, 2))
print("10 / 0 =", safe_divide(10, 0))
print("'ten' / 2 =", safe_divide("ten", 2))


# ---------------- Part B: Guarded File Reader ----------------
def read_file_safe(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")

# Test read_file_safe
print("\n---- Part B: Guarded File Reader ----")
print("\nReading existing file:")
print(read_file_safe("python_notes.txt"))

print("\nReading non-existing file:")
print(read_file_safe("ghost_file.txt"))


# ---------------- Part C: Robust API Calls ----------------
def robust_get(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print("Unexpected error:", e)
    return None

def robust_post(url, data):
    try:
        response = requests.post(url, json=data, timeout=5)
        response.raise_for_status()
        return response
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print("Unexpected error:", e)
    return None


# ---------------- Part D: Input Validation Loop ----------------
print("\n---- Part D: Product Lookup ----")
while True:
    user_input = input("Enter a product ID to look up (1–100), or 'quit' to exit: ").strip()
    if user_input.lower() == "quit":
        print("Exiting product lookup.")
        break

    # Validate input
    if not user_input.isdigit():
        print("Invalid input. Please enter a number between 1 and 100.")
        continue

    product_id = int(user_input)
    if not (1 <= product_id <= 100):
        print("Invalid input. Number must be between 1 and 100.")
        continue

    # Make robust API call
    url = f"https://dummyjson.com/products/{product_id}"
    response = robust_get(url)
    if response:
        if response.status_code == 404:
            print("Product not found.")
        elif response.status_code == 200:
            product = response.json()
            print(f"Product: {product['title']}, Price: ${product['price']}")
        else:
            print(f"Unexpected HTTP status: {response.status_code}")
            
            # ===============================
# Task 4 — Error Logger
# ===============================

import requests
from datetime import datetime

# Function to log errors
def log_error(function_name, error_type, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ERROR in {function_name}: {error_type} — {message}\n"
    with open("error_log.txt", "a", encoding="utf-8") as f:
        f.write(log_entry)

# ------------------ Trigger 1: ConnectionError ------------------
print("Triggering ConnectionError...")
try:
    response = requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
    response.raise_for_status()
except requests.exceptions.ConnectionError as e:
    log_error("fetch_products", "ConnectionError", str(e))
    print("Logged ConnectionError.")

# ------------------ Trigger 2: HTTPError (404) ------------------
print("Triggering HTTP 404 error for product lookup...")
product_id = 999
try:
    url = f"https://dummyjson.com/products/{product_id}"
    response = requests.get(url, timeout=5)
    if response.status_code != 200:
        log_error("lookup_product", "HTTPError", f"{response.status_code} Not Found for product ID {product_id}")
        print(f"Logged HTTPError for product ID {product_id}.")
except requests.exceptions.RequestException as e:
    log_error("lookup_product", type(e).__name__, str(e))
    print(f"Logged unexpected error: {e}")

# ------------------ Display log file contents ------------------
print("\n--- Current contents of error_log.txt ---")
try:
    with open("error_log.txt", "r", encoding="utf-8") as f:
        logs = f.read()
        print(logs)
except FileNotFoundError:
    print("No logs found yet.")