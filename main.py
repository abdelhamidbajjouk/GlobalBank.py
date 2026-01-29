#!/usr/bin/env python3

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
                    capital: int,
                    country: str,
                    currency: str,
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
        print("Successfuly created a new bank!")
        if print_info:
            print(f"Bank name: {name.capitalize()}\nBank capital: {capital}\n"
                  f"Bank's country: {country.capitalize()}")


def main():
    global_bank = GlobalBank()
    global_bank.create_bank("attijari", 2000000000, "morocco", "MAD")
    global_bank.create_bank("CDM", 20000000, "morocco", "MAD")
    global_bank.create_bank("test", 20000, "morocco", "MAD")
    global_bank.create_bank("attijari", 2000000000, "morocco", "MAD")
    while True:
        choice = input(
            "=== WELCOME TO GLOBAL BANK ===\n"
            "1) Create a new bank\n"
            "2) List banks by country\n"
            "3) Exit\n"
            "Select an option: "
        )
        if choice == "3":
            break


main()
