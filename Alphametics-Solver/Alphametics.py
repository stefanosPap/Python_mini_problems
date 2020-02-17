def alphametics(puzzle):
    splitted = puzzle
    splitted = splitted.split("=")
    splitted[0] = splitted[0].split("+")
    unique = sorted(set(str(splitted)))
    unique.remove('[')
    unique.remove(']')
    unique.remove(',')
    unique.remove("'")
    unique.remove(' ')
    print(unique)
    print(puzzle)
    print(splitted)
alphametics("SEND + MORE = MONEY")