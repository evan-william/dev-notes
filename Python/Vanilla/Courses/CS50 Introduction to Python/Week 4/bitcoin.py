import sys
import requests
import json

try:
    btcamount = 0
    getdata = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    rawdata = getdata.json()

    btcamount = float(rawdata["data"]["priceUsd"]) # This doesn't work like API Apple Tunes because one is list and other is dict (WELL KINDA LIKE THAT)
                       # ["data"] and ["priceUsd"] is str so must be changed to float first

except requests.RequestException as errormsg:
    print(f"General error: {errormsg}")


if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    btc_amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a valid number")


btcamount = btcamount * float(sys.argv[1])
#print(f"${btcamount:.4f}")
print(f"${btcamount:,.4f}")




