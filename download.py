from bs4 import BeautifulSoup
import requests
import gzip
from StringIO import StringIO

USHCN_URL = 'http://cdiac.ornl.gov/ftp/ushcn_daily/'


def get_and_parse(url=USHCN_URL):
    r = requests.get(url)
    return BeautifulSoup(r.text, 'html.parser')


def find_all_state_files(html):
    hrefs = [a.get('href') for a in html.find_all('a')]
    return [href for href in hrefs if href.startswith('state')]


def get_filename_from_path(path):
    """Assuming path looks like:
       http://cdiac.ornl.gov/ftp/ushcn_daily/state01_AL.txt.gz
    """
    f = path.split('/')[-1].split('.gz')[0]
    return 'source-data/%s' % f


def unzip_file(content):
    """Build a file-like object with the response so we don't need to do
       uneccessary IO
    """
    zipped_file = StringIO(content)
    return gzip.GzipFile(fileobj=zipped_file)


def download_zipped_files(download_paths):
    unzipped_files = []
    for path in download_paths:
        r = requests.get(path)
        filename = get_filename_from_path(path)
        with open(filename, 'wb') as f:
            f.write(unzip_file(r.content).read())
        unzipped_files.append(filename)

    return unzipped_files


def build_download_paths(href_list, directory_path=USHCN_URL):
    return [directory_path + href for href in href_list]


def main():
    """Download, unzip and save state daily files locally.
    """
    state_daily_files = find_all_state_files(get_and_parse())
    files_to_download = build_download_paths(state_daily_files)
    download_zipped_files(files_to_download)

if __name__ == "__main__":
    main()
