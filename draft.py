# from datetime import date
#
# date_test = [2023, 6, 30]
# print(date(date_test))
from pathlib import Path

p = Path('migrations')
print([x for x in p.iterdir()])
