# CMCPriceData
This is a quick python script to track coin prices for coins on Coin Market Cap (CMC)

This is a quick python script I made to help me track the prices of various crypto currencies.  My set up is by pluggin into the Coin Market Cap api with a basic user subscription and will gather date, price and volume data for various crypto coins every 5 minutes and save them to specific CSV files pertaining to the coins.  In this guide, I will detail my set up if you wish to gather your own price data. 

STEPS:
1. Set up an API account with coin market cap. 
  - go to https://pro.coinmarketcap.com/login/ and provide your credentials to make an acount.
  - when the account is made, copy the api key.  You can either copy the secret key into your python code, or put it in an environmental variable (recommended method)
  you can get more information about environmental variables via this medium article : https://medium.com/@ksarthak4ever/hiding-passwords-and-secret-keys-in-environment-variables-ccca72a3b01e
  
 2. Gather the coin information from CMC to access coin information with the API.
 - You can find this information by accessing the map in the api via the following link : https://pro-api.coinmarketcap.com/v1/cryptocurrency/map
 the default will give you data for the top 100 coins by marketcap.  I will provide a list of the Top 100 coins.
 
 3. Create a CSV file containing the Coinid and coin ticker symbol.  You can skip this step by removing lines 9 through 19 and putting this information into a dictionary.
 - Make sure that the CSV file is in the same location as the python script.  Make sure there are no headers in the CSV file.  

4. Create a folder called CoinData and create CSV files to store the price data.
- name each CSV file as the ticker symbol as it appears on coinmarketcap followed by price, ex: BTCprice.csv, ETHprice.csv. You can change the name of the files by tweaking line 67. 

5. Create/edit the crontab to activate the script to run to your preference (on MAC/Linux).
- copy the file path where the script is located.
- go into terminal, and type nano crontab -e    (you can use any other editor you wish aside from nano)
-  tweak the tab to run the python file.  If you are new to this, please google how to run cronjobs.  


Please feel free to contact if you have any questions or if there is anything I can clarify.  

Thanks

