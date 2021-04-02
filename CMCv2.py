from requests import Session
import json
import dateutil.parser
import pytz
import csv
import os


# Dictionary containing keys: Coin TIckers and values: CMC id
with open('cid.csv', mode='r') as coins:
    coin_reader = csv.reader(coins)
    cid = {}
    id_string = []
    for row in coin_reader:
        k, v = row
        cid[k] = v
        id_string.append(v)

id_string = ', '.join(id_string)


# API config
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
PARAMETERS = {'id': str(id_string)}
HEADERS = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': str(os.environ.get('CMC_Secret_Key'))
}


def get_latest_quotes(url, parameters, headers):
    """Request Latest price Quotes from coinmarketcap and returns a json with data from all coins

     url: str: the URL to access Coinmarketcap
     parameters: dict: List of coins for the Api to return
     headers: dict: required info to access api, accept data type and the private key
     """
    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    data = response.json()
    data = json.loads(data)
    return data


def update_price_file(data, cointicker, coinid):
    """Takes the json data downloaded by the previous function and appends them to csv files


        Data: JSON: the downloaded JSON data containing coin data.
        cointicker: dict: A list of dict keys or list containing the ticker symbol for the coins
        you wish to gather data for.
        coinid: dict: the dict key values, or a list containing CMC's coinid for parsing through
        the JSON data.
        """
    # create dict to append into the CSV
    date = data['status']['timestamp']
    date = dateutil.parser.parse(date)
    date = date.astimezone(pytz.timezone("America/Los_Angeles"))
    price = data['data'][str(coinid)]['quote']['USD']['price']
    volume = data['data'][str(coinid)]['quote']['USD']['volume_24h']

    # Make Dict into a CSV, or equivalent for appendage

    # Load old CSV
    filepath = "/CoinData/%s_price.csv"%cointicker
    # Open CSV with CSV Library
    with open(str(filepath), mode='a') as coin_file:
        coin_writer = csv.writer(coin_file, quoting= csv.QUOTE_NONNUMERIC)

        # Append New CSV to old CSV or equivalent
        coin_writer.writerow([date, price, volume])
        # overwrite CSV on file


if __name__ =="__main__":
    pricedata = get_latest_quotes(url, PARAMETERS, HEADERS)

    for key in cid:
        update_price_file(pricedata, key, cid[key])
