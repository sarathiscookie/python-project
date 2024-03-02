# Number occurs at begin, middle or end.
# Number may not occurs in the array.
# Number may be repeated.
# If repeated get first position.
# Number may be an one array.
# Number may be negative array.

# Algorithm
# Set a value 0.
# Check number is matching with the query.
# If it's not matching increment the value and repeat steps.
# It the number not found return -1.

# Code
def main():
    query = int(input("Enter the card number: "))
    cards = [10, 9, 8, 7, 6, 5, 3, 2, 1]
    print(locate_card(cards, query))

def locate_card(cards, query):

    for card in cards:

        if card == query:
            return card

    return -1

if __name__ == "__main__":
    main()

# Time complexity: O(N)
# Space complexity: O(1)
