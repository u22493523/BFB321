#This model calculates the EPQ, economic production quantity, which is essentially the EOQ, economic order quantity, for a company that manufactures its own goods.
#5.1 After changing the daily production rate to 150, the EPQ goes down because it takes less time to maufacture goods
#5.2 When P is 100000, the EPQ acts like the EOQ because your production is so fast that your goods are essentially manufactured instantly, which is similar to how EOQ views the delivery of goods: instantly. So they behave the same.

import math

annual_demand = 12000 # units per year
setup_cost = 50 # cost per production run, in Rand
holding_cost = 2 # cost per unit per year, in Rand
daily_demand_rate = 40 # units produced/sold per day
daily_production_rate = 100 # units your process can make per day

def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
    return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))

epq = calculate_epq(annual_demand, setup_cost, holding_cost,
                    daily_demand_rate, daily_production_rate)
print("Optimal production quantity:", round(epq, 2))

runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate

print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))

max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)
print("Maximum inventory level:", round(max_inventory, 2))


annual_demand = 12000 # units per year
setup_cost = 50 # cost per production run, in Rand
holding_cost = 2 # cost per unit per year, in Rand
daily_demand_rate = 40 # units produced/sold per day
daily_production_rate = 150 # units your process can make per day

def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
    return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))

epq = calculate_epq(annual_demand, setup_cost, holding_cost,
                    daily_demand_rate, daily_production_rate)
print("Optimal production quantity:", round(epq, 2))

runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate

print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))

max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)
print("Maximum inventory level:", round(max_inventory, 2))

annual_demand = 12000 # units per year
setup_cost = 50 # cost per production run, in Rand
holding_cost = 2 # cost per unit per year, in Rand
daily_demand_rate = 40 # units produced/sold per day
daily_production_rate = 100000 # units your process can make per day

def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
    return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))

epq = calculate_epq(annual_demand, setup_cost, holding_cost,
                    daily_demand_rate, daily_production_rate)
print("Optimal production quantity:", round(epq, 2))

runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate

print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))

max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)
print("Maximum inventory level:", round(max_inventory, 2))