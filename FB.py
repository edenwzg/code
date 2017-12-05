#coding = utf-8

FORBIDDEN = ('!', '?', '.', ',', ' ')
SEPARATOR = ('_', '-','.')

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

def fibonacci(max):
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


def counter(low, high):
    '''
    Counter for genterator.
    '''
    while low <= high:
        yield low
        low += 1


def get_part(filename, initchar='', symbols='-_.'):
    '''
    Find the keyword in a filename. 
    
    :param1: this is a string to be processed
    :param2: search for initials
    :param3: split symobls for str
    :return: a string with '_' intervals 

    :example: 
        in [1]: filename = '12_dioguitar23.net_MKBD-S109-s30d_H265-1080P-264_482.mp4'
        in [2]: get_part(filename, 's')
        Out[2]: 'S109_S30D'
    '''

    import re
    import os

    main_name = splitf(filename)
    symbols = '[' + symbols + ']+'    
    parts = re.split(symbols, main_name.strip().replace(' ', '_'))
    result = []

    if initchar.upper() not in main_name.upper():
        # Not fund
        return main_name
    elif initchar == '':
        # Find number
        print 'a'
        [result.append(part) for part in parts if part.isdigit()] 
    else:
        # Find specified initial char
        [result.append(part.upper()) for part in parts if part[0].upper() == initchar.upper()]
    
    return '_'.join(result)


def splitf(filename, part="main"):
    '''
    Rerurn the extension from a filename.
    :param1: this is a string to be processed
    :param2: 
        part='main' return the main name
        part='ext' return the extension name
    :return: string
    '''

    import os

    if part == 'main':
        result = os.path.splitext(filename)[0]
    if part == 'ext':
        result = os.path.splitext(filename)[1]

    return result


def print_dict(d, flip=False): 
    '''
    '''
    if flip:
        for k, v in d.items():
            print '%-20s%s' % (v,k)
    else:
        for k, v in d.items():
            print '%-50s%s' % (k,v)


def write_dict(h, d, flip=True): 
    '''
    '''
    if flip:
        for k, v in d.items():
            h.write('%-20s%s\n' % (v,k))
    else:
        for k, v in d.items():
            h.write('%-50s%s\n' % (k,v))          


def modify_filename_from_file(file, dir):
    '''
    Read the file to modify the filename.
    
    MKBD_S61.jpg        dioguitar23.net_MKBD-S61.jpg
    front part          back part

    front part is the current file name
    back part is the name to be modified

    :param1: file path for Record file name
    :param2: the directory for modify the file name
    :return: None
    
    '''
    import os
    from os.path import join

    for line in open(file, 'r'):
        os.rename(join(dir, line.split()[0]), join(dir, line.split()[1]))


def modify_filename(file, dir, base, char):
    '''
    Modify file name.

    :param1: 
    :param2: 
    :param3: 
    :param4: 
    '''

    import os
    from os.path import join
    from os.path import isfile

    f = open(file, 'w')
    newnames = {}
    
    try:
        for name in os.listdir(dir):
            if isfile(join(dir, name)) == True:
                newnames[name] = '%s_%s%s' % (base, get_part(name, char), splitf(name, part='ext'))
                os.rename(join(dir,name), join(dir, newnames[name]))
        
        print_dict(newnames, flip=True)
        write_dict(f, newnames)
        print "%s files done!" % len(newnames)
    finally:
        f.close()


# ----------------------------------------------------------------------

if __name__ == '__main__':
    pass
