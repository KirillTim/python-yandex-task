#tests and benchmarks: https://github.com/KirillTim/python-yandex-task
import sys


def main():
    if len(sys.argv) < 2:
        print(sys.argv[0]+" <file name>")
        exit(1)

    with open(sys.argv[1], "rb") as input:
        from_bytes = str.encode("From ")
        files = {}
        sender = prev_sender = None
        buf = bytearray()
        for line in input:
            if line[:5] == from_bytes:
                sender = line.decode().split(' ')[1]
                if sender not in files:
                    files[sender] = open(sender, "wb")
            if sender:
                if not prev_sender:
                    prev_sender = sender
                elif sender != prev_sender:
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
