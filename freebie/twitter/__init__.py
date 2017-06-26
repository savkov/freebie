import os
import pandas as pd

_this_folder = os.path.abspath(os.path.dirname(__file__))
DEFAULT_HANDLES_PATH = os.path.join(_this_folder, 'twitter_handles.csv')
HANDLES_PATH = os.environ.get('FREEBIE_TWITTER_HANDLES', DEFAULT_HANDLES_PATH)

HANDLES = pd.read_csv(HANDLES_PATH)
