import sqlite3
import glob


def get_all_txt_files():
    return glob.glob('./source-data/*.txt')


def parse_line(line):
    """This function is responsible for knowing what characters mean what
       in the input line and returning a list of readings.

       see: http://cdiac.ornl.gov/ftp/ushcn_daily/data_format.txt
    """
    year = line[6:10]
    month = line[10:12]
    element = line[12:16].lower()
    line_constants = {
        'coop_id': line[0:6]
    }

    monthly_readings = []
    for i in range(0, 31):
        entry_begin_point = i * 8 + 16
        entry = dict(line_constants)
        entry['date'] = '%s-%s-%02d' % (year, month, i + 1)
        entry[element] = line[entry_begin_point:(entry_begin_point + 5)]
        entry['%s_m_flag'] = line[entry_begin_point + 5]
        entry['%s_q_flag'] = line[entry_begin_point + 6]
        entry['%s_s_flag'] = line[entry_begin_point + 7]
        monthly_readings.append(entry)

    return monthly_readings


def add_entry_to_db(line_values):
    # TODO
    return False


def process_line(line):
    monthly_readings = parse_line(line)
    for reading in monthly_readings:
        print reading
        add_entry_to_db(reading)


def process_file(path):
    with open(path, 'rb') as f:
        for line in f:
            process_line(line)


def main():
    for txt_file in get_all_txt_files():
        process_file()


if __name__ == '__main__':
    process_file(get_all_txt_files()[0])
