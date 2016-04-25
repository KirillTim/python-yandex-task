import sys
if len(sys.argv) < 2:
    print("./first <file name>")
    exit(1)

with open(sys.argv[1], "rb") as f:
    files = {}
    sender = None
    FROM_BYTES = str.encode("From ")
    for line in f:
        if line[:5] == FROM_BYTES:
            sender = line.decode().split(' ')[1]
            if sender not in files:
                files[sender] = open(sender, "wb")
        if sender:
            files[sender].write(line)

    for f in files.values():
        f.close()
