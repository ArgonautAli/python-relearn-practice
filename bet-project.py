from betUtils import get_number_of_lines
from betUtils import get_bet
import random

ROWS = 3
COLS = 3

SYMBOLS = { "A": 2, "B": 4, "C": 6, "D": 8 }

def get_slot_machine_spins(rows, cols, symbols):
    all_symbols = []
    for symbol, counts in symbols.items():
        for _ in range(counts):
            all_symbols.append(symbol)

    columns = []

    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns



def deposit():
    while True:
        amount = input("Enter amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter positive amount")
        else:
            print("Please enter a number")
    
    return amount

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in  enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else: print(column[row], end = "")

        print()


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        if bet > balance:
            print("Your bet can't be more than your balance $", balance)
        else:
            break
    print(f"You are betting ${bet} on ${lines} line. Your total bet is $", bet*lines)

    slots = get_slot_machine_spins(ROWS, COLS, SYMBOLS)
    print_slot_machine(slots)


main()
                