def get_id(names, name):
    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    elif not name.isalpha() or name != name.capitalize():
        raise ValueError('Имя не является корректным')
    else:
        names.append(name)
        return len(names)
