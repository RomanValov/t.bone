
print('t.bone: kosh kelinizder')


def main(argv):
    opts = {} # --opts

    pipe = ' '.join(argv).split('/')

    for part in pipe:
        print(part.strip())

def bone(argv):
    main(argv)
