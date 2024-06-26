from datetime import datetime, timedelta
from aws_keyspace_conn import DataExtraction
from mail import sendMail
from query import generate_queries
from calculaters import *
import pandas as pd
from pprint import pprint
def sendMarketSnapshotMail():
    queries = generate_queries()

    # Exchange
    iex_dam = DataExtraction.execute_query(queries['iex_dam_query'])
    hpx_dam = DataExtraction.execute_query(queries['hpx_dam_query'])
    pxil_dam = DataExtraction.execute_query(queries['pxil_dam_query'])
    iex_gdam = DataExtraction.execute_query(queries['iex_gdam_query'])
    hpx_gdam = DataExtraction.execute_query(queries['hpx_gdam_query'])
    pxil_gdam = DataExtraction.execute_query(queries['pxil_gdam_query'])
    iex_rtm = DataExtraction.execute_query(queries['iex_rtm_query'])
    hpx_rtm = DataExtraction.execute_query(queries['hpx_rtm_query'])
    pxil_rtm = DataExtraction.execute_query(queries['pxil_rtm_query'])

    iex_last_year_dam = DataExtraction.execute_query(queries['iex_lastYear_dam_query'])
    iex_last_year_gdam = DataExtraction.execute_query(queries['iex_lastYear_gdam_query'])
    iex_last_year_rtm = DataExtraction.execute_query(queries['iex_lastYear_rtm_query'])

    hpx_last_year_dam = DataExtraction.execute_query(queries['hpx_dam_query'])
    hpx_last_year_gdam = DataExtraction.execute_query(queries['hpx_gdam_query'])
    hpx_last_year_rtm = DataExtraction.execute_query(queries['hpx_rtm_query'])

    pxil_last_year_dam = DataExtraction.execute_query(queries['pxil_lastYear_dam_query'])
    pxil_last_year_gdam = DataExtraction.execute_query(queries['pxil_lastYear_gdam_query'])
    pxil_last_year_rtm = DataExtraction.execute_query(queries['pxil_lastYear_rtm_query'])

    # Cumulative metrics calculations
    iex_dam_cumulative_metrics = calculate_cumulative_metrics_iex_dam(iex_dam)
    hpx_dam_cumulative_metrics = calculate_cumulative_metrics_hpx_dam(hpx_dam)
    pxil_dam_cumulative_metrics = calculate_cumulative_metrics_pxil_dam(pxil_dam)
    iex_gdam_cumulative_metrics = calculate_cumulative_metrics_iex_gdam(iex_gdam)
    hpx_gdam_cumulative_metrics = calculate_cumulative_metrics_hpx_gdam(hpx_gdam)
    pxil_gdam_cumulative_metrics = calculate_cumulative_metrics_pxil_gdam(pxil_gdam)
    iex_rtm_cumulative_metrics = calculate_cumulative_metrics_iex_rtm(iex_rtm)
    hpx_rtm_cumulative_metrics = calculate_cumulative_metrics_hpx_rtm(hpx_rtm)
    pxil_rtm_cumulative_metrics = calculate_cumulative_metrics_pxil_rtm(pxil_rtm)

    iex_dam_lastYear_cumulative_metrics = calculate_cumulative_metrics_iex_dam(iex_last_year_dam)
    iex_gdam_lastYear_cumulative_metrics = calculate_cumulative_metrics_iex_gdam(iex_last_year_gdam)
    iex_rtm_lastYear_cumulative_metrics = calculate_cumulative_metrics_iex_rtm(iex_last_year_rtm)


    hpx_dam_lastYear_cumulative_metrics = calculate_cumulative_metrics_hpx_dam(hpx_last_year_dam)
    hpx_gdam_lastYear_cumulative_metrics = calculate_cumulative_metrics_hpx_gdam(hpx_last_year_gdam)
    hpx_rtm_lastYear_cumulative_metrics = calculate_cumulative_metrics_hpx_rtm(hpx_last_year_rtm)



    pxil_dam_lastYear_cumulative_metrics = calculate_cumulative_metrics_pxil_dam(pxil_last_year_dam)
    pxil_gdam_lastYear_cumulative_metrics = calculate_cumulative_metrics_pxil_gdam(pxil_last_year_gdam)
    pxil_rtm_lastYear_cumulative_metrics = calculate_cumulative_metrics_pxil_rtm(pxil_last_year_rtm)

    print(pxil_dam_cumulative_metrics)

    # Market Snapshots
    items = ['Purchase Bid (MU)', 'Sell Bid (MU)', 'MCV (MU)', 'Avg. MCP (₹/KWh)', 'Wt. Avg. MCP (₹/KWh)']
    iex_dam_values = list(iex_dam_cumulative_metrics.values())[:5]
    hpx_dam_values = list(hpx_dam_cumulative_metrics.values())
    pxil_dam_values = list(pxil_dam_cumulative_metrics.values())
    iex_gdam_values = list(iex_gdam_cumulative_metrics.values())
    hpx_gdam_values = list(hpx_gdam_cumulative_metrics.values())
    pxil_gdam_values = list(pxil_gdam_cumulative_metrics.values())
    iex_rtm_values = list(iex_rtm_cumulative_metrics.values())
    hpx_rtm_values = list(hpx_rtm_cumulative_metrics.values())
    pxil_rtm_values = list(pxil_rtm_cumulative_metrics.values())

    df = pd.DataFrame({'Items': items, 'IEX DAM': iex_dam_values, 'HPX DAM': hpx_dam_values, 'PXIL DAM': pxil_dam_values, 'IEX GDAM': iex_gdam_values, 'HPX GDAM': hpx_gdam_values, 'PXIL GDAM': pxil_gdam_values, 'IEX RTM': iex_rtm_values, 'HPX RTM': hpx_rtm_values, 'PXIL RTM': pxil_rtm_values})
    
    iexDamItems = ["Maximum", "Minimum", "Average"]
    iexPurchaseBid = [iex_dam_cumulative_metrics['Max Purchase Bid (MU)'], iex_dam_cumulative_metrics['Min Purchase Bid (MU)'], iex_dam_cumulative_metrics['Average Purchase Bid (MU)']]
    iexSellBid = [iex_dam_cumulative_metrics['Max Sell Bid (MU)'], iex_dam_cumulative_metrics['Min Sell Bid (MU)'], iex_dam_cumulative_metrics['Average Sell Bid (MU)']]
    iexMCV = [iex_dam_cumulative_metrics['Max MCV (MU)'], iex_dam_cumulative_metrics['Min MCV (MU)'], iex_dam_cumulative_metrics['Average MCV (MU)']]
    iexMCP = [iex_dam_cumulative_metrics['Max MCP (₹/KWh)'], iex_dam_cumulative_metrics['Min MCP (₹/KWh)'], iex_dam_cumulative_metrics['Avg. MCP (₹/KWh)']]

    df2 = pd.DataFrame({'Items': iexDamItems, 'Purchase Bid (MU)': iexPurchaseBid, 'Sell Bid (MU)': iexSellBid, 'MCV (MU)': iexMCV, 'MCP (₹/KWh)': iexMCP})

    iexYearComparison = ["DAM 2024", "DAM 2023", "GDAM 2024", "GDAM 2023", "RTM 2024", "RTM 2023"]
    avgMCP = [iex_dam_cumulative_metrics['Wt. Avg. MCP (₹/KWh)'], iex_dam_lastYear_cumulative_metrics['Wt. Avg. MCP (₹/KWh)'], iex_gdam_cumulative_metrics['Wt. Avg. MCP (₹/KWh)'], iex_gdam_lastYear_cumulative_metrics['Wt. Avg. MCP (₹/KWh)'], iex_rtm_cumulative_metrics['Wt. Avg. MCP (₹/KWh)'], iex_rtm_lastYear_cumulative_metrics['Wt. Avg. MCP (₹/KWh)']]
    df3 = pd.DataFrame({'Items': iexYearComparison, 'Wt. Avg. MCP (₹/KWh)': avgMCP})

    # HPX last year data
    hpxYearComparison = ["DAM 2024", "DAM 2023", "GDAM 2024", "GDAM 2023", "RTM 2024", "RTM 2023"]
    hpx_avgMCP = [hpx_dam_cumulative_metrics['Wt. Avg. MCP (₹/KWh)'], hpx_dam_lastYear_cumulative_metrics['Wt. Avg. MCP (₹/KWh)'], hpx_gdam_cumulative_metrics['Wt. Avg. MCP (₹/KWh)'], hpx_gdam_lastYear_cumulative_metrics['Wt. Avg. MCP (₹/KWh)'], hpx_rtm_cumulative_metrics['Wt. Avg. MCP (₹/KWh)'], hpx_rtm_lastYear_cumulative_metrics['Wt. Avg. MCP (₹/KWh)']]
    df4 = pd.DataFrame({'Items': hpxYearComparison, 'Wt. Avg. MCP (₹/KWh)': hpx_avgMCP})

    # PXIL last year data
    pxilYearComparison = ["DAM 2024", "DAM 2023", "GDAM 2024", "GDAM 2023", "RTM 2024", "RTM 2023"]
    pxil_avgMCP = [pxil_dam_cumulative_metrics['Wt. Avg. MCP (₹/KWh)'], pxil_dam_lastYear_cumulative_metrics['Wt. Avg. MCP (₹/KWh)'], pxil_gdam_cumulative_metrics['Wt. Avg. MCP (₹/KWh)'], pxil_gdam_lastYear_cumulative_metrics['Wt. Avg. MCP (₹/KWh)'], pxil_rtm_cumulative_metrics['Wt. Avg. MCP (₹/KWh)'], pxil_rtm_lastYear_cumulative_metrics['Wt. Avg. MCP (₹/KWh)']]
    df5 = pd.DataFrame({'Items': pxilYearComparison, 'Wt. Avg. MCP (₹/KWh)': pxil_avgMCP})

    # create excel with multiple sheets
    with pd.ExcelWriter('Market_Snapshot.xlsx') as writer:  
        df.to_excel(writer, sheet_name='Market Snapshot', index=False)
        df2.to_excel(writer, sheet_name='IEX DAM', index=False)
        df3.to_excel(writer, sheet_name='IEX Year Comparison', index=False)
        df4.to_excel(writer, sheet_name='HPX Year Comparison', index=False)
        df5.to_excel(writer, sheet_name='PXIL Year Comparison', index=False)

    # sendMail('Market_Snapshot.xlsx', f'Market Snapshot data for Newsletter {datetime.now().strftime("%d-%m-%20%y")}')

if __name__ == '__main__':
    sendMarketSnapshotMail()
