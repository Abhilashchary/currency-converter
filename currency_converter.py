class FixedRateCurrencyConverter:
    def __init__(self):
        # Dictionary to store conversion rates to a base currency (e.g., USD)
        self.exchange_rates = {
            'USD': 1.0,    # Base currency
            'EUR': 0.85,   # 1 USD = 0.85 EUR
            'GBP': 0.75,   # 1 USD = 0.75 GBP
            'JPY': 110.0,  # 1 USD = 110 JPY
            'INR': 73.5    # 1 USD = 73.5 INR
        }

    def show_available_currencies(self):
        # Display available currencies in a user-friendly way
        print("\nAvailable Currencies:")
        for currency in self.exchange_rates:
            print(f" - {currency}")

    def convert_currency(self, amount, from_currency, to_currency):
        # Validate if both currencies are supported
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("Currency not supported.")
        
        # Convert amount to USD (base currency) first
        amount_in_usd = amount / self.exchange_rates[from_currency]
        
        # Convert USD to the target currency
        converted_amount = amount_in_usd * self.exchange_rates[to_currency]
        
        return round(converted_amount, 2)

def main():
    # Create an instance of the converter
    converter = FixedRateCurrencyConverter()
    
    while True:
        print("\n--- Currency Converter ---")
        converter.show_available_currencies()

        try:
            # Input amount and currency choices from the user
            amount = float(input("\nEnter amount to convert: "))
            from_currency = input("From currency: ").upper()
            to_currency = input("To currency: ").upper()

            # Perform the conversion
            converted_amount = converter.convert_currency(amount, from_currency, to_currency)
            print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
        
        except ValueError as e:
            print(f"Error: {e}")

        # Ask the user if they want to perform another conversion
        choice = input("\nDo you want to convert another amount? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Thank you for using the currency converter!")
            break

if __name__ == "__main__":
    main()
