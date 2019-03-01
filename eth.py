import dryscrape
import time
from bs4 import BeautifulSoup


def get_coin(coin, cl, nm):

	poloniex_url = "https://poloniex.com/exchange#"

	session = dryscrape.Session()
	session.visit(poloniex_url + coin)

	response = session.body()

	soup = BeautifulSoup(response, features="lxml")

	if cl == "class":
		return soup.find(class_=nm).get_text()


print get_coin("usdt_btc", "class", "info")
