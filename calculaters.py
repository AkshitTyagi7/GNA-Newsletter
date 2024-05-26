from decimal import Decimal


def calculate_cumulative_metrics_iex_dam(rows):
    # Initialize cumulative variables
    purchase_bid_total = Decimal('0')
    sell_bid_total = Decimal('0')
    mcv_total = Decimal('0')
    mcp_sum = Decimal('0')
    weighted_mcp_sum = Decimal('0')
    max_pur_bid = Decimal('0')
    min_pur_bid = Decimal('999999999999999')
    average_pur_bid = Decimal('0')
    max_sell_bid = Decimal('0')
    min_sell_bid = Decimal('999999999999999')
    average_sell_bid = Decimal('0')
    max_mcv = Decimal('0')
    min_mcv = Decimal('999999999999999')
    average_mcv = Decimal('0')
    max_mcp = Decimal('0')
    min_mcp = Decimal('999999999999999')
    average_mcp = Decimal('0')
    total_records = len(rows)

    # Iterate through rows to calculate cumulative values
    for row in rows:
        prchs_bid_mw = Decimal(row.prchs_bid_mw) if row.prchs_bid_mw else Decimal('0')
        sell_bid_mw = Decimal(row.sell_bid_mw) if row.sell_bid_mw else Decimal('0')
        mcv_mw = Decimal(row.mcv_mw) if row.mcv_mw else Decimal('0')
        mcp_rs_mwh = Decimal(row.mcp_rs_mwh) if row.mcp_rs_mwh else Decimal('0')
        wt_mcp_rs_mwh = Decimal(row.wt_mcp_rs_mwh) if row.wt_mcp_rs_mwh else Decimal('0')

        purchase_bid_total += prchs_bid_mw
        sell_bid_total += sell_bid_mw
        mcv_total += mcv_mw
        mcp_sum += mcp_rs_mwh
        weighted_mcp_sum += (wt_mcp_rs_mwh * mcv_mw)/1000  # Calculate weighted sum of MCP

        if prchs_bid_mw > max_pur_bid:
            max_pur_bid = prchs_bid_mw
        if prchs_bid_mw < min_pur_bid:
            min_pur_bid = prchs_bid_mw

        if sell_bid_mw > max_sell_bid:
            max_sell_bid = sell_bid_mw
        if sell_bid_mw < min_sell_bid:
            min_sell_bid = sell_bid_mw
        
        if mcv_mw > max_mcv:
            max_mcv = mcv_mw
        if mcv_mw < min_mcv:
            min_mcv = mcv_mw
        
        if mcp_rs_mwh > max_mcp:
            max_mcp = mcp_rs_mwh
        if mcp_rs_mwh < min_mcp:
            min_mcp = mcp_rs_mwh

        
    if total_records > 0:
        average_pur_bid = purchase_bid_total / total_records
        average_sell_bid = sell_bid_total / total_records
        average_mcv = mcv_total / total_records


    # Calculate averages
    if total_records > 0:
        avg_mcp = mcp_sum / total_records
        if mcv_total > 0:
            wt_avg_mcp = weighted_mcp_sum / mcv_total
        else:
            wt_avg_mcp = Decimal('0')
    else:
        avg_mcp = Decimal('0')
        wt_avg_mcp = Decimal('0')

    # Return the cumulative metrics as a dictionary
    return {
        'Purchase Bid (MU)': purchase_bid_total/4,
        'Sell Bid (MU)': sell_bid_total/4,
        'MCV (MU)': mcv_total/4,
        'Avg. MCP (₹/KWh)': avg_mcp/1000,
        'Wt. Avg. MCP (₹/KWh)': wt_avg_mcp,
        'Max Purchase Bid (MU)': max_pur_bid,
        'Min Purchase Bid (MU)': min_pur_bid,
        'Average Purchase Bid (MU)': average_pur_bid,
        'Max Sell Bid (MU)': max_sell_bid,
        'Min Sell Bid (MU)': min_sell_bid,
        'Average Sell Bid (MU)': average_sell_bid,
        'Max MCV (MU)': max_mcv,
        'Min MCV (MU)': min_mcv,
        'Average MCV (MU)': average_mcv,
        'Max MCP (₹/KWh)': max_mcp,
        'Min MCP (₹/KWh)': min_mcp,
    }


