# Keanu Foltz Module 4.2 11/10/24
# Displays graph of temperature highs or lows based on user selection

import sys

import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Extract dates, high temperatures, and low temperatures
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

def plot_highs():
    # plots highs
    plt.figure()
    plt.plot(dates, highs, c='red')
    plt.title("Daily High Temperatures - 2018", fontsize=24)
    plt.xlabel("", fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.gcf().autofmt_xdate()
    plt.show()


def plot_lows():
    # plots lows
    plt.figure()
    plt.plot(dates, lows, c='blue')
    plt.title("Daily Low Temperatures - 2018", fontsize=24)
    plt.xlabel("", fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.gcf().autofmt_xdate()
    plt.show()


def selection_menu():
    # menu display
    while True:
        print("Menu:")
        print("1: Show High Temperatures")
        print("2: Show Low Temperatures")
        print("3: Exit")

        option = input("Input option 1, 2, or 3: ")

        if option == '1':
            plot_highs()
        elif option == '2':
            plot_lows()
        elif option == '3':
            print("Exit program, Goodbye!")
            sys.exit(0)
        else:
            print("Please input 1, 2, or 3.")


# Run the program
if __name__ == "__main__":
    selection_menu()