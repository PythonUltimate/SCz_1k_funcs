import math


# basic economics

def total_revenue(price, quantity_demand):
    return price * quantity_demand


def marginal_revenue(delta_revenue, delta_quantity):
    return delta_revenue / delta_quantity


def average_revenue(total_revenue, total_quantity):
    return total_revenue / total_quantity


def total_costs(fixed_costs, variable_costs):
    return fixed_costs + variable_costs


def marginal_costs(delta_total_costs, delta_quantity_produced):
    return delta_total_costs / delta_quantity_produced


def average_costs(total_costs, total_quantity):
    return total_costs / total_quantity


def average_fixed_costs(fixed_costs, total_quantity):
    return fixed_costs / total_quantity


def average_variable_costs(variable_costs, total_quantity):
    return variable_costs / total_quantity


def total_profit(total_revenue, total_costs):
    return total_revenue - total_costs


def marginal_profit(marginal_revenue, marginal_costs):
    return marginal_revenue - marginal_costs


def economic_profit(accounting_profit, opportunity_cost):
    return accounting_profit - opportunity_cost


def accounting_profit(total_revenue, explicit_costs):
    return total_revenue - explicit_costs


def opportunity_cost(best_alt_not_chosen, chosen_option):
    return best_alt_not_chosen - chosen_option


def interest_capital(capital, interest_rate, time):
    return capital * interest_rate / 100 * time


def compound_interest(capital, interest_rate, time):
    return capital * (1 + interest_rate / 100) ** time


def price_demand_elasticity(delta_quantity_demanded, quantity_demanded, delta_price, price):
    return (delta_quantity_demanded / quantity_demanded) / (delta_price / price)


def mixed_price_demand_elasticity(delta_quantity_demanded_a, quantity_demanded_a, delta_price_b, price_b):
    return (delta_quantity_demanded_a / quantity_demanded_a) / (delta_price_b / price_b)


def income_demand_elasticity(delta_quantity_demanded, quantity_demanded, delta_income, income):
    return (delta_quantity_demanded / quantity_demanded) / (delta_income / income)


def price_supply_elasticity(delta_quantity_offered, quantity_offered, delta_price, price):
    return (delta_quantity_offered / quantity_offered) / (delta_price / price)


def marginal_utility(delta_utility, delta_input):
    return delta_utility / delta_input


def marginal_cost(delta_cost, delta_input):
    return delta_cost / delta_input


def gdp(c, i, g, ex, im):
    return c + i + g + ex - im


def real_gdp(nominal_gdp, deflator):
    return nominal_gdp / deflator


def gdp_growth(gdp_1, gdp_2):
    return (gdp_2 - gdp_1) / gdp_2


def gdp_factors_income(wages, interest, rent, remaining):
    return wages + interest + rent + remaining


def gdp_global_method(global_consumption, intermediate_consumption):
    return global_consumption - intermediate_consumption


def gdp_factor_prices(gdp, subsidies, indirect_taxes):
    return gdp - indirect_taxes + subsidies


def gnp(gdp, net_income_national_factors):
    return gdp + net_income_national_factors


def gnp_factor_prices(gdp, net_income_national_factors, subsidies, indirect_taxes):
    return gdp + net_income_national_factors - indirect_taxes + subsidies


def nnp(gnp, depreciation):
    return gnp - depreciation


def nnp_factor_prices(gnp, depreciation, subsidies, indirect_taxes):
    return gnp - depreciation + subsidies - indirect_taxes


def disposable_income(nnp_factor_prices, direct_taxes, retained_profits):
    return nnp_factor_prices - direct_taxes - retained_profits


def hdi(life_exp, avg_school, exp_school, log_gdp):
    return (life_exp * (avg_school + exp_school) / 2 * log_gdp) ** 1 / 3


def mew(gdp, leisure, unpaid_work, envir_damage):
    return gdp + leisure - unpaid_work - envir_damage


def cobb_douglass_production(technology, capital, labour, alpha):
    return technology * capital ** alpha * labour ** (1 - alpha)


