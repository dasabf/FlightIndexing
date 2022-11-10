from Flights.ManageFlights import *


def __flight__():
    choice = input("Enter (1) for Add Flight to the database \nEnter (2) for View all Flights in the database"
                   "\nEnter (3) for exit from console...\n")
    while choice != "3":
        if choice == "1":
            flight = input("Enter Flight Name You Want To Add :: ")
            add(flight)
        elif choice == "2":
            viewFlightName()

        choice = input("Enter (1) for Add Flight to the database \nEnter (2) for View all Flights in the database"
                       "\nEnter (3) for exit from console...\n")

