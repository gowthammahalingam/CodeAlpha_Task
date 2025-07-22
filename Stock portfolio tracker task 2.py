def stock_portfolio_tracker():
    print("--- Stock Portfolio Tracker ---")
    # Hardcoded dictionary of stock prices
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 150, "MSFT": 420, "AMZN": 185}
    portfolio = {}  # Dictionary to store user's stock and quantity
    total_investment = 0.0

    print("Available stocks and their prices:")
    for stock, price in stock_prices.items():
        print(f"  {stock}: ${price}")

    while True:
        stock_name = input("Enter stock symbol (e.g., AAPL) or 'done' to finish: ").upper()
        if stock_name == 'DONE':
            break # Exit the loop if the user types 'done'

        if stock_name not in stock_prices:
            print("Invalid stock symbol. Please choose from the available stocks.")
            continue # Ask for input again

        while True: # Loop to ensure valid quantity input
            try:
                quantity = int(input(f"Enter quantity for {stock_name}: "))
                if quantity <= 0:
                    print("Quantity must be a positive number.")
                else:
                    break # Exit quantity loop if valid
            except ValueError:
                print("Invalid quantity. Please enter a whole number.")

        # Add or update stock quantity in the portfolio
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print(f"Added {quantity} shares of {stock_name}.")

    print("\n--- Your Portfolio ---")
    if not portfolio: # Check if the portfolio is empty
        print("No stocks added to your portfolio.")
    else:
        # Calculate and display investment for each stock
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = quantity * price
            total_investment += investment
            print(f"{stock}: {quantity} shares @ ${price} = ${investment:.2f}")
        print(f"Total Investment Value: ${total_investment:.2f}")

        # Optional: Save results to a file
        save_option = input("Do you want to save the results to a file? (yes/no): ").lower()
        if save_option == 'yes':
            filename = input("Enter filename (e.g., portfolio.txt or portfolio.csv): ")
            try:
                with open(filename, 'w') as f: # Open file in write mode
                    if filename.endswith('.csv'):
                        # Write CSV header and data
                        f.write("Stock,Quantity,Price,Investment\n")
                        for stock, quantity in portfolio.items():
                            price = stock_prices[stock]
                            investment = quantity * price
                            f.write(f"{stock},{quantity},{price},{investment:.2f}\n")
                        f.write(f"\nTotal Investment Value,{total_investment:.2f}\n")
                    else: # Default to .txt if not .csv
                        f.write("--- Your Portfolio ---\n")
                        for stock, quantity in portfolio.items():
                            price = stock_prices[stock]
                            investment = quantity * price
                            f.write(f"{stock}: {quantity} shares @ ${price} = ${investment:.2f}\n")
                        f.write(f"Total Investment Value: ${total_investment:.2f}\n")
                print(f"Portfolio saved to {filename}")
            except IOError as e:
                print(f"Error saving file: {e}")
    print("-" * 20)

# To run the Stock Portfolio Tracker:
if __name__ == "__main__":
    stock_portfolio_tracker()