# encoding: utf-8

# This code is free, THANK YOU!
# It is explained at the guide you can find at www.theincompleteguide.com
# You will also find improvement ideas and explanations

import config
from asset_handler import AssetHandler
import logging
from multi_handler import MultiHandler
import os
from shared import *
from stock import *
from trader import *
from datetime import datetime
import threading

# Global object we log to; the handler will work with any log message
_L = logging.getLogger("demo")

def clean_open_orders(api):
    # First, cancel any existing orders so they don't impact our buying power.
    orders = api.list_orders(status="open")

    print('\nCLEAR ORDERS')
    print('%i orders were found open' % int(len(orders)))

    for order in orders:
      api.cancel_order(order.id)

def check_account_ok(api):

    account = api.get_account()
    if account.account_blocked or account.trading_blocked or account.transfers_blocked:

        print('OJO, account blocked. WTF?')
        import pdb; pdb.set_trace()

def create_log_folder(path):

    # create the files folder in case it does not exist
    if not os.path.exists(config.FILES_FOLDER):
        os.mkdir(config.FILES_FOLDER)

    if not os.path.exists(config.LOGS_PATH):
        os.mkdir(config.LOGS_PATH)

    folderName = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = path  + folderName + '/'

    if not os.path.exists(path):
        os.mkdir(path)

    return path

def run_tbot(_L,assetHandler,account):

    # initialize trader object
    trader = Trader(config.APCA_API_KEY_ID, config.APCA_API_SECRET_KEY, _L, account)

    while True:

        ticker = assetHandler.find_target_asset()
        stock = Stock(ticker)

        ticker,lock = trader.run(stock) # run the trading program

        if lock: # if the trend is not favorable, lock it temporarily
            assetHandler.lock_asset(ticker)
        else:
            assetHandler.make_asset_available(ticker)

def main():
    # Set up a basic stderr logging; this is nothing fancy.
    log_format = '%(asctime)s %(threadName)12s: %(lineno)-4d %(message)s'
    stderr_handler = logging.StreamHandler()
    stderr_handler.setFormatter(logging.Formatter(log_format))
    logging.getLogger().addHandler(stderr_handler)

    # Set up a logger that creates one file per thread
    todayLogsPath = create_log_folder(config.LOGS_PATH)
    multi_handler = MultiHandler(todayLogsPath)
    multi_handler.setFormatter(logging.Formatter(log_format))
    logging.getLogger().addHandler(multi_handler)

    # Set default log level, log a message
    _L.setLevel(logging.DEBUG)
    _L.info("\n\n\nRun initiated")
    _L.info('Max workers allowed: ' + str(config.MAX_WORKERS))

    # initialize the API with Alpaca
    api = tradeapi.REST(config.APCA_API_KEY_ID, config.APCA_API_SECRET_KEY, config.APCA_API_ENDPOINT, api_version='v2')

    # initialize the asset handler
    assetHandler = AssetHandler()

    # get the Alpaca account ready
    try:
        _L.info("Getting account")
        check_account_ok(api) # check if it is ok to trade
        account = api.get_account()
        clean_open_orders(api) # clean all the open orders
        _L.info("Got it")

        for thread in range(config.MAX_WORKERS): # this will launch the threads
            worker = 'th' + str(thread) # establishing each worker name

            worker = threading.Thread(name=worker,target=run_tbot,args=(_L, assetHandler, account))
            worker.start() # it runs a run_tbot function, declared here as well

            time.sleep(1)

    except Exception as e:
        _L.info(str(e))

if __name__ == '__main__':
    main()
