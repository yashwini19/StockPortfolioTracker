from colorama import Fore, Style, init
import csv

# Initialize colorama
init(autoreset=True)

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300,
    "AMZN": 200,
    "NFLX": 350
}

# Dictionary to store user portfolio
portfolio = {}


# ---------------- Banner ---------------- #

def banner():
    print(Fore.CYAN + "=" * 50)
    print(Fore.GREEN + "        📈 STOCK PORTFOLIO TRACKER")
    print(Fore.CYAN + "=" * 50)


# ---------------- Menu ---------------- #

def menu():
    print("\nChoose an Option")
    print(Fore.YELLOW + "1. Add Stock")
    print("2. View Portfolio")
    print("3. Save Portfolio")
    print("4. Exit")


# ---------------- Display Stocks ---------------- #

def display_stocks():
    print(Fore.MAGENTA + "\nAvailable Stocks")
    print("-" * 30)

    for stock, price in stock_prices.items():
        print(f"{stock}  --> ₹{price}")

    print("-" * 30)


# ---------------- Add Stock ---------------- #

def add_stock():

    display_stocks()

    stock = input("\nEnter Stock Name: ").upper()

    if stock not in stock_prices:
        print(Fore.RED + "❌ Invalid Stock Name!")
        return

    try:
        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print(Fore.RED + "Quantity must be greater than zero.")
            return

    except ValueError:
        print(Fore.RED + "Please enter numbers only.")
        return

    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

    print(Fore.GREEN + "✅ Stock Added Successfully!")


# ---------------- View Portfolio ---------------- #

def view_portfolio():

    if len(portfolio) == 0:
        print(Fore.RED + "\nPortfolio is Empty!")
        return

    print(Fore.CYAN + "\nYOUR PORTFOLIO")
    print("=" * 60)

    print(f"{'Stock':10}{'Qty':10}{'Price':10}{'Value'}")
    print("-" * 60)

    total = 0
    highest_stock = ""
    highest_value = 0

    for stock, qty in portfolio.items():

        price = stock_prices[stock]

        value = qty * price

        total += value

        if value > highest_value:
            highest_value = value
            highest_stock = stock

        print(f"{stock:10}{qty:<10}{price:<10}₹{value}")

    print("-" * 60)

    print(Fore.GREEN + f"💰 Total Investment : ₹{total}")

    print(Fore.YELLOW + f"🏆 Highest Investment : {highest_stock} (₹{highest_value})")


# ---------------- Save Portfolio ---------------- #

def save_portfolio():

    if len(portfolio) == 0:
        print(Fore.RED + "Portfolio is Empty!")
        return

    # Save TXT
    with open("portfolio.txt", "w") as file:

        total = 0

        file.write("STOCK PORTFOLIO\n")
        file.write("=" * 40 + "\n")

        for stock, qty in portfolio.items():

            value = qty * stock_prices[stock]
            total += value

            file.write(f"{stock} | Qty:{qty} | Value: ₹{value}\n")

        file.write("=" * 40 + "\n")
        file.write(f"Total Investment = ₹{total}")

    # Save CSV
    with open("portfolio.csv", "w", newline="") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow(["Stock", "Quantity", "Price", "Investment"])

        for stock, qty in portfolio.items():
            writer.writerow([
                stock,
                qty,
                stock_prices[stock],
                qty * stock_prices[stock]
            ])

    print(Fore.GREEN + "✅ Portfolio Saved Successfully!")
    print(Fore.CYAN + "Files Created:")
    print("📄 portfolio.txt")
    print("📄 portfolio.csv")


# ---------------- Main Program ---------------- #

while True:

    banner()

    menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_stock()

    elif choice == "2":
        view_portfolio()

    elif choice == "3":
        save_portfolio()

    elif choice == "4":
        print(Fore.GREEN + "\nThank you for using Stock Portfolio Tracker!")
        break

    else:
        print(Fore.RED + "Invalid Choice!")

    input("\nPress Enter to continue...")