def unemployment_rate(num_unemployed, active_on_labor_market):
    return num_unemployed / active_on_labor_market * 100


def employment_rate(total_employed, workforce):
    return total_employed / workforce * 100


def labor_force_participation(total_employed, work_seekers, work_age_population):
    return (total_employed + work_seekers) * 100 / work_age_population


def keynesian_multiplier(mpc):
    return 1 / (1 - mpc)


def macro_consumption_function(income, taxes, autonomous_consumption, mpc):
    return autonomous_consumption + mpc * (income - taxes)


def money_multiplier(reserve_ratio):
    return 1 / reserve_ratio


def government_multiplier(mpc, delta_gov_spending):
    return delta_gov_spending / (1 - mpc)


def investment_multiplier(mps, delta_investments):
    return delta_investments / mps


def cpi(costs_year1, costs_base_year):
    return costs_year1 / costs_base_year


def inflation_rate(delta_cpi, cpi_last_year):
    return delta_cpi / cpi_last_year * 100


def real_interest_rate(interest_rate, antic_inflation):
    return (1 + interest_rate) / (1 + antic_inflation) - 1


def money_from_fischer_equation(velocity, price_level, gdp):
    return price_level * gdp / velocity


def roi(taxed_oper_profit, investment_value):
    return taxed_oper_profit / investment_value * 100


def roe(net_profit, own_capital_input):
    return net_profit / own_capital_input * 100


def roa(net_profit, total_assets):
    return net_profit / total_assets


def gross_profit_margin(gross_profit, net_sales):
    return gross_profit / net_sales


def operating_profit_margin(operating_profit, net_sales):
    return operating_profit / net_sales


def ebit_margin(ebit, net_sales):
    return ebit / net_sales


def net_profit_margin(net_profit, net_sales):
    return net_profit / net_sales


def asset_turnover(net_sales, total_sales):
    return net_sales / total_sales


def fixed_asset_turnover(net_sales, fixed_assets):
    return net_sales / fixed_assets


def price_earnings_ratio(stock_price, earning_per_share):
    return stock_price / earning_per_share


def reverse_pe_ratio(earning_per_share, stock_price):
    return earning_per_share / stock_price


def return_period(input, final_value, depreciation, avg_year_net_profit):
    return (input - final_value) / (depreciation + avg_year_net_profit)


def npv(positive_cash_flow, negative_cash_flow, discount_rate, reinvestment_rate, time_periods, investment_time):
    return positive_cash_flow * (1 + reinvestment_rate) ** (investment_time - time_periods) / (
            1 + discount_rate) ** time_periods - negative_cash_flow


def current_liquidity(current_assets, current_liabilities):
    return current_assets / current_liabilities


def liquidity_quick_ratio(current_assets, inventory, current_liabilities):
    return (current_assets - inventory) / current_liabilities


def leverage_debt_ratio(total_liabilities, total_assets):
    return total_liabilities / total_assets


def leverage_debt_interest_ratio(total_liabilities, minority_interest, total_assets):
    return (total_liabilities + minority_interest) / total_assets


def debt_to_worth_ratio(total_liabilities, shareholders_equity):
    return total_liabilities / shareholders_equity


def equity_ratio(shareholders_equity, total_assets):
    return shareholders_equity / total_assets


def debt_to_tangible_net_worth(total_liabilities, tangible_net_worth):
    return total_liabilities / tangible_net_worth


def interest_coverage(ebit, interest_expense):
    return ebit / interest_expense


def fixed_charge_coverage(ebit, interest_expense, cmltd):
    return ebit / (interest_expense + cmltd)


def cash_flow_coverage(net_income, depreciation, cmltd):
    return (net_income + depreciation) / cmltd


def operating_cashflow_ratio(operating_cashflow, current_liabilities):
    return operating_cashflow / current_liabilities


def gross_asset_rotation(net_sales, total_assets):
    return net_sales / total_assets


def dividend_yield(dividend_per_share, market_price_per_share):
    return dividend_per_share / market_price_per_share