def calculate_cumulative_metrics_hpx_dam(rows):
    # Initialize cumulative variables
    purchase_bid_total = Decimal('0')
    sell_bid_total = Decimal('0')
    mcv_total = Decimal('0')
    mcp_sum = Decimal('0')
    weighted_mcp_sum = Decimal('0')
    total_records = len(rows)

    # Iterate through rows to calculate cumulative values
    for row in rows:
        prchs_bid_mw = Decimal(row.purchase_bid_mw) if row.purchase_bid_mw else Decimal('0')
        sell_bid_mw = Decimal(row.sell_bid_mw) if row.sell_bid_mw else Decimal('0')
        mcv_mw = Decimal(row.mcv_mw) if row.mcv_mw else Decimal('0')
        mcp_rs_mwh = Decimal(row.mcp_rs_mwh) if row.mcp_rs_mwh else Decimal('0')
        wt_mcp_rs_mwh = Decimal(row.mcp_rs_mwh) if row.mcp_rs_mwh else Decimal('0')

        purchase_bid_total += prchs_bid_mw
        sell_bid_total += sell_bid_mw
        mcv_total += mcv_mw
        mcp_sum += mcp_rs_mwh
        weighted_mcp_sum += (wt_mcp_rs_mwh * mcv_mw)/1000  # Calculate weighted sum of MCP

    # Calculate averages
    if total_records > 0:
        avg_mcp = mcp_sum / total_records
        if mcv_total > 0:
            wt_avg_mcp = weighted_mcp_sum / mcv_total
        else:
            wt_avg_mcp = Decimal('0')
    else:
        avg_mcp = Decimal('0')
        wt_avg_mcp = Decimal('0')

    # Return the cumulative metrics as a dictionary
    return {
        'Purchase Bid (MU)': purchase_bid_total/4,
        'Sell Bid (MU)': sell_bid_total/4,
        'MCV (MU)': mcv_total/4,
        'Avg. MCP (₹/KWh)': avg_mcp/1000,
        'Wt. Avg. MCP (₹/KWh)': wt_avg_mcp
    }

def calculate_cumulative_metrics_pxil_dam(rows):
    # Initialize cumulative variables
    purchase_bid_total = Decimal('0')
    sell_bid_total = Decimal('0')
    mcv_total = Decimal('0')
    mcp_sum = Decimal('0')
    weighted_mcp_sum = Decimal('0')
    total_records = len(rows)

    # Iterate through rows to calculate cumulative values
    for row in rows:
        prchs_bid_mw = Decimal(row.buy_bid_mwh) if row.buy_bid_mwh != "-" else Decimal('0')
        sell_bid_mw = Decimal(row.sell_bid_mwh) if row.sell_bid_mwh != "-" else Decimal('0')
        mcv_mw = Decimal(row.mcv_mwh) if row.mcv_mwh != "-" else Decimal('0')
        mcp_rs_mwh = Decimal(row.unconstraint_mcp_inr_mwh) if row.unconstraint_mcp_inr_mwh != "-" else Decimal('0')
        wt_mcp_rs_mwh = Decimal(row.unconstraint_mcp_inr_mwh) if row.unconstraint_mcp_inr_mwh != "-" else Decimal('0')

        purchase_bid_total += prchs_bid_mw
        sell_bid_total += sell_bid_mw
        mcv_total += mcv_mw
        mcp_sum += mcp_rs_mwh
        weighted_mcp_sum += (wt_mcp_rs_mwh * mcv_mw)/1000  # Calculate weighted sum of MCP

    # Calculate averages
    if total_records > 0:
        avg_mcp = mcp_sum / total_records
        if mcv_total > 0:
            wt_avg_mcp = weighted_mcp_sum / mcv_total
        else:
            wt_avg_mcp = Decimal('0')
    else:
        avg_mcp = Decimal('0')
        wt_avg_mcp = Decimal('0')

    # Return the cumulative metrics as a dictionary
    return {
        'Purchase Bid (MU)': purchase_bid_total,
        'Sell Bid (MU)': sell_bid_total,
        'MCV (MU)': mcv_total/4,
        'Avg. MCP (₹/KWh)': avg_mcp/1000,
        'Wt. Avg. MCP (₹/KWh)': wt_avg_mcp
    }


