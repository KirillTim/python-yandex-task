import sys


def gen(senders_count, mails_per_sender, lines_per_mail, chars_per_line):
    line = [''.join([c] * chars_per_line) for c in ["a", "b"]]
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
    if len(sys.argv) < 5:
        print(sys.argv[0]+" <senders_count> <mails_per_sender> <lines_per_mail> <chars_per_line>")
        exit(1)
    else:
        gen(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))


if __name__ == "__main__":
    main()
