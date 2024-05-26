from datetime import timedelta
from aws_keyspace_conn import DataExtraction
from datetime import datetime
from mail import sendMail
from query import *
from calculaters import *
import pandas as pd

def sendCrossBorderMail():
    cross_border = DataExtraction.execute_query(cross_border_query)
    
    cross_border_data = calculate_cross_border(cross_border)

    df = pd.DataFrame(cross_border_data)

    # Export to excel with multiple sheets

    df.to_excel('cross_border.xlsx', index=False)       

    sendMail('cross_border.xlsx', f'Cross Border Data for Newsletter {previous_crossBorderDate}')