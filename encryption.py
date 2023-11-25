# encryption using a linear feedback shift register
from copy import deepcopy
import bindec


def char_to_base64(c):
    """Converts a single character string to the base64 int

    Args:
        c (str): A single character string

    Raises:
        ValueError: If string is longer than 1 character, or character is
        not in the base64 encoding

    Returns:
        int: The base64 value of the character
    """
    if len(c) > 1:
        raise ValueError("String is longer than 1 character")

    c_utf8 = ord(c)
    if c_utf8 >= 65 and c_utf8 <= 90:
        c_base64 = c_utf8 - 65  # 'A' is 0
    elif c_utf8 >= 97 and c_utf8 <= 122:
        c_base64 = c_utf8 - 97 + 26  # 'a' is 26
    elif c_utf8 >= ord('0') and c_utf8 <= ord('9'):
        c_base64 = c_utf8 - ord('0') + 26 + 26  # '0' is 52
    elif c_utf8 == ord('+'):
        c_base64 = c_utf8 - ord('+') + 26 + 26 + 10  # '+' is 62
    elif c_utf8 == ord('/'):
        c_base64 = c_utf8 - ord('/') + 26 + 26 + 10 + 1  # '/' is 63
    else:
        raise ValueError('Character should be from the base64 table provided '
                         'in the assignment!', c, c_utf8)
    return c_base64


def base64_to_utf8(i):
    if i < 0 or i > 63:
        raise ValueError('Invalid base64 integer value')

    if i >= 0 and i < 26:  # Uppercase letter
        # 'A' is chr(65)
        c_utf8 = chr(65+i-0)
    elif i >= 26 and i < 52:  # Lowercase lettter
        # 'a' is chr(97) and base64('a') = 26
        c_utf8 = chr(97+i-26)
    elif i >= 52 and i < 62:  # Numeral
        # '0' is chr(48) and base64('0') = 52
        c_utf8 = chr(48+i-52)
    elif i == 62:  # '+'
        c_utf8 = '+'
    elif i == 63:  # '/'
        c_utf8 = '/'
    else:
        raise ValueError(
            'Conversion of base64 int to UTF-8 value unsuccessful')
    return c_utf8


def charToBin(c):
    # converts a character c into a list of six 1's and 0's using Base64 encoding
    # Possible values are from 0-63
    c_base64 = char_to_base64(c)
    return bindec.decToBin(c_base64)


def binToChar(b):
    # converts a list of six 1's and 0's into a character using Base64 encoding
    if len(b) != 6:
        raise ValueError(
            'Incorrect length of list for conversion to character')
    c_base64 = 0
    loop_count = len(b) - 1
    for val in b:
        c_base64 = c_base64 + (val * 2 ** loop_count)
        loop_count -= 1
    return base64_to_utf8(c_base64)


def strToBin(s):
    # convert a string of characters into a list of 1's and 0's using Base64 encoding
    bin_list = []
    for c in s:
        bin_list = bin_list + charToBin(c)
    return bin_list


def binToStr(b_list):
    # convert a list of 1's and 0's into a string of characters using Base64 encoding
    char_list =[] 
    for i in range(0, len(b_list), 6):
        char_list.append(binToChar(b_list[i:i+6]))
    return ''.join(char_list)


def generatePad(seed, k, length):
    # generates a sequence of pseudo-random numbers
    my_seed = deepcopy(seed)
    offset = len(seed) - k
    lfsr = []
    for i in range(length):
        feedback = my_seed[i] ^ my_seed[i+offset]
        my_seed.append(feedback)
        lfsr.append(feedback)
    return lfsr


def encrypt(message, seed, k):
    # takes a message and returns it as an encrypted string using an [N, k] LFSR
    #Generate base64 representation of message
    my_message_base64 = strToBin(message)
    #Generate LFSR for encryption
    my_lfsr = generatePad(seed, k, len(my_message_base64))
    encrypted_bin = []
    for i in range(len(my_message_base64)):
        encrypted_bin.append(my_message_base64[i] ^ my_lfsr[i])
    
    char_list=[]
    for i in range(0, len(encrypted_bin), 6):
        char_list.append(binToChar(encrypted_bin[i:i+6]))
    return binToStr(encrypted_bin)
