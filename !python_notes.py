"""Python Notes"""
import pandas as pd
import numpy as np

"""Table of Contents"""

# TODO:     Dictionary
# TODO:     pd.Timestamp vs. datetime.date
# TODO:     System notice/tracker


# TODO:     Dictionary
sales_dict = { 'apple': 2, 'orange': 3, 'grapes': 4 }

""" .pop() """
#removes and returns an element
aaple_empty_d = sales_dict.pop('aaple_large', {})
aaple_d = sales_dict.pop('apple')


# TODO:     System notice/tracker
""" logging.getLogger(__name__) """
# Logs a message with level INFO on the root logger.
import logging
log = logging.getLogger(__name__)
log.info('process started...\n')
log.warning('Did not pass pre-condition checks!')

pd.set_option('display.width', 250)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 100)


""" print with variables"""
name1='john'
name2='mike'
print("Hello %s, my name is %s" % (name1, name2))


# TODO:     pd.Timestamp vs. datetime.date
from datetime import date
today_1=pd.Timestamp('today')
today_2=date.today()
# convert datetime.date -> pd.Timestamp
today_3=pd.Timestamp(today_2)