def calculate_cumulative_metrics_iex_gdam(rows):
    # Initialize cumulative variables
    purchase_bid_total = Decimal('0')
    sell_bid_total = Decimal('0')
    mcv_total = Decimal('0')
    mcp_sum = Decimal('0')
    weighted_mcp_sum = Decimal('0')
    total_records = len(rows)

    # Iterate through rows to calculate cumulative values
    for row in rows:
        prchs_bid_mw = Decimal(row.prchs_bid_mw) if row.prchs_bid_mw else Decimal('0')
        sell_bid_mw = Decimal(row.sell_bid_tot_mw) if row.sell_bid_tot_mw else Decimal('0')
        mcv_mw = Decimal(row.mcv_tot_mw) if row.mcv_tot_mw else Decimal('0')
        mcp_rs_mwh = Decimal(row.mcp_rs_mwh) if row.mcp_rs_mwh else Decimal('0')
        wt_mcp_rs_mwh = Decimal(row.wt_mcp_rs_mwh) if row.wt_mcp_rs_mwh else Decimal('0')

        purchase_bid_total += prchs_bid_mw
        sell_bid_total += sell_bid_mw
        mcv_total += mcv_mw
        mcp_sum += mcp_rs_mwh
        weighted_mcp_sum += (wt_mcp_rs_mwh * mcv_mw)/1000  # Calculate weighted sum of MCP

    # Calculate averages
    if total_records > 0:
        avg_mcp = mcp_sum / total_records
        if mcv_total > 0:
            wt_avg_mcp = weighted_mcp_sum / mcv_total
        else:
            wt_avg_mcp = Decimal('0')
    else:
        avg_mcp = Decimal('0')
        wt_avg_mcp = Decimal('0')

    # Return the cumulative metrics as a dictionary
    return {
        'Purchase Bid (MU)': purchase_bid_total/4,
        'Sell Bid (MU)': sell_bid_total/4,
        'MCV (MU)': mcv_total/4,
        'Avg. MCP (₹/KWh)': avg_mcp/1000,
        'Wt. Avg. MCP (₹/KWh)': wt_avg_mcp
    }

