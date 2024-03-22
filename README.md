# base64-Encryption
This project encrypts and decrypts a message using a Linear Feedback Shift Register (LFSR) and Base64 encoding. The initial project was developed in October 2022. Here's an explanation of each function:

* charToBin(c): This function converts a character c into a list of six 1's and 0's using Base64 encoding. It first finds the index of the character c in the b64_char_order list, which represents the order of characters in Base64 encoding. Then, it converts this index to a binary representation with a fixed length of 6 using the bindec.decToBin() function from the bindec module.

* binToChar(b): This function performs the reverse operation of charToBin(). It converts a list of six 1's and 0's (b) into a character using Base64 encoding. It first converts the binary list b to its decimal equivalent using bindec.binToDec(), then finds the character corresponding to this decimal value in the b64_char_order list.

* strToBin(b64_message): This function converts a string of characters (b64_message) into a list of 1's and 0's using Base64 encoding. It iterates through each character in the input string, converts it to binary using charToBin(), and concatenates the binary representations.

* binToStr(b_list): This function performs the reverse operation of strToBin(). It converts a list of 1's and 0's (b_list) into a string of characters using Base64 encoding. It iterates through the binary list, extracts groups of six bits, and converts each group to its corresponding character using binToChar().

* generatePad(seed_param, k, length): This function generates a pseudo-random sequence of numbers using an LFSR. It takes a seed (seed_param), a parameter k (the size of the shift register), and the desired length of the sequence to generate. It initializes the LFSR with the seed and iterates length times, shifting the register and updating it based on the LFSR algorithm.

* encrypt(message, seed, k): This function encrypts a message using the LFSR-generated pseudo-random sequence. It first converts the input message to binary using strToBin(), then generates the LFSR sequence using generatePad(). Finally, it performs a bitwise XOR operation between the message and the LFSR sequence to obtain the encrypted binary sequence and converts it back to a string using binToStr().
