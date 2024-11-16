'''
Created on 10/9/2024
@author: Yahia Abdelsalam
Pledge: "I pledge my honor that I have abided by the Stevens Honor System"

CS115 - Hw 3
'''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount, coins):
    '''
    Returns a list where the first item is the minimum number of coins needed to make 'amount',
    and the second item is a list of the coins used to make that amount.
    
    amount: int, the target amount
    coins: list of int, the denominations of coins available
    '''
    if amount == 0:
        return [0, []]  
    if amount < 0 or coins == []:
        return [float('inf'), []]  

    # Option 1: Use the first coin
    use_it = giveChange(amount - coins[0], coins)
    if use_it[0] != float('inf'):
        use_it = [use_it[0] + 1, [coins[0]] + use_it[1]]

    
    lose_it = giveChange(amount, coins[1:])

    
    if use_it[0] < lose_it[0]:
        return use_it
    else:
        return lose_it


# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(letter, scorelist):
    '''Returns the score of a single letter.'''
    for item in scorelist:
        if letter == item[0]:
            return item[1]
    return 0  

def wordScore(word, scorelist):
    '''Returns the Scrabble score for a word.'''
    if word == '':
        return 0
    return letterScore(word[0], scorelist) + wordScore(word[1:], scorelist)

def wordsWithScore(dct, scores):
    '''
    List of words in dct, with their Scrabble score.
    Assume dct is a list of words and scores is a list of [letter, number] pairs.
    Returns a list where each word is paired with its Scrabble score.
    '''
    if dct == []:
        return []
    return [[dct[0], wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if n == 0 or L == []:
        return []
    return [L[0]] + take(n - 1, L[1:])


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if n == 0 or L == []:
        return L
    return drop(n - 1, L[1:])

# Testing giveChange function


print(giveChange(48, [1, 5, 10, 25, 50]))
print(wordsWithScore(['a', 'am', 'at', 'apple', 'bat', 'bar'], scrabbleScores))
print(wordsWithScore(Dictionary, scrabbleScores)) 
print(take(3, [1, 2, 3, 4, 5]))
print(drop(3, [1, 2, 3, 4, 5]))
