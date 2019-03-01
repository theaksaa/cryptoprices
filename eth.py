import dryscrape
import time
from bs4 import BeautifulSoup


def get_coin(coin, option):

	poloniex_url = "https://poloniex.com/exchange#"

	session = dryscrape.Session()
	session.visit(poloniex_url + coin)

	response = session.body()

	soup = BeautifulSoup(response, features="lxml")

	lp = soup.find("div", { "class" : "lastPrice" }).find("div", { "class" : "info" }).get_text()
	ch = soup.find("div", { "class" : "change" }).find("div", { "class" : "info" }).get_text()
	hg = soup.find("div", { "class" : "high" }).find("div", { "class" : "info" }).get_text()
	lw = soup.find("div", { "class" : "low" }).find("div", { "class" : "info" }).get_text()

	if option == "lastPrice":
		return lp
	elif option == "change":
		return ch
	elif option == "high":
		return hg
	elif option == "low":
		return lw
	elif option == "all":
		print lp, ch, hg, lw
	else: return "Error"

# lastPrice, change, high, low
print get_coin("usdt_eth", "lastPrice")
