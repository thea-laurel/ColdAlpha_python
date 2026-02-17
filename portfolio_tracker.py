stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

portfolio = {}
total_value = 0

print("STOCK PORTFOLIO TRACKER")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or DONE to finish): ").upper()
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid stock name.")
        continue

    quantity = int(input("Enter quantity: "))
    portfolio[stock] = quantity

print("\nPORTFOLIO SUMMARY")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares")

print(f"Total Investment Value: ₹{total_value}")

with open("portfolio_summary.txt", "w") as file:
    file.write("PORTFOLIO SUMMARY\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock}: {qty} shares\n")
    file.write(f"Total Investment Value: INR {total_value}")