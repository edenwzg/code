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