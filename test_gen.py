import sys


def gen(senders_count, lines_per_mail, mails_per_sender):
    line = [''.join([c] * 1000) for c in ["a", "b"]]
    with open("maxtest.mailbox", "w") as f:
        senders = ["sender" + str(x) + "@mail.com" for x in range(senders_count)]
        for i in range(mails_per_sender):
            for s in senders:
                msg = "From " + s + " Any Date Here\n"
                for j in range(lines_per_mail):
                    msg += (line[j % 2] + "\n")
                msg += "\n"
                f.write(msg)


def main():
    if len(sys.argv) < 4:
        print("test_gen.py <senders_count> <lines_per_mail> <mails_per_sender>")
        exit(1)
    else:
        gen(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))


if __name__ == "__main__":
    main()
