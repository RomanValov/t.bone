
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


def bone(opts, argv, init):
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
