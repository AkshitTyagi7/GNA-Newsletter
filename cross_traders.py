from datetime import datetime
from aws_keyspace_conn import DataExtraction
from mail import sendMail
from query import generate_queries
from calculaters import *
import pandas as pd

def sendCrossBorderMail():
    queries = generate_queries()

    cross_border = DataExtraction.execute_query(queries['cross_border_query'])
    
    cross_border_data = calculate_cross_border(cross_border)

    df = pd.DataFrame(cross_border_data)

    # Export to excel with multiple sheets
    df.to_excel('cross_border.xlsx', index=False)

    sendMail('cross_border.xlsx', f'Cross Border Data for Newsletter {datetime.now().strftime("%d-%m-%20%y")}')

if __name__ == '__main__':
    sendCrossBorderMail()
