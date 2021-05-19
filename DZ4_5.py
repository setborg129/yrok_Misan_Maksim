from my_utils import valuta


def main(argv):
    program, *argv = argv
    valuta(*argv)


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
