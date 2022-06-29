from datetime import date
from colorama import Fore

if __name__ == '__main__':
    MILES_ALLOWED_PER_YEAR = 12000
    MILES_ALLOWED_PER_DAY = 32.87

    days_since_lease_start = date.today() - date(2022, 3, 14)
    current_max_mileage = days_since_lease_start.days * MILES_ALLOWED_PER_DAY
    print("It has been " + str(days_since_lease_start.days) + " days since the lease started.")
    print(str(MILES_ALLOWED_PER_YEAR) + " miles are allowed per year.")
    print(str(MILES_ALLOWED_PER_DAY) + " miles are allowed per day.")
    print("To stay on track, the total mileage today should be under " + str(current_max_mileage) + " miles.")

    current_miles = int(input("\nEnter current mileage: "))

    print("\n---------------------------------------------------------------------")

    mileage_delta = int(current_max_mileage - current_miles)

    if mileage_delta >= 0:
        print("\nYou have ", end='')
        print(Fore.CYAN + str(mileage_delta), end='')
        print(Fore.RESET + " miles remaining to stay on track.")
    else:
        print("\nYou are ", end='')
        print(Fore.RED + str(abs(mileage_delta)), end='')
        print(Fore.RESET + " miles over the current allowed mileage.")
