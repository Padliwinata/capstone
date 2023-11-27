from fastapi import FastAPI
from pydantic import BaseModel


class Rekening(BaseModel):
    account_receivables_1: float
    sales_1: float
    cogs_1: float
    current_assets_1: float
    ppe_1: float
    depreciation_1: float
    sga_expense_1: float
    long_term_debt_1: float
    current_liabilities_1: float
    total_asset_1: float
    cash_1: float
    current_maturities_of_ltd_1: float
    income_tax_payable_1: float
    depreciation_and_amortization_1: float
    account_receivables_2: float
    sales_2: float
    cogs_2: float
    current_assets_2: float
    ppe_2: float
    depreciation_2: float
    sga_expense_2: float
    long_term_debt_2: float
    current_liabilities_2: float
    total_asset_2: float
    cash_2: float
    current_maturities_of_ltd_2: float
    income_tax_payable_2: float
    depreciation_and_amortization_2: float


app = FastAPI()

@app.post('/index')
def before_index(data: Rekening):
    dsri = (data.account_receivables_2 / data.sales_2) / (data.account_receivables_1 / data.sales_1)
    gmi = ((data.sales_1 - data.cogs_1)/data.sales_1) / ((data.sales_2 - data.cogs_2)/data.sales_2)
    aqi = (1 - (data.current_assets_2 + data.ppe_2)/data.total_asset_2) / (1 - (data.current_assets_1 + data.ppe_1)/data.total_asset_1)
    sgi = data.sales_2 / data.sales_1
    depi = (data.depreciation_1 / (data.depreciation_1 + data.ppe_1)) / (data.depreciation_1 / (data.depreciation_2 + data.ppe_2))
    sgai = (data.sga_expense_2 / data.sales_2) / (data.sga_expense_1 / data.sales_1)
    lvgi = ((data.long_term_debt_2 + data.current_liabilities_2) / data.total_asset_2) / ((data.long_term_debt_1 + data.current_liabilities_1) / data.total_asset_1)
    tata = ((data.current_assets_2 - data.current_assets_1) - (data.cash_2 - data.cash_1) - ((data.current_liabilities_2 - data.current_liabilities_1) - (data.current_maturities_of_ltd_2 - data.current_maturities_of_ltd_1) - (data.income_tax_payable_2 - data.income_tax_payable_1) - data.depreciation_and_amortization_2)) / data.total_asset_2
    result = -4.84 + (0.920 * dsri) + (0.528 * gmi) + (0.404 * aqi) + (0.892 * sgi) + (0.115 * depi) - (0.172 * sgai) - (0.327 * lvgi) + (4.679 * tata)
    return result