def calculate_cumulative_metrics_hpx_gdam(rows):
    # Initialize cumulative variables
    purchase_bid_total = Decimal('0')
    sell_bid_total = Decimal('0')
    mcv_total = Decimal('0')
    mcp_sum = Decimal('0')
    weighted_mcp_sum = Decimal('0')
    total_records = len(rows)

    # Iterate through rows to calculate cumulative values
    for row in rows:
        prchs_bid_mw = Decimal(row.purchase_bid) if row.purchase_bid else Decimal('0')
        sell_bid_mw = Decimal(row.mw_total) if row.mw_total else Decimal('0')
        mcv_mw = Decimal(row.mcv_total) if row.mcv_total else Decimal('0')
        mcp_rs_mwh = Decimal(row.mcp) if row.mcp else Decimal('0')
        wt_mcp_rs_mwh = Decimal(row.mcp) if row.mcp else Decimal('0')

        purchase_bid_total += prchs_bid_mw
        sell_bid_total += sell_bid_mw
        mcv_total += mcv_mw
        mcp_sum += mcp_rs_mwh
        weighted_mcp_sum += (wt_mcp_rs_mwh * mcv_mw)/1000  # Calculate weighted sum of MCP

    # Calculate averages
    if total_records > 0:
        avg_mcp = mcp_sum / total_records
        if mcv_total > 0:
            wt_avg_mcp = weighted_mcp_sum / mcv_total
        else:
            wt_avg_mcp = Decimal('0')
    else:
        avg_mcp = Decimal('0')
        wt_avg_mcp = Decimal('0')

    # Return the cumulative metrics as a dictionary
    return {
        'Purchase Bid (MU)': purchase_bid_total/4,
        'Sell Bid (MU)': sell_bid_total/4,
        'MCV (MU)': mcv_total/4,
        'Avg. MCP (₹/KWh)': avg_mcp/1000,
        'Wt. Avg. MCP (₹/KWh)': wt_avg_mcp
    }

def calculate_cumulative_metrics_pxil_gdam(rows):
    # Initialize cumulative variables
    purchase_bid_total = Decimal('0')
    sell_bid_total = Decimal('0')
    mcv_total = Decimal('0')
    mcp_sum = Decimal('0')
    weighted_mcp_sum = Decimal('0')
    total_records = len(rows)

    # Iterate through rows to calculate cumulative values
    for row in rows:
        prchs_bid_mw = Decimal(row.buy_bid_mwh) if row.buy_bid_mwh != "-"  else Decimal('0')
        sell_bid_mw = Decimal(row.sell_bid_mwh) if row.sell_bid_mwh != "-"  else Decimal('0')
        mcv_mw = Decimal(row.mcv_mwh) if row.mcv_mwh != "-"  else Decimal('0')
        mcp_rs_mwh = Decimal(row.unconstraint_mcp_inr_mwh)  if row.unconstraint_mcp_inr_mwh != "-"  else Decimal('0')
        wt_mcp_rs_mwh = Decimal(row.unconstraint_mcp_inr_mwh) if row.unconstraint_mcp_inr_mwh != "-"  else Decimal('0')

        purchase_bid_total += prchs_bid_mw
        sell_bid_total += sell_bid_mw
        mcv_total += mcv_mw
        mcp_sum += mcp_rs_mwh
        weighted_mcp_sum += (wt_mcp_rs_mwh * mcv_mw)/1000  # Calculate weighted sum of MCP

    # Calculate averages
    if total_records > 0:
        avg_mcp = mcp_sum / total_records
        if mcv_total > 0:
            wt_avg_mcp = weighted_mcp_sum / mcv_total
        else:
            wt_avg_mcp = Decimal('0')
    else:
        avg_mcp = Decimal('0')
        wt_avg_mcp = Decimal('0')

    # Return the cumulative metrics as a dictionary
    return {
        'Purchase Bid (MU)': purchase_bid_total/4,
        'Sell Bid (MU)': sell_bid_total/4,
        'MCV (MU)': mcv_total/4,
        'Avg. MCP (₹/KWh)': avg_mcp/1000,
        'Wt. Avg. MCP (₹/KWh)': wt_avg_mcp
    }

