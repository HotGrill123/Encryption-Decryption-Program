#use a word as a code
import random # maybe i'll do a random key
texts = []
converted = []
keycheck = []
ed = "y"
ans = ""
convertword = ""
def keypart(key): # finds the ascii code for every letter in the key
    keys = []
    for x in range(0, len(key)):
        keys.append(ord(key[x]))
    return keys
def keypart2(dkey): # does the same thing as keypart, but it's for the decoding.
    keys = []
    for x in range(0, len(key)):
        keys.append(ord(key[x]))
    return keys

def convert(temp): # changing ascii characters to stuff between a-z
    counter = 0
    newtemp = temp
    while newtemp > 122:
        newtemp = newtemp - 25
        counter += 1
    newtemp = chr(newtemp)
    return newtemp, str(counter)

def unconvert(temp): # similar to the convert, but adds instead of subtracts.
    newtemp = temp
    counter = 0
    while newtemp < 97:
        newtemp += 25
        counter += 1
    newtemp = chr(newtemp)
    return newtemp, str(counter)
print("disclaimer: this program's decoding system can only work using this program's exlusive encoding system due to how it is shaped.")
print("Therefore, we recommend that you use the encoding system before using the decoding system. Happy hunting! \n")
while ed == "y":
    ans = input("encode, decode or quit? \n")
    while ans != "encode" and ans != "decode" and ans != "quit":
        ans = input("Invalid answer. Please input encode or decode. \n")
    if ans == "encode":
        counters = ""
        text = input("input text to type up \n")
        key = input("input a word as a key \n")
        keys = keypart(key)
        for x in range(0,len(text)): # converts everything in the text into their individual ascii characters
            texts.append(ord(text[x]))
        for x in range(0,len(text)):
            temp = keys[((len(key) + x) % len(key))] # goes in a loop of numbers according to the length of the key　(たとえば, if key is 3 letters long, it'll do 0 1 2 0 1 2 for a while).
            keycheck.append(temp)                    # check logic stuff at the bottom for how it worked.
            temp = texts[x] + temp
            converted.append(convert(temp))
        for x in range(0,len(converted)):
            convertword += converted[x][0]
            counters += converted[x][1]
        print(convertword)
        print(counters)
 
#logic stuff
# if key is 5 positions, then it should go keys[0], keys[1], keys[2], keys[3], keys[4], keys[5], then loops round to keys[0]
#therefore, if we want to use unknowns, we have to add the unknown by x each time, then divide by unknown and use the remainder
#for example, if the unknown is 5, we have to do (5 + x) % 5. When x is 0, the answer is 0, then 1,2,3,4,then loops back to 0.


#decryption, which only works if the encoding happened in the one above/something similar, and spacebars won't be recognised because of technical difficulties i'll explain at the bottom.
    if ans == "decode":
        dtexts = []
        dconverted = []
        dcounters = ""
        dkeycheck = []
        dconvertword = ""
        dtext = input("input text to decrypt \n")
        dkey = input("input the key used to encrypt the data \n")
        val = input("what were the numbers that popped up underneath? \n")
        dkeys = keypart(dkey)
        for x in range(0,len(dtext)):
            dtexts.append(ord(dtext[x]))
        for x in range(0,len(dtext)):
            temp = dkeys[((len(dkey) + x) % len(dkey))]
            dkeycheck.append(temp)
            temp = dtexts[x] - temp
            newtemp = temp
            newtemp = newtemp + (25 * int(val[x]))
            dconverted.append(chr(newtemp))
        for x in range(0,len(dconverted)):
            dconvertword += dconverted[x][0]
        print("the decoded message is as follows :")
        print(dconvertword, "\n \n")
    else:
        ed = "n"

# more logic stuff


#the decryption only works with this specific encryption program due to how the program decrypts. The numbers that are generated after encrypting are a sort of "cycle".
#the cycle determines how many times it looped through a-z while encoding the text. The reason why these numbers are important is because without them, the decyphering program
#doesn't know where the encoder stopped looping. For example, to get from the letter a to r may have taken 2 loops, however to get fromt the letter y to r may have been a likely
#output in that situation , which would've taken 3 loops. The decyphering program wouldn't know how to differentiate between r and y, and would therefore output a sentence that has
#most likely mixed up y and r. To fix this, the way i've programmed it to decypher is to use the loop number in a formula in order to find what letter specifically it was originally.
#that is why this program can only work with itself; the numbers are a sort of "third key" per se, which are exclusive to this program.

