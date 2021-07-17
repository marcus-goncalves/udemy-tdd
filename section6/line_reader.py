def read_from_file(filename: str) -> str:
    infile = open(filename, 'r')
    line = infile.readline()
    return line
