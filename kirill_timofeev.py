#tests and benchmarks: https://github.com/KirillTim/python-yandex-task
import sys


def main():
    if len(sys.argv) < 2:
        print(sys.argv[0]+" <file name>")
        exit(1)
    #sometimes such a big read buffer can help
    #avoid python encoding troubles -- read bytes, not strings
    with open(sys.argv[1], "rb", buffering = 1024*1024) as input:
        from_bytes = str.encode("From ") #it's 2016, everybody should use utf-8
        #it works with other encodings though
        files = {}
        sender = prev_sender = None
        buf = bytearray()
        for line in input:
            if line[:5] == from_bytes:
                sender = line.decode().split(' ')[1]
                if sender not in files:
                    files[sender] = open(sender, "wb")
            if sender: #skip all lines before first mail header
                if not prev_sender:
                    prev_sender = sender
                elif sender != prev_sender:
                    #write all email using one write() syscall
                    #python is smart enough to set the size of write() buffer as len(buf)
                    files[prev_sender].write(buf)
                    prev_sender = sender
                    buf = bytearray()

                buf += line
        if sender:
            files[sender].write(buf)
        for f in files.values():
            f.close()


if __name__ == "__main__":
    main()
