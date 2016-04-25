import sys
if len(sys.argv) < 2:
    print("./first <file name>")
    exit(1)

with open(sys.argv[1]) as f:
    files = {}
    sender = None
    for line in f:
        if line.startswith("From "):
            sender = line.split(' ')[1]
            if sender not in files:
                files[sender] = open(sender, "w")
        if sender:
            files[sender].write(line)

    for f in files.values():
        f.close()
