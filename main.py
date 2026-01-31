#!/usr/bin/env python3

import json


class Bank:
    def __init__(self, name: str, capital: int, country: str):
        self.name = name
        self.capital = capital
        self.country = country
        self.users = {}


class GlobalBank:
    def __init__(self):
        self.banks = {}

    def create_bank(self,
                    name: str,
                    country: str,
                    currency: str = "USD",
                    capital: int = 1000000,
                    print_info: bool = False) -> None:
        self.banks.setdefault('countries', {})
        self.banks['countries'].setdefault(country, [])
        for bank in self.banks['countries'][country]:
            if bank.get("name") == name:
                print("Bank already exists!")
                return
        self.banks['countries'][country].append({
            "name": name,
            "capital": capital,
            "currency": currency
            })
        with open("db.txt", "w+") as db_file:
            json.dump(self.banks, db_file, indent=4)
        print("Successfuly created a new bank!")
        if print_info:
            print(f"Bank name: {name.capitalize()}\nBank capital: {capital}\n"
                  f"Bank's country: {country.capitalize()}")


def create_bank(bank_instance: GlobalBank):
    print("=== BANK CREATION ===")
    bank_name = input("Please insert the bank name: ")
    bank_capital = input("Enter bank's capital(PRESS ENTER TO SKIP): ")
    bank_country = input("Enter bank's country/location: ")
    bank_currency = input("Enter bank's currency: ")
    if not bank_name:
        create_bank()
    if not bank_capital or not bank_country or not bank_currency:
        bank_capital = "100000"
        bank_country = "morocco"
        bank_currency = "MAD"
    bank_instance.create_bank(bank_name, bank_country, bank_currency, bank_capital)


def list_banks(country: str):
    print("=== LISTING BANKS ===")
    with open("db.txt", "r") as db_file:
        data = json.load(db_file)
    for key, banks in data['countries'].items():
        for bnk in banks:
            print(f"Bank's Name: {bnk.get('name')}")
            print(f"Bank's Capital: {int(bnk.get('capital')):,.2f}") # I KNOW THIS STUPID TO DO IN ONE LINE BUT ANYWAY
            print(f"Bank's Currency: {bnk.get('currency')}")
            print(f"Bank's Country: {key.capitalize()}")
            print("=========================================")


def main():
    # IGNORE FOR NOW THIS IS FOR TESTING
    REAL_MODE = True
    global_bank = GlobalBank()
    # global_bank.create_bank("attijari", "morocco", "MAD", "2000000000")
    # global_bank.create_bank("CDM", 20000000, "morocco", "MAD")
    # global_bank.create_bank("test", 20000, "morocco", "MAD")
    # global_bank.create_bank("attijari", 2000000000, "morocco", "MAD")
    # list_banks(global_bank, 'morocco')
    while REAL_MODE:
        choice = input(
            "=== WELCOME TO GLOBAL BANK ===\n"
            "1) Create a new bank\n"
            "2) List all banks\n"
            "3) List banks by country\n"
            "4) Exit\n"
            "Select an option: "
        )
        if choice == "1":
            create_bank(global_bank)
        elif choice == "2":
            list_banks()
        elif choice == "3":
            print("OPTION CURRENTLY DISABLED")
        elif choice == "4":
            print("LEAVING GLOBAL BANK DASHBOARD")
            break

if __name__ == "__main__":
    try:
        main()
    except BaseException:
        print("\n!!!PROGRAM EXITED!!!")
        
