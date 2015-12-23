import hashlib

def to_infinity():
    index = 0
    while 1:
        yield index
        index += 1

key = "ckczppom"

for i in to_infinity():
    test = key + str(i)
    test = test.encode('utf-8')
    m = hashlib.md5()
    m.update(test)
    md5 = m.hexdigest()
    if str(md5).startswith("000000"):
        print(test.decode('utf-8'))
        print(m.hexdigest())
        break



