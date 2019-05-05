import hashlib

with open('passwords.txt') as f:
    passwords = f.read().splitlines()

with open('/usr/share/dict/words') as f:
    words = f.read().splitlines()

for word in words:
    for pw in passwords:
        for x in range(500):
            guess = word + str(x)
            digest = hashlib.sha256(guess.encode('UTF-8')).hexdigest()
            if digest == pw:
                print("Found password {} for hash {}.".format(guess, pw))
                break