def calculate_cumulative_metrics_iex_rtm(rows):
    # Initialize cumulative variables
    purchase_bid_total = Decimal('0')
    sell_bid_total = Decimal('0')
    mcv_total = Decimal('0')
    mcp_sum = Decimal('0')
    weighted_mcp_sum = Decimal('0')
    total_records = len(rows)

    # Iterate through rows to calculate cumulative values
    for row in rows:
        prchs_bid_mw = Decimal(row.purchase_bid_mw) if row.purchase_bid_mw else Decimal('0')
        sell_bid_mw = Decimal(row.sell_bid_mw) if row.sell_bid_mw else Decimal('0')
        mcv_mw = Decimal(row.mcv_mw) if row.mcv_mw else Decimal('0')
        mcp_rs_mwh = Decimal(row.mcp_rs_mwh) if row.mcp_rs_mwh else Decimal('0')
        wt_mcp_rs_mwh = Decimal(row.weighted_mcp_rs_mwh) if row.weighted_mcp_rs_mwh else Decimal('0')

        purchase_bid_total += prchs_bid_mw
        sell_bid_total += sell_bid_mw
        mcv_total += mcv_mw
        mcp_sum += mcp_rs_mwh
        weighted_mcp_sum += (wt_mcp_rs_mwh * mcv_mw)/1000  # Calculate weighted sum of MCP

    # Calculate averages
    if total_records > 0:
        avg_mcp = mcp_sum / total_records
        if mcv_total > 0:
            wt_avg_mcp = weighted_mcp_sum / mcv_total
        else:
            wt_avg_mcp = Decimal('0')
    else:
        avg_mcp = Decimal('0')
        wt_avg_mcp = Decimal('0')

    # Return the cumulative metrics as a dictionary
    return {
        'Purchase Bid (MU)': purchase_bid_total/4,
        'Sell Bid (MU)': sell_bid_total/4,
        'MCV (MU)': mcv_total/4,
        'Avg. MCP (₹/KWh)': avg_mcp/1000,
        'Wt. Avg. MCP (₹/KWh)': wt_avg_mcp
    }


def calculate_cumulative_metrics_hpx_rtm(rows):
    # Initialize cumulative variables
    purchase_bid_total = Decimal('0')
    sell_bid_total = Decimal('0')
    mcv_total = Decimal('0')
    mcp_sum = Decimal('0')
    weighted_mcp_sum = Decimal('0')
    total_records = 0

    # Iterate through rows to calculate cumulative values
    for row in rows:
        prchs_bid_mw = Decimal(row.purchase_bid_mw) if row.purchase_bid_mw else Decimal('0')
        sell_bid_mw = Decimal(row.sell_bid_mw) if row.sell_bid_mw else Decimal('0')
        mcv_mw = Decimal(row.mcv_mw) if row.mcv_mw else Decimal('0')
        mcp_rs_mwh = Decimal(row.mcp_rs_mwh) if row.mcp_rs_mwh else Decimal('0')
        wt_mcp_rs_mwh = Decimal(row.mcp_rs_mwh) if row.mcp_rs_mwh else Decimal('0')
        if mcp_rs_mwh != "-" and float(mcp_rs_mwh) > 0.0:
            print(mcp_rs_mwh)
            total_records += 1

        purchase_bid_total += prchs_bid_mw
        sell_bid_total += sell_bid_mw
        mcv_total += mcv_mw
        mcp_sum += mcp_rs_mwh
        weighted_mcp_sum += (wt_mcp_rs_mwh * mcv_mw)/1000  # Calculate weighted sum of MCP
    # Calculate averages
    if total_records > 0:
        avg_mcp = mcp_sum  / total_records
        if mcv_total > 0:
            wt_avg_mcp = weighted_mcp_sum / mcv_total
        else:
            wt_avg_mcp = Decimal('0')
    else:
        avg_mcp = Decimal('0')
        wt_avg_mcp = Decimal('0')

    # Return the cumulative metrics as a dictionary
    return {
        'Purchase Bid (MU)': purchase_bid_total/4,
        'Sell Bid (MU)': sell_bid_total/4,
        'MCV (MU)': mcv_total/4,
        'Avg. MCP (₹/KWh)': avg_mcp/1000,
        'Wt. Avg. MCP (₹/KWh)': wt_avg_mcp
    }


