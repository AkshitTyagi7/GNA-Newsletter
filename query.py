from datetime import timedelta
from aws_keyspace_conn import DataExtraction
from datetime import datetime

date = datetime.now() 
previousDate = date -   timedelta(days=1)
previous_crossBorderDate = previousDate.strftime('20%y-%m-%d')
date = date.strftime('%d-%m-20%y')
previousDate = previousDate.strftime('%d-%m-20%y')
lastYeardate = date.replace('24','23')
previousLastYeardate = previousDate.replace('24','23')

iex_dam_query = f"""select * from gna_database.dam_mrkt_snapshot where date = '{date}' allow filtering"""
iex_lastYear_dam_query = f"""select * from gna_database.dam_mrkt_snapshot where date = '{lastYeardate}' allow filtering"""
hpx_dam_query = f"""select * from gna_database.dam_mrkt_snapshot_hpx where date = '{date}' allow filtering"""
pxil_dam_query = f"""select * from gna_database.dam_mrkt_snapshot_pxil where delivery_date = '{date}' allow filtering"""
iex_gdam_query = f"""select * from gna_database.gdam_mrkt_snapshot where date = '{date}' allow filtering"""
iex_lastYear_gdam_query = f"""select * from gna_database.gdam_mrkt_snapshot where date = '{lastYeardate}' allow filtering"""
hpx_gdam_query = f"""select * from gna_database.gdam_mrkt_snapshot_hpx where date = '{date}' allow filtering"""
pxil_gdam_query = f"""select * from gna_database.gdam_mrkt_snapshot_pxil where delivery_date = '{date}' allow filtering"""
iex_rtm_query = f"""select * from gna_database.rtm_mrkt_snapshot where date = '{previousDate}' allow filtering"""
iex_lastYear_rtm_query = f"""select * from gna_database.rtm_mrkt_snapshot where date = '{previousLastYeardate}' allow filtering"""
hpx_rtm_query = f"""select * from gna_database.rtm_mrkt_snapshot_hpx where date = '{previousDate}' allow filtering"""
pxil_rtm_query = f"""select * from gna_database.rtm_mrkt_snapshot_pxil where delivery_date = '{previousDate}' allow filtering"""

source_wise_query = f"""select * from gna_database.sourcewise_generation where date = '{date}' allow filtering"""
source_wise_previous_query = f"""select * from gna_database.sourcewise_generation where date = '{previousDate}' allow filtering"""

# psp
psp_query = f"""select * from gna_database.psp_report_all_india where date = '{previousDate}'  and regions='TOTAL'  allow filtering"""
psp_previous_query = f"""select * from gna_database.psp_report_all_india where date = '{previousLastYeardate}'  and regions='TOTAL'  allow filtering"""
frequency_query = f"""select * from gna_database.frequency_psp where id = '{previousDate}' allow filtering"""
frequency_previous_query = f"""select * from gna_database.frequency_psp where id = '{previousLastYeardate}' allow filtering"""


# Fossil Fuels 
source_wise_query = f"""select * from gna_database.sourcewise_generation where date = '{previousDate}' and region='All India' allow filtering"""
source_wise_previous_query = f"""select * from gna_database.sourcewise_generation where date = '{previousLastYeardate}' and region='All India' allow filtering"""
psp_report_query = f"""select * from gna_database.psp_report_all_india where date = '{previousDate}' allow filtering"""
psp_report_previous_query = f"""select * from gna_database.psp_report_all_india where date = '{previousLastYeardate}' allow filtering"""

# Cross Border 
cross_border_query = f"""select * from gna_database.transnational_exchanges where date = '{previous_crossBorderDate}' allow filtering"""