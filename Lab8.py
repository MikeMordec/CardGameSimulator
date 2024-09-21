'''
Created on May 1, 2022

@author: michaelmordec
'''
import random

def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    # Return the deck.
    return deck
    
#shuffle the items in a deck/dictionary
def shuffle(deck):
    shuffled_items = list(deck.items())  # List of tuples of (key,values)
    random.shuffle(shuffled_items)
    keys = []
    values = []
    for key, value in shuffled_items:
        keys.append(key)
        values.append(value)
    shuffled_deck = dict(zip(keys, values))
    return shuffled_deck

def main():
    deck = create_deck()
    deck = shuffle(deck)
    
    score1 = 0
    score2 = 0
    while(len(deck.items())>0):
        newcard1 = deck.popitem()
        newcard2 = deck.popitem()
        print()
        print("Player 1",newcard1)
        print("Player 2",newcard2)
        
        newCard1Value = newcard1[1]
        newCard2Value = newcard2[1]

        if(score1 < 11 and newCard1Value == 1):
            score1 = score1 + 10
        if(score2 < 11 and newCard2Value == 1):
            score2 = score2 + 10
    
        
        score1 = score1 + newcard1[1]
        score2 = score2 + newcard2[1]
               
        print("Player 1 score is", score1)
        print("Player 2 score is", score2)
        if(score1 == 21 and score2 == 21):
            print("Tied!")
            return;
        if(score1 > 21 and score2 > 21):
            print("Both busted!")
            return;
        if(score1 <= 21 and score2 > 21):
            print("Player 1 wins with a score of",score1)
            return;
        if(score2 <= 21 and score1 > 21):
            print("Player 2 wins with a score of",score2)
            return;
    print("No more cards left.")    
        
main()