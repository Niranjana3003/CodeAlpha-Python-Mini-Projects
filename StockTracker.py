def stock_portfolio_tracker():
    # Hardcoded dictionary of stock prices
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 2700, "AMZN": 3400}
    
    portfolio = {}
    print("Enter stock names and quantities (type 'done' to finish):")
    
    while True:
        stock_name = input("Stock name: ").upper()
        if stock_name == 'DONE':
            break
        if stock_name not in stock_prices:
            print("Stock not found in price list. Try again.")
            continue
        try:
            quantity = int(input("Quantity: "))
        except ValueError:
            print("Please enter a valid number for quantity.")
            continue
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    # Calculate total investment
    total_investment = sum(stock_prices[s] * q for s, q in portfolio.items())

    print(f"\nTotal investment value: ${total_investment}")

    # Optional: Save result to file
    save = input("Save result to file? (yes/no): ").lower()
    if save == 'yes':
        filename = input("Enter filename (with .txt or .csv extension): ")
        with open(filename, 'w') as f:
            f.write("Stock,Quantity,Price per Share,Total Value\n")
            for s, q in portfolio.items():
                f.write(f"{s},{q},{stock_prices[s]},{stock_prices[s]*q}\n")
            f.write(f"\nTotal investment value,,,{total_investment}\n")
        print(f"Result saved to {filename}")

# Run the tracker
if __name__ == "__main__":
    stock_portfolio_tracker()