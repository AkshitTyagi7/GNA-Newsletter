# PSP 
from datetime import timedelta
from aws_keyspace_conn import DataExtraction
from datetime import datetime
from mail import sendMail
from query import *
from calculaters import *
import pandas as pd

def sendPSPMail():
    psp = DataExtraction.execute_query(psp_query)
    psp_previous = DataExtraction.execute_query(psp_previous_query)
    frequency = DataExtraction.execute_query(frequency_query)
    frequency_previous = DataExtraction.execute_query(frequency_previous_query)

    print(psp_query)
    print(frequency_query)

    # Fossil Fuels
    source_wise = DataExtraction.execute_query(source_wise_query)
    source_wise_previous = DataExtraction.execute_query(source_wise_previous_query)
    psp_report = DataExtraction.execute_query(psp_report_query)
    psp_report_previous = DataExtraction.execute_query(psp_report_previous_query)

    # PSP
    pspData = calculate_cumulative_report(psp)
    pspData["Frequency (49.9-50.05)"] = frequency[0].from_49_9_to_50_05
    pspData_previous = calculate_cumulative_report(psp_previous)
    pspData_previous["Frequency (49.9-50.05)"] = frequency_previous[0].from_49_9_to_50_05


    # Fossil Fuels
    psp_data = calculate_cumulative_metrics_psp(psp_report)
    nuclear_res = calculate_cumulative_metrics_source_wise(source_wise)
    # mergring data
    psp_data=nuclear_res
    psp_data_previous = calculate_cumulative_metrics_psp(psp_report_previous)
    nuclear_res_previous = calculate_cumulative_metrics_source_wise(source_wise_previous)
    psp_data_previous=nuclear_res_previous


    df1 = pd.DataFrame([pspData, pspData_previous], index=[date, lastYeardate])
    df2 = pd.DataFrame([psp_data, psp_data_previous])

    # Export to excel with multiple sheets

    with pd.ExcelWriter('psp.xlsx') as writer:
        df1.to_excel(writer, sheet_name='PSP')
        df2.to_excel(writer, sheet_name='Fossil Fuels')

    sendMail('psp.xlsx', f'PSP Data for News Letter {date}')

if __name__ == '__main__':
    sendPSPMail()