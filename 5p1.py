import hashlib

def main():
    testinput = "abc"
    testindex = 0
    testhash = hashlib.md5((testinput + str(testindex)).encode("utf-8")).hexdigest()
    testpw = ""
    while len(testpw) < 8:
        while not notZeros(testhash):
            testhash = hashlib.md5((testinput + str(testindex)).encode("utf-8")).hexdigest()
        print(testhash)
        testpw = testpw + testhash[6]


def notZeros(pwhash):
    return pwhash[0:6] == "000000"

if __name__ == "__main__":
    main()
