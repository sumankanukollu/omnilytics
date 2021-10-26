import string
import random
import re
from pathlib import Path

from django.conf import settings #MEDIA_ROOT,MEDIA_URL


class Generate(object):
    def __init__(self, n=10):
        self.n = n
        self.filename = Path.cwd()/'omni_log_2.txt'
        # self.filename = settings.MEDIA_ROOT / 'logs' / 'omni_log_2.txt'
        # if not Path(Path.cwd() / self.file_name).exists():
        self.f = open(self.filename, 'w+')

    # 1. Real number generation:
    def realNum(self):
        return random.random()

    # 2. Integare Generation:
    def integer(self):
        return ''.join(random.choices(string.digits, k=self.n))

    # 3. Alabhabet Generation:
    def alphabets(self):
        return ''.join(random.choices(string.ascii_letters, k=self.n))

    # 4. Alpha numeric Generation:
    def alphanum(self):
        return ''.join(random.choices(string.ascii_letters+string.digits, k=self.n))

    # 5. Write content to a file:
    def dump_generated_data(self):
        initial = []
        i = 100
        for _ in range(i):
            initial.append(self.integer())
            initial.append(str(self.realNum()))
            initial.append(self.alphabets())
            initial.append(self.alphanum())
            self.f.write(','.join(initial))
        file_sz = self.filename.stat().st_size
        if file_sz < 2100000:
            self.dump_generated_data()
        else:
            print(f'### File size is : {file_sz//1e+6} MB')
            self.f.close()
        return self.filename


class Analyze_Report(object):
    def __init__(self, filename=Path.cwd()/'omni_log_2.txt'):
        self.filename = filename
        with open(self.filename, 'r') as f:
            self.data = f.read()

    def analyze(self):
        import pdb
        data_split = self.data.split(',')
        self.integers = len([x for x in data_split if x.isnumeric()])
        self.alnum = len([x for x in data_split if x.isalnum()])
        self.real_nums = len(re.findall(r'\d+\.\d+', self.data))
        self.alphabets_2 = len(re.findall(r"\,[a-zA-Z]+\,", self.data))

        analyze_dict = {'int': self.integers, 'alnum': self.alnum,
                        'realnum': self.real_nums, 'alpha': self.alphabets_2}
        print(f"### Integers : {analyze_dict['int']}\n### real numbers : {analyze_dict['realnum']}\n### Alpha Numeric  : {analyze_dict['alnum']}\n### Alphabets count : {analyze_dict['alpha']}")
        return analyze_dict


if __name__ == '__main__':
    Generate().dump_generated_data()
    Analyze_Report().analyze()
