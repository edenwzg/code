def reverse(sequence):
    ''' Return the Reverse sequence. '''
    return sequence[::-1]


def is_palindrome(sequence):
    ''' Return the sequence is palindrome ? '''
    return sequence == reverse(sequence)