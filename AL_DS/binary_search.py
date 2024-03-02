# Algorithm
# Find the middle element of the list.
# If it is matching return the result.
# If it is less than queried number, then search the first half of the list.
# If it is greater than the queried number, then search the second half of the list.
# If not more elements remain return -1.

# Code
def main():
    cards = [9, 7, 6, 4, 3, 2, 1]
    query = int(input("Enter the query: "))
    length_of_cards = len(cards)
    print(binary_search(query, length_of_cards, cards))

def binary_search(query, length_of_cards, cards):
    if length_of_cards % 2 == 0:
        middle_value = length_of_cards // 2 - 1
    else:
        middle_value = length_of_cards // 2

    print(middle_value)
    print(query)

    if middle_value == query:
        return query
    elif middle_value < query:
        return cards[:middle_value]
    elif middle_value > query:
        return cards[middle_value:]
    else:
        return -1

if __name__ == "__main__":
    main()



