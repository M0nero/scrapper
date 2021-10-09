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
sc.grab("bitcoin", 2)
```

### Usage example:

```json
[{'title': 'Why Bitcoin, Ethereum and Dogecoin Surged This Week', 'paragraph': 'Major coins increased in value this week. ', 'source': 'Decrypt', 'time': 'an 
hour ago'}, {'title': 'Why This Executive Predicted Bitcoin Will Be Legal Tender In 5 Countries By 2022', 'paragraph': 'Bitcoinist has followed closely the rollout of The Bitcoin Law in El Salvador. Via the National Congress, this country gave BTC the status of legal tender, the implications of this action are still under scrutiny but point toward a new phase of adoption for the crypto industry. R...', 'source': 'Bitcoinist.com', 'time': 'an hour ago'}]
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
