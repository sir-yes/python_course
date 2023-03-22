# Prime number checker
'''
n = int(input("Check this number: "))
print(n % 1)
def prime_checker(number):
    if n == 2 or n == 3:
        print(number,"Is a Prime Number")
    elif n == 1:
        print(number,"Is Not a Prime Number")
    elif n % 2 == 0 or n % 3 == 0:
        print(number,"Is Not a Prime Number")
    else:
        print(number,"Is a Prime Number")

prime_checker(number=n)
'''
# Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(plain_text,shift_amount,cipher_direction):
    result = ""
    if cipher_direction == "decode":
        shift_amount *= - 1
    for i in plain_text:
        get_index_of_i = alphabet.index(i)
        #if cipher_direction == "decode":
        #    shift_amount *= - 1
        new_position = get_index_of_i + shift_amount
        result += alphabet[new_position]
        #shift_amount *= - 1
    print(f"The {cipher_direction}d text is {result}")
caesar(text, shift, direction)