with open("unix.mailbox") as f:
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
