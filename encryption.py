# encryption using a linear feedback shift register
import bindec
b64_char_order = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"0",'1','2','3','4','5','6','7','8','9','+','/']


# converts a character c into a list of six 1's and 0's using Base64 encoding
def charToBin(c):
    dec_b64= b64_char_order.index(str(c))
    char_in_bin = bindec.decToBin(dec_b64,6)
    return char_in_bin

# converts a list of six 1's and 0's into a character using Base64 encoding
def binToChar(b):
    dec_pos= int(bindec.binToDec(b))
    b64_char = b64_char_order[dec_pos]
    return b64_char

# convert a string of characters into a list of 1's and 0's using Base64 encoding
def strToBin(b64_message):
    bin_string=[]
    for i in range(len(b64_message)):
        character = b64_message[i]
        bin_char= charToBin(character)
        bin_string = bin_string + bin_char
    # Implement me
    return bin_string

# convert a list of 1's and 0's into a string of characters using Base64 encoding
def binToStr(b_list):
    i=0
    b64_string = ""
    while i in range(len(b_list)):
        the_six_digits= b_list[i:i+6]
        b64_char = binToChar(the_six_digits)
        b64_string = b64_string + b64_char
        i+=6
    return b64_string

# generates a sequence of pseudo-random numbers
def generatePad(seed_param, k, length):
    random_list = []
    seed = seed_param
    i=0
    while i <= length:
        if seed[0] == seed[-k]:
            random_list.append(0)
            seed.append(0)

        else:
            random_list.append(1)
            seed.append(1)

        seed.pop(0)
        i+=1
    # Implement me
    return random_list

# takes a message and returns it as an encrypted string using an [N, k] LFSR
def encrypt(message, seed, k):
    bin_message= strToBin(message)
    random_key = generatePad(seed, k, len(bin_message))
    encrypted_bin_message = []
    for i in range(len(bin_message)):
        if bin_message[i]==random_key[i]:
            encrypted_bin_message.append(0)
        else:
            encrypted_bin_message.append(1)

    encrypted_message = binToStr(encrypted_bin_message)
    return encrypted_message
