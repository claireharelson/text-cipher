from operator import itemgetter

# Using frequency analysis to break an encrypted message

# Read in two files: ciphertext.txt and freq.txt
m = open("ciphertext.txt", "r")
f = open("freq.txt", "r")

# Initialize variables
message = m.readlines()
message = str(message)
freq = []


# Define the function, accept the message, & return a dictionary
def get_freq_counts():
    for line in f.readlines():
        frequency = line.strip().split(":")
        freq.append((str(frequency[0]), int(frequency[1])))
    dict_freq = dict(freq)
    sort_freq = sorted(dict_freq.items(), key=itemgetter(int(1)))
    sort_freq = dict(sort_freq)

    letters = "abcdefghijklmnopqrstuvwxyz "
    letter_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                    'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                    'y': 0, 'z': 0, ' ': 0}

    # Count appearances of each letter in the message
    for i in message:
        if i in letters:
            letter_count[i] += 1

    # Remove letters not in the message
    for (key, value) in list(letter_count.items()):
        if value == 0:
            del letter_count[key]

    # Sort dictionary in ascending order
    sort_count = sorted(letter_count.items(), key=itemgetter(int(1)))
    sort_count = dict(sort_count)

    # Create a third dictionary mapping letters to each other
    new_dict = {}
    sort_freq = list(sort_freq)
    sort_count = list(sort_count)

    for i in sort_count:
        for j in sort_freq:
            new_dict[i] = j
            sort_freq.remove(j)
            break

    # Use a conditional statement to replace the message keys with the new mapped letters
    list_message = list(message)

    for index, item in enumerate(list_message):
        for key, value in new_dict.items():
            if item == key:
                list_message[index] = value

    decoded = ' '.join(map(str, list_message))
    print(decoded)
    # Result: mtcom thorn are the oss adents leetind in the rear ou saint larvs softh chfrch auter rear agliram
    # slith retfrns urol his trayem abroag to lafritania uor operation immicitscent


get_freq_counts()

# Provide final decoded message -- some by hand
# Corrected letter swaps: m/l, f/u, g/d, y/v/b/p

# ltcol thorn are the oss agents meeting in the rear of saint marys south church after rear admiral
# smith returns from his travel abroad to Mauritania for operation illicitscent
