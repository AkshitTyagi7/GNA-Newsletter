from datetime import timedelta, datetime

def generate_queries():
    date = datetime.now()
    previousDate = date - timedelta(days=1)
    previous_crossBorderDate = previousDate.strftime('20%y-%m-%d')
    date_str = date.strftime('%d-%m-20%y')
    previousDate_str = previousDate.strftime('%d-%m-20%y')
    lastYeardate = date_str.replace('24','23')

    previousLastYeardate = previousDate_str.replace('24','23')
    print(lastYeardate)

    queries = {
        'iex_dam_query': f"""select * from gna_database.dam_mrkt_snapshot where date = '{date_str}' allow filtering""",
        'iex_lastYear_dam_query': f"""select * from gna_database.dam_mrkt_snapshot where date = '{lastYeardate}' allow filtering""",
        'hpx_dam_query': f"""select * from gna_database.dam_mrkt_snapshot_hpx where date = '{date_str}' allow filtering""",
        'hpx_lastYear_dam_query': f"""select * from gna_database.dam_mrkt_snapshot_hpx where date = '{lastYeardate}' allow filtering""",
        'pxil_dam_query': f"""select * from gna_database.dam_mrkt_snapshot_pxil where delivery_date = '{date_str}' allow filtering""",
        'pxil_lastYear_dam_query': f"""select * from gna_database.dam_mrkt_snapshot_pxil where delivery_date = '{lastYeardate}' allow filtering""",
        'iex_gdam_query': f"""select * from gna_database.gdam_mrkt_snapshot where date = '{date_str}' allow filtering""",
        'iex_lastYear_gdam_query': f"""select * from gna_database.gdam_mrkt_snapshot where date = '{lastYeardate}' allow filtering""",
        'hpx_gdam_query': f"""select * from gna_database.gdam_mrkt_snapshot_hpx where date = '{date_str}' allow filtering""",
        'hpx_lastYear_gdam_query': f"select * from gna_database.gdam_mrkt_snapshot_hpx where date = '{lastYeardate}' allow filtering",
        'pxil_gdam_query': f"""select * from gna_database.gdam_mrkt_snapshot_pxil where delivery_date = '{date_str}' allow filtering""",
        'pxil_lastYear_gdam_query': f"""select * from gna_database.gdam_mrkt_snapshot_pxil where delivery_date = '{lastYeardate}' allow filtering""",
        'iex_rtm_query': f"""select * from gna_database.rtm_mrkt_snapshot where date = '{previousDate_str}' allow filtering""",
        'iex_lastYear_rtm_query': f"""select * from gna_database.rtm_mrkt_snapshot where date = '{previousLastYeardate}' allow filtering""",
        'hpx_rtm_query': f"""select * from gna_database.rtm_mrkt_snapshot_hpx where date = '{previousDate_str}' allow filtering""",
        'hpx_lastYear_rtm_query': f"""select * from gna_database.rtm_mrkt_snapshot_hpx where date = '{previousLastYeardate}' allow filtering""",
        'pxil_rtm_query': f"""select * from gna_database.rtm_mrkt_snapshot_pxil where delivery_date = '{previousDate_str}' allow filtering""",
        'pxil_lastYear_rtm_query': f"""select * from gna_database.rtm_mrkt_snapshot_pxil where delivery_date = '{previousLastYeardate}' allow filtering""",
        'source_wise_query': f"""select * from gna_database.sourcewise_generation where date = '{date_str}' allow filtering""",
        'source_wise_previous_query': f"""select * from gna_database.sourcewise_generation where date = '{previousDate_str}' allow filtering""",
        'psp_query': f"""select * from gna_database.psp_report_all_india where date = '{date_str}' and regions='TOTAL' allow filtering""",
        'psp_previous_query': f"""select * from gna_database.psp_report_all_india where date = '{lastYeardate}' and regions='TOTAL' allow filtering""",
        'frequency_query': f"""select * from gna_database.frequency_psp where id = '{date_str}' allow filtering""",
        'frequency_previous_query': f"""select * from gna_database.frequency_psp where id = '{lastYeardate}' allow filtering""",
        'psp_report_query': f"""select * from gna_database.psp_report_all_india where date = '{date_str}' allow filtering""",
        'psp_report_previous_query': f"""select * from gna_database.psp_report_all_india where date = '{lastYeardate}' allow filtering""",
        'cross_border_query': f"""select * from gna_database.transnational_exchanges where date = '{date_str}' allow filtering"""
    }

    return queries