def calculate_cumulative_metrics_pxil_rtm(rows):
    # Initialize cumulative variables
    purchase_bid_total = Decimal('0')
    sell_bid_total = Decimal('0')
    mcv_total = Decimal('0')
    mcp_sum = Decimal('0')
    weighted_mcp_sum = Decimal('0')
    total_records = len(rows)

    # Iterate through rows to calculate cumulative values
    for row in rows:
        prchs_bid_mw = Decimal(row.buy_bid_mwh) if row.buy_bid_mwh else Decimal('0')
        sell_bid_mw = Decimal(row.sell_bid_mwh) if row.sell_bid_mwh else Decimal('0')
        mcv_mw = Decimal(row.mcv_mwh) if row.mcv_mwh else Decimal('0')
        mcp_rs_mwh = Decimal(row.unconstraint_mcp_inr_mwh) if row.unconstraint_mcp_inr_mwh != "-" else Decimal('0')
        wt_mcp_rs_mwh = Decimal(row.unconstraint_mcp_inr_mwh) if row.unconstraint_mcp_inr_mwh != "-" else Decimal('0')

        purchase_bid_total += prchs_bid_mw
        sell_bid_total += sell_bid_mw
        mcv_total += mcv_mw
        mcp_sum += mcp_rs_mwh
        weighted_mcp_sum += (wt_mcp_rs_mwh * mcv_mw)/1000  # Calculate weighted sum of MCP

    # Calculate averages
    if total_records > 0:
        avg_mcp = mcp_sum / total_records
        if mcv_total > 0:
            wt_avg_mcp = weighted_mcp_sum / mcv_total
        else:
            wt_avg_mcp = Decimal('0')
    else:
        avg_mcp = Decimal('0')
        wt_avg_mcp = Decimal('0')

    # Return the cumulative metrics as a dictionary
    return {
        'Purchase Bid (MU)': purchase_bid_total/4,
        'Sell Bid (MU)': sell_bid_total/4,
        'MCV (MU)': mcv_total/4,
        'Avg. MCP (₹/KWh)': avg_mcp/1000,
        'Wt. Avg. MCP (₹/KWh)': wt_avg_mcp
    }


class Entry:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

def calculate_cumulative_report(data):
    cumulative_report = {
        "enrgy_met_mu": Decimal(0),
        "enrgy_shrtage_mu": Decimal(0),
        "max_demand_met_during_the_day_mw_from_nldc_scada": Decimal(0),
        "solar_gen_mu": Decimal(0),
        "demand_met_during_evening_peak_hrsmw_at_19_00_hrs_from_rldcs": Decimal(0),
        "peak_shrtage_mw": Decimal(0),
        "wind_gen_mu": Decimal(0),
        "energy_met_mu": Decimal(0)
    }

    for entry in data:
        cumulative_report["enrgy_shrtage_mu"] += Decimal(entry.enrgy_shrtage_mu)
        cumulative_report["max_demand_met_during_the_day_mw_from_nldc_scada"] += Decimal(entry.max_demand_met_during_the_day_mw_from_nldc_scada)
        cumulative_report["solar_gen_mu"] += Decimal(entry.solar_gen_mu)
        cumulative_report["demand_met_during_evening_peak_hrsmw_at_19_00_hrs_from_rldcs"] += Decimal(entry.demand_met_during_evening_peak_hrsmw_at_19_00_hrs_from_rldcs)
        cumulative_report["peak_shrtage_mw"] += Decimal(entry.peak_shrtage_mw)
        cumulative_report["wind_gen_mu"] += Decimal(entry.wind_gen_mu) if entry.wind_gen_mu != "-" else 0
        cumulative_report["energy_met_mu"] += Decimal(entry.enrgy_met_mu)
        
        

    return cumulative_report



# Fossile Fuels 

