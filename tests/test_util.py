import os

from freebie.util import read_csv


def test_read_csv(dummie_csv):
    fp = 'test_temp_file.csv'
    with open(fp, 'w') as fh:
        fh.write(dummie_csv)
    print(fp)
    csv = read_csv(fp)
    print(csv)
    assert len(csv) == 2
    assert len(csv[0].keys()) == 3
    os.remove(fp)


def test_read_csv_with_header(dummie_csv):
    fp = 'test_temp_file.csv'
    with open(fp, 'w') as fh:
        fh.write(dummie_csv)
    csv = read_csv(fp, header=['head1', 'head2', 'head3'])
    assert len(csv) == 3
    assert len(csv[0].keys()) == 3
    assert csv[0]['head1']
    os.remove(fp)
