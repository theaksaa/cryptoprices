import dryscrape
import time
from bs4 import BeautifulSoup


def get_coin(coin, cl, nm):

	poloniex_url = "https://poloniex.com/exchange#"

	session = dryscrape.Session()
	session.visit(poloniex_url + coin)

	response = session.body()

	soup = BeautifulSoup(response, features="lxml")

	result = soup.find("div", { cl : nm } )

	return result.find("div", { "class" : "info" } ).get_text()

# lastPrice, change, high, low

print get_coin("usdt_eth", "class", "lastPrice")
print get_coin("usdt_eth", "class", "change")
print get_coin("usdt_eth", "class", "high")
print get_coin("usdt_eth", "class", "low")
