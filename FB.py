FORBIDDEN = ('!', '?', '.', ',', ' ')

def reverse(string):
    '''
    Reverse the character in the string. 
    
    :param1: this is a string to be processed
    :return: a copy of the string S
    '''
    return string[::-1]


def is_palindrome(string):
    ''' 
    Check if the string is palindrome.

    :param1: this is a string to be processed
    :return: boolean 
    '''
    return string == reverse(string)


def remove_forbidden(string, forbidden=','):
    '''
    Remove the forbidden char.

    :param1: this is a string to be processed
    :param2: this is the deleted character sequence
    :return: a copy of the string S
    '''
    for char in forbidden:
        if char in string:
            string = string.replace(char, '')
    return  string


def make_change(amount, coins=[1, 5, 10, 25], hand=None):
    '''
    Find the only way to convert a dollar into any set of COINS 
    '''
    hand = [] if hand is None else hand
    if amount == 0:
        yield hand
    for coin in coins:
        if coin > amount or (len(hand) > 0 and hand[-1] < coin):
            continue
        for result in make_change(amount - coin, coins = coins, hand = hand + [coin]):
            yield result

def Fibonacci(max):
    '''
    Fibonacci number.

    param1: to generate the number for fibonacci series
    '''
    a, b, n = 0, 0, 1
    if n < max:
        yield b
        a, b = b, a+b
        n += 1
    raise StopIteration('Done')


class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def next(self):
        if self.current < self.high:
            self.current += 1
            return self.current -1
        raise StopIteration


def Counter_generator(low, high):
    while low <= high:
        yield low
        low += 1