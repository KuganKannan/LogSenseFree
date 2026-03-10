def read_log_file(path):

    with open(path, "r", encoding="utf-8") as file:

        for line in file:
            yield line.strip()