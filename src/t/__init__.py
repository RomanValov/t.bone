
#print('t.bone: kosh kelinizder')


def _set(argv, data):
    if not argv:
        raise KeyError()

    key = argv.pop(0)

    if not argv:
        raise ValueError()

    value = argv.pop(0)

    data[key] = value

    return data


func = {
    'set': _set,
}


def hint(name):
    raise NotImplementedError(name)


def main(opts, argv, init):
    pipe = ' '.join(argv).split('/')

    data = None
    for part in pipe:
        elem = part.split()

        if not elem:
            continue

        name = elem.pop(0)

        if data is None:
            data = init()

        data = func.get(name, lambda *_: hint(name))(elem, data)

        if data is None:
            break

    return data



def bone(sys):
    import json
    from collections import defaultdict

    opts = defaultdict(bool)

    argv = []
    for item in sys.argv[1:]:
        extra, _, value = item.partition('--')

        if not extra and value:
            opts[value] = True
        else:
            argv.append(item)

    ilines = sys.stdin
    olines = sys.stdout

    if opts['jsoni'] or opts['json']:
        init = lambda: json.loads(ilines.read())
    else:
        init = lambda: json.loads(ilines.read())

    if opts['debug']:
        print(opts, file=sys.stderr)
        print(argv, file=sys.stderr)

    data = main(opts, argv, init)

    if opts['debug']:
        print(type(data), file=sys.stderr)

    text = str() if data is None else str(data)

    if text:
        olines.write(text)
        olines.write('\n')

    olines.flush()
