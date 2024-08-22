import requests

def get_exchange_rate(base, target):
    base_url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    url = f"{base_url}?symbols={target}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve data")
        return None

def main():
    while True:
        print("1. Naira to other currency")
        print("2. Other currency to Naira")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            target_currency = input("Enter currency (e.g. USD, EUR, GBP): ").upper()
            amount = int(input("NGN: "))
            exchange_info = get_exchange_rate("NGN", target_currency)
            if exchange_info:
                print(f"Date: {exchange_info['date']}")
                print(f"{amount} NGN = {amount * exchange_info['rates'][target_currency]} {target_currency}")
        elif choice == "2":
            base_currency = input("Enter currency (e.g. USD, EUR, GBP): ").upper()
            amount = int(input("Enter amount in {}: ".format(base_currency)))
            exchange_info = get_exchange_rate(base_currency, "NGN")
            if exchange_info:
                print(f"Date: {exchange_info['date']}")
                print(f"{amount} {base_currency} = {amount * exchange_info['rates']['NGN']} NGN")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()