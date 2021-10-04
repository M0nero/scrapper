# scrapper

## Requirements

Requires `python3` and `beautifulsoup4`, `selenium`, `webdriver-manager`  libraries.

```sh
pip install beautifulsoup4
pip install selenium
pip install webdriver-manager
```
## Installation

### install script

Clone the repository. 

```bash
git clone https://github.com/M0nero/scrapper.git
cd scrapper
```

### edit path in the script

Provide proper path to the file where data will be saved. You need to edit `test.py` file. In my case it is:

```python
sys.path.insert(0, '/Users/gorda/Desktop/PyProjects/scrapper/src')
```


## Usage

```python
# after installing the project and changing path
cd scrapper\test
python test.py
```

## Examples

```python
sc = Scrapper()
sc.grab("bitcoin", 3)
```

### Usage example:

```python
[{'title': "Bitfarms: BITF's Reduced Mining Efficiency And Our Updated Valuation Framework", 'source': 'Seeking Alpha', 'time': '2 hours ago'}, {'title': 'Bitcoin S2F Creator PlanB Thinks BTC Will Reach $135k By December', 'source': 'NewsBTC', 'time': '2 hours ago'}, {'title': 'Bitcoin Surpasses Facebook In Market Capitalization', 'source': 'Bitcoin Magazine', 'time': '2 hours ago'}]
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
