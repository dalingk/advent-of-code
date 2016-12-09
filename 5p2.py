import hashlib

def main():
    doorid = "uqwqemis"
    doorindex = 0
    doorpassword = ["_","_","_","_","_","_","_","_"]
    print("".join(x for x in doorpassword), end="\r")
    while not isDone(doorpassword): 
        doorhash = hashlib.md5((doorid + str(doorindex)).encode("utf-8")).hexdigest()
        while not first5Zeros(doorhash):
            doorindex += 1
            doorhash = hashlib.md5((doorid + str(doorindex)).encode("utf-8")).hexdigest()
        if validIndex(doorhash[5]) and doorpassword[int(doorhash[5])] == "_":
            doorpassword[int(doorhash[5])] = doorhash[6]
            print("".join(x for x in doorpassword), end="\r")
        doorindex += 1
    print("".join(x for x in doorpassword))

def first5Zeros(pwhash):
    return pwhash[0:5] == "00000"

def isDone(pwarray):
    for element in pwarray:
        if element == "_":
            return False
    return True

def validIndex(character):
    number = int(character, 16)
    return number >= 0 and number < 8

if __name__ == "__main__":
    main()
