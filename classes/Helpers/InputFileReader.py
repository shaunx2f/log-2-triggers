def read_log_lines_from_file(file_name):
    fp = open(file_name, 'r', encoding='utf-8')
    while True:
        log_line = fp.readline()
        if not log_line:
            return
        else:
            yield log_line