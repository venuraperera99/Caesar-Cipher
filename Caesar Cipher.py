import string
def caesar_encryption(msg, shift):
    lst = []
    for i in msg:
        shifttext(i, shift, lst)
                
    encrypt = ''.join(lst)
    return encrypt

def caesar_decryption(msg, shift):
    pass

def shifttext(i, shift, lst):
    alph = 'abcdefghijklmnopqrstuvwxyz' #alphabet to map the shifting
    if i.strip() and i in alph: # if character 'i' isnt a space shift it by the shift amount else append to the list
        new = (alph.index(i)+shift)%26
        lst.append(alph[new])
    else:
        lst.append(i)



if __name__ == "__main__":
    cipher_lst = {}  # keys represent the cipher messeges and the mapped value corresponds to the shift value
    print(caesar_encryption("abc", 3))