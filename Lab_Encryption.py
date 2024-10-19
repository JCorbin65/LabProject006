
def letter_to_index(letter, alphabet):
    return alphabet.index(letter)


def index_to_letter(index, alphabet):
    return alphabet[index]

def vignere_index(key_letter, plaintext_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)
    ciphertext_index = (plaintext_index + key_index) % len(alphabet)
    return index_to_letter(ciphertext_index, alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    key_repeated = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    ciphertext = []
    for i in range(len(plaintext)):
        p_letter = plaintext[i]
        k_letter = key_repeated[i]
        c_letter = vignere_index(k_letter, p_letter, alphabet)
        ciphertext.append(c_letter)
    return ''.join(ciphertext)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "VIVELEMPERUER"
plaintext = "OURCAVALRYISPREPARINGTOATTACKATNOONTOMORROW"
ciphertext = encrypt_vigenere(key, plaintext, alphabet)
print(ciphertext)