import hashlib

def main():
    doorid = "uqwqemis"
    doorindex = 0
    doorpassword = ""
    while len(doorpassword) < 8:
        doorhash = hashlib.md5((doorid + str(doorindex)).encode("utf-8")).hexdigest()
        while not first5Zeros(doorhash):
            doorindex += 1
            doorhash = hashlib.md5((doorid + str(doorindex)).encode("utf-8")).hexdigest()
        print("hash: {}, index: {}".format(doorhash, doorindex))
        doorpassword += doorhash[5]
        doorindex += 1
    print(doorpassword)

def first5Zeros(pwhash):
    return pwhash[0:5] == "00000"

if __name__ == "__main__":
    main()