#   {
#     "date": "03-08-2023",
#     "hydro_gen_mu": "137.92",
#     "max_demand_met_during_the_day_mw_from_nldc_scada": "27865",
#     "regions": "ER",
#     "demand_met_during_evening_peak_hrsmw_at_19_00_hrs_from_rldcs": "25738",
#     "peak_shrtage_mw": "279",
#     "converted_date": {
#       "millisSinceEpoch": "1691020800000",
#       "daysSinceEpoch": 19572,
#       "year": 2023,
#       "month": 8,
#       "day": 3
#     },
#     "solar_gen_mu": "1.49",
#     "enrgy_shrtage_mu": "1.002",
#     "wind_gen_mu": "-",
#     "time_of_max_demand_met_from_nldc_scada": "21:18",
#     "enrgy_met_mu": "558.17",
#     "id": "ER03.08.23"
#   },
def calculate_cumulative_metrics_psp(data):
    cumulative_metrics = {}
    cumulative_metrics['date']= data[0].date

    cumulative_metrics['hydro_gen_mu'] = 0
    cumulative_metrics['solar_gen_mu'] = 0
    cumulative_metrics['wind_gen_mu'] = 0
    for i in data:
        cumulative_metrics['hydro_gen_mu'] += float(i.hydro_gen_mu) if i.hydro_gen_mu != "-" else 0
        cumulative_metrics['solar_gen_mu'] += float(i.solar_gen_mu) if i.solar_gen_mu != "-" else 0
        cumulative_metrics['wind_gen_mu'] += float(i.wind_gen_mu) if i.wind_gen_mu != "-" else 0

    #  round off the values
    cumulative_metrics['hydro_gen_mu'] = round(cumulative_metrics['hydro_gen_mu'])
    cumulative_metrics['solar_gen_mu'] = round(cumulative_metrics['solar_gen_mu'])
    cumulative_metrics['wind_gen_mu'] = round(cumulative_metrics['wind_gen_mu'])
    return cumulative_metrics

#   {
#     "date": "03-08-2023",
#     "hydro": "137.92",
#     "total": "715.63",
#     "res_solar_biomass": "2.52",
#     "converted_date": {
#       "millisSinceEpoch": "1691020800000",
#       "daysSinceEpoch": 19572,
#       "year": 2023,
#       "month": 8,
#       "day": 3
#     },
#     "coal": "575.19",
#     "lignite": "0",
#     "id": "ER03.08.23",
#     "gas_naptha_diesel": "0",
#     "nuclear": "0",
#     "region": "ER"
#   },
def calculate_cumulative_metrics_source_wise(data):
    cumulative_metrics = {
        
    }
    cumulative_metrics['res_solar_biomass'] = 0
    cumulative_metrics['nuclear'] = 0
    cumulative_metrics['share_of_non_fossil_fuel_hydro_nuclear_res_in_total_generation_perc'] = 0
    for i in data:
        cumulative_metrics['res_solar_biomass'] += float(i.res_solar_biomass) if i.res_solar_biomass != "-" else 0
        cumulative_metrics['nuclear'] += float(i.nuclear) if i.nuclear != "-" else 0
        try:
            cumulative_metrics['share_of_non_fossil_fuel_hydro_nuclear_res_in_total_generation_perc'] += float(i.share_of_non_fossil_fuel_hydro_nuclear_res_in_total_generation_perc) 
        except:
            pass
         
    cumulative_metrics['res_solar_biomass'] = round(cumulative_metrics['res_solar_biomass'])
    cumulative_metrics['nuclear'] = round(cumulative_metrics['nuclear'])
    cumulative_metrics['share_of_non_fossil_fuel_hydro_nuclear_res_in_total_generation_perc'] = round(cumulative_metrics['share_of_non_fossil_fuel_hydro_nuclear_res_in_total_generation_perc'])
    return cumulative_metrics



# Cross Border Trade

