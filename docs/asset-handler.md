# asset-handler

class responsible for managing specific assets

## load asset list

reads list of ticker symbols to watch from assets.csv file

## filter assets

iterate list of assets
get state of asset
lock assets which do not meet watch criteria
periodically unlock and rescan assets
