import csv
import os
import matplotlib.pyplot as plt
import yfinance as yf

def get_live_stock_price(ticker_symbol):
    """Fetches real-time asset price from Yahoo Finance API."""
    try:
        ticker_object = yf.Ticker(ticker_symbol)
        live_price = ticker_object.fast_info['last_price']
        if live_price is None or str(live_price) == 'nan':
            return None
        return float(live_price)
    except Exception:
        return None

def generate_portfolio_chart(user_portfolio):
    """Processes the portfolio data and renders the visual chart."""
    tickers = list(user_portfolio.keys())
    values = list(user_portfolio.values())
    
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    bars = ax.barh(tickers, values, color='#2ca02c', edgecolor='#1a611a', height=0.6)
    
    ax.set_title('Real-Time Portfolio Asset Allocation ($ USD)', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Total Position Value ($)', fontsize=12, fontweight='bold', labelpad=10)
    ax.set_ylabel('Asset Ticker', fontsize=12, fontweight='bold')
    
    for bar in bars:
        width = bar.get_width()
        ax.text(width + (width * 0.02),        
                bar.get_y() + bar.get_height()/2, 
                f"${width:,.2f}", 
                va='center', ha='left', fontsize=10, fontweight='bold', color='#333333')
                
    plt.tight_layout()
    print("📊 Launching visual engine window...")
    plt.show()

def main():
    raw_holdings = {}
    
    print("=========================================")
    print("   VISUAL LIVE-TICKING ASSET ANALYTICS   ")
    print("=========================================")
    print("Type 'done' when you have finished entering your positions.\n")

    while True:
        ticker = input("Enter asset ticker (e.g., AAPL, NVDA, TSLA): ").upper().strip()
        if ticker == "DONE":
            break
            
        print(f"📡 Verifying {ticker} market value...")
        live_price = get_live_stock_price(ticker)
        
        if live_price is None:
            print("❌ Invalid symbol or server connection failure. Skipping.")
            continue
            
        # FIXED: Explicitly print the single asset price right here!
        print(f"💰 LIVE PRICE: 1 share of {ticker} = ${live_price:,.2f}")
        
        try:
            quantity = float(input(f"How many units/shares do you own of {ticker}? "))
            if quantity <= 0:
                print("❌ Value must be positive.")
                continue
        except ValueError:
            print("❌ Numeric entries only.")
            continue
            
        raw_holdings[ticker] = raw_holdings.get(ticker, 0.0) + quantity
        print(f"✅ Position updated.\n")

    if not raw_holdings:
        print("No assets provided. Exiting.")
        return

    # --- EVALUATE LIVE NET WORTH & PREPARE GRAPHING DICTIONARY ---
    print("\nProcessing real-time financial sheets...")
    final_portfolio_valuation = {}
    csv_rows = []
    total_net_worth = 0.0
    
    # Updated Header to explicitly display both Single Unit Price and Total Value
    print("\n" + "=" * 58)
    print(f"{'ASSET':<10}{'UNITS':<12}{'UNIT PRICE':<16}{'TOTAL VALUE':<15}")
    print("-" * 58)
    
    for ticker, quantity in raw_holdings.items():
        price = get_live_stock_price(ticker)
        position_value = quantity * price
        total_net_worth += position_value
        
        # Display neatly aligned console text showing single price AND total value
        print(f"{ticker:<10}{quantity:<12,.2f}${price:<15,.2f}${position_value:<15,.2f}")
        
        final_portfolio_valuation[ticker] = position_value
        csv_rows.append([ticker, quantity, round(price, 2), round(position_value, 2)])

    print("-" * 58)
    print(f"TOTAL NET WORTH: ${total_net_worth:,.2f}")
    print("=" * 58 + "\n")

    # --- AUTO-EXPORT LOG ENTRY ---
    filename = "visual_portfolio_manifest.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Ticker", "Units", "Single Unit Price", "Total Position Value"])
        writer.writerows(csv_rows)
        writer.writerow([])
        writer.writerow(["TOTAL VALUE", "", "", f"${total_net_worth:,.2f}"])
    print(f"💾 Local log generated at: {os.path.basename(filename)}")

    # --- TRIGGER THE MATPLOTLIB PLOT SYSTEM ---
    generate_portfolio_chart(final_portfolio_valuation)

if __name__ == "__main__":
    main()