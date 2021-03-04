
#print('t.bone: kosh kelinizder')

def _get(*args, **kwargs):
    if not args:
        raise KeyError()

    def func(data):
        copy = {}
        for key in args:
            copy[key] = data[key]

        return copy

    return func


def _set(*args, **kwargs):
    if args:
        raise KeyError()

    if not kwargs:
        raise ValueError()

    def func(data):
        for key in kwargs:
            data[key] = kwargs[key]

        return data

    return func


def _del(*args, **kwargs):
    if not args:
        raise KeyError()

    def func(data):
        for key in args:
            if key in data:
                del data[key]

        return data

    return func


def _wrap(*args, **kwargs):
    if not args:
        raise KeyError()

    def func(data):
        copy = {}

        for key in args:
            copy[key] = data

        return copy

    return func


vtbl = {
    'set': _set,
    'del': _del,
    'get': _get,
    'wrap': _wrap,
}


def hint(name):
    raise NotImplementedError(name)


def bone(opts, argv, init):
    if opts['colon']:
        delim = ':'
    else:
        delim = '/'

    pipe = ' '.join(argv).split(delim)

    data = None
    for part in pipe:
        elem = part.split()

        if not elem:
            continue

        name = elem.pop(0)

        args, kwargs = [], {}
        for item in elem:
            key, delim, value = item.partition('=')
            if delim:
                kwargs[key] = value
            else:
                args.append(item)

        if data is None:
            data = init()

        func = vtbl.get(name, lambda *_, **__: hint(name))(*args, **kwargs)

        data = func(data)

        if data is None:
            break

    return data
