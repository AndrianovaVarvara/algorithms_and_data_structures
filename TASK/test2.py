def blackjack_hand_greater_than(hand_1):
    """
    Return True if hand_1 beats hand_2, and False otherwise.

    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21

    Hands are represented as a list of cards. Each card is represented by a string.

    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.

    When determining a hand's total, you should try to count aces in the way that
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14."""

    def total_in_hand(hand):
        total = 0
        aces = 0
        for card in hand:
            if card in ['J', 'Q', 'K']:
                total += 10
            elif card == 'A':
                aces += 1
            else:
                total += int(card)
        total += aces

        while total + 10 <= 21 and aces > 0:

            total += 10
            aces -= 1
        return total

    def blackjack_hand_greater_than(hand_1, hand_2):
        total_1 = total_in_hand(hand_1)
        total_2 = total_in_hand(hand_2)
        return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)