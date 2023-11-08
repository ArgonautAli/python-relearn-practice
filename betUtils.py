MAX_LINES = 3
MAX_BET = 100
MIN_BET = 50

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter valid number of lines")
        else:
            print("Please enter a number")
    
    return lines

def get_bet():
    while True:
        bet = input("Enter your bet on each line: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} & {MAX_BET}")
        else:
            print("Please enter a number")
    
    return bet