# [
#   {
#     "date": {
#       "millisSinceEpoch": "1714608000000",
#       "daysSinceEpoch": 19845,
#       "month": 5,
#       "day": 2,
#       "year": 2024
#     },
#     "country": "Myanmar",
#     "tgna_collextive_idam_pxil": 0,
#     "bilateral_total": 0,
#     "tgna_collextive_idam_iex": 0,
#     "tgna_collextive_rtm_pxil": 0,
#     "total": 0,
#     "tgna_collextive_rtm_iex": 0,
#     "gna_isgs_ppa": 0,
#     "tgna_collextive_rtm_hpx": 0,
#     "id": "2024-05-02Myanmar",
#     "tgna_collextive_idam_hpx": 0
#   },
#   {
#     "date": {
#       "millisSinceEpoch": "1714608000000",
#       "daysSinceEpoch": 19845,
#       "month": 5,
#       "day": 2,
#       "year": 2024
#     },
#     "country": "Total Export",
#     "tgna_collextive_idam_pxil": 0,
#     "bilateral_total": 0,
#     "tgna_collextive_idam_iex": 4.1,
#     "tgna_collextive_rtm_pxil": 0,
#     "total": 31.1,
#     "tgna_collextive_rtm_iex": 6.1,
#     "gna_isgs_ppa": 20.9,
#     "tgna_collextive_rtm_hpx": 0,
#     "id": "2024-05-02Total Export",
#     "tgna_collextive_idam_hpx": 0
#   },
#   {
#     "date": {
#       "millisSinceEpoch": "1714608000000",
#       "daysSinceEpoch": 19845,
#       "month": 5,
#       "day": 2,
#       "year": 2024
#     },
#     "country": "Bangladesh",
#     "tgna_collextive_idam_pxil": 0,
#     "bilateral_total": 0,
#     "tgna_collextive_idam_iex": 0,
#     "tgna_collextive_rtm_pxil": 0,
#     "total": 20.62,
#     "tgna_collextive_rtm_iex": 0,
#     "gna_isgs_ppa": 20.62,
#     "tgna_collextive_rtm_hpx": 0,
#     "id": "2024-05-02Bangladesh",
#     "tgna_collextive_idam_hpx": 0
#   },
#   {
#     "date": {
#       "millisSinceEpoch": "1714608000000",
#       "daysSinceEpoch": 19845,
#       "month": 5,
#       "day": 2,
#       "year": 2024
#     },
#     "country": "Nepal",
#     "tgna_collextive_idam_pxil": 0,
#     "bilateral_total": 0,
#     "tgna_collextive_idam_iex": 4.1,
#     "tgna_collextive_rtm_pxil": 0,
#     "total": 6.5,
#     "tgna_collextive_rtm_iex": 2.12,
#     "gna_isgs_ppa": 0.28,
#     "tgna_collextive_rtm_hpx": 0,
#     "id": "2024-05-02Nepal",
#     "tgna_collextive_idam_hpx": 0
#   },
#   {
#     "date": {
#       "millisSinceEpoch": "1714608000000",
#       "daysSinceEpoch": 19845,
#       "month": 5,
#       "day": 2,
#       "year": 2024
#     },
#     "country": "Bhutan",
#     "tgna_collextive_idam_pxil": 0,
#     "bilateral_total": 0,
#     "tgna_collextive_idam_iex": 0,
#     "tgna_collextive_rtm_pxil": 0,
#     "total": 3.98,
#     "tgna_collextive_rtm_iex": 3.98,
#     "gna_isgs_ppa": 0,
#     "tgna_collextive_rtm_hpx": 0,
#     "id": "2024-05-02Bhutan",
#     "tgna_collextive_idam_hpx": 0
#   }
# ]

def calculate_cross_border(data):
    cumulative_metrics = {
        "country": 0,
        "actual_mu": 0,
        "date": 0,
        "day_peak_mw": 0,
    }
    metrics = []
    print(data)
    for i in data:
        metrics.append({
            "country": i.country,
            "actual_mu": i.actual_mu,
            "date": i.date,
            "day_peak_mw": i.day_peak_mw
        })
    print(metrics)

    if len(metrics) == 0:
        raise Exception("No data available for cross border trade for the given date.")

    return metrics