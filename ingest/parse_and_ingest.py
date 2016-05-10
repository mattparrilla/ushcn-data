import glob
from database import ingest_month


# TODO: should get list of text files from download, not by using glob
def get_all_txt_files():
    return glob.glob('./source-data/*.txt')


def parse_line(line):
    """This function is responsible for knowing about the shape of the data
       we get from USHCN and turning it into a list of individual dates.

       see: http://cdiac.ornl.gov/ftp/ushcn_daily/data_format.txt
    """
    year = line[6:10]
    month = line[10:12]
    line_constants = {
        'station_id': int(line[0:6]),
        'metric': line[12:16]
    }

    monthly_readings = []
    for i in range(0, 31):
        entry_index = i * 8 + 16
        entry = line_constants.copy()
        entry['date'] = '%s-%s-%02d' % (year, month, i + 1)
        entry['value'] = int(line[entry_index:(entry_index + 5)])
        entry['m_flag'] = line[entry_index + 5].strip()
        entry['q_flag'] = line[entry_index + 6].strip()
        entry['s_flag'] = line[entry_index + 7].strip()
        monthly_readings.append(entry)

    return monthly_readings


def process_line(line):
    monthly_readings = parse_line(line)
    ingest_month(monthly_readings)


def process_file(path):
    with open(path, 'rb') as f:
        for line in f:
            process_line(line)


def main():
    for txt_file in get_all_txt_files():
        process_file()


if __name__ == '__main__':
    for f in get_all_txt_files():
        process_file(f)
