import sys
sys.path.insert(0, '/Users/gorda/Desktop/PyProjects/scrapper/src')
from scrapper import Scrapper

sc = Scrapper()
print(sc.grab("bitcoin", 6))
