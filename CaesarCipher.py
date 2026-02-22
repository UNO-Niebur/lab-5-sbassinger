#CaesarCipher.py
#Name:Scott Bassinger
#Date:02/22/2026
#Assignment:Lab 5 - Caesar Cipher



#Caesar Cipher
#The Caesar cipher moves each letter forward in the alphabet by
#the key.  The resulting message has all the letters advanced by 'key'
#letters.
#To run the code, run the main() function

def encode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    secret = ""

    for letter in message:
        if (alpha.find(letter) >= 0): #check to see if the letter is actually a letter
            spot = (alpha.find(letter) + key) % 26
            secret = secret + alpha[spot]
        else: # letter must have been a number, symbol, or punctuation.
            secret = secret + letter

    return secret

def decode(secret, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    secret = secret.upper()
    message1 = ""
    for ch in secret:
        if(alpha.find(ch) >=0 ):
            spot = (alpha.find(ch) + key * -1) % 26
            message1 = message1 + alpha[spot]
        else:
            message1 = message1 + ch
    return message1 


def main():
    message = input("Enter a message: ")
    key = int(input("Enter a key: "))

    secret = encode(message, key)
    print ("Encrypted:", secret)
    plaintext = decode(secret, key)
    print ("Decrypted:", plaintext)


if __name__ == '__main__':
  main()
