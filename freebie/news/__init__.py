import os
import pandas as pd

_this_folder = os.path.abspath(os.path.dirname(__file__))
DEFAULT_RSS_PATH = os.path.join(_this_folder, 'rss_feeds.csv')
DEFAULT_WEBSOURCES_PATH = os.path.join(_this_folder, 'websources.csv')
RSS_PATH = os.environ.get('FREEBIE_RSS', DEFAULT_RSS_PATH)
WEBSOURCES_PATH = os.environ.get('FREEBIE_WEBSOURCES', DEFAULT_WEBSOURCES_PATH)

# RSS = pd.read_csv(RSS_PATH)
WEBSOURCES = pd.read_csv(WEBSOURCES_PATH)
