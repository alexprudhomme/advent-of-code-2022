def open_file(path):
    with open(path) as f:
        lines = f.readlines()

    return [item.strip() for item in lines]