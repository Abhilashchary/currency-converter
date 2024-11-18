# Fixed Rate Currency Converter 💱

This is a simple **Currency Converter** program written in Python. It uses fixed exchange rates to convert between various currencies. The program is user-friendly and allows users to perform multiple conversions in one session.

## Features
- **Available Currencies**: USD, EUR, GBP, JPY, INR.
- **Fixed Conversion Rates**: Uses predefined exchange rates to convert between currencies.
- **Interactive User Interface**: Allows users to input amounts and select currencies dynamically.
- **Error Handling**: Ensures users input valid currencies and amounts.

## Requirements
To run this program, you'll need:
- Python 3.x installed on your system.

No additional libraries are required, as this project uses Python's built-in capabilities.

## How to Run
1. Clone or download this repository:
   ```bash
   git clone https://github.com/Abhilashchary/currency-converter.git
   cd fixed-rate-currency-converter
   ```
2. Run the script:
   ```bash
   python currency_converter.py
   ```

3. Follow the prompts:
   - Enter the amount you want to convert.
   - Choose the currency you are converting **from** (e.g., USD).
   - Choose the currency you are converting **to** (e.g., EUR).
   - The program will display the converted amount.

4. You can perform additional conversions or exit the program when done.

## Conversion Rates
The script uses fixed conversion rates relative to USD:
- **USD**: 1.0 (Base currency)
- **EUR**: 0.85
- **GBP**: 0.75
- **JPY**: 110.0
- **INR**: 73.5

These rates can be adjusted by modifying the `exchange_rates` dictionary in the `FixedRateCurrencyConverter` class.

## Error Handling
- The program ensures that the entered currencies are valid and supported.
- If the user provides invalid input, a descriptive error message is displayed.
- Invalid numeric inputs or unsupported currencies will prompt the user to retry.

## File Details
- `currency_converter.py`: The main script containing the implementation of the currency converter.

## Contribution
Feel free to fork the repository and submit pull requests for:
- Adding more currencies.
- Implementing dynamic exchange rate updates using an API.
- Enhancing the user interface.
