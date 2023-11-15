from fastapi import FastAPI
from pydantic import BaseModel


class Rekening(BaseModel):
    revenue: float
    cost_goods_sold: float
    sgae: float
    depreciation: float
    net_income_continuing_operations: float
    accounts_receiveables: float
    current_assets: float
    ppe: float
    securities: float
    total_assets: float
    current_liabilities: float
    total_long_term_debt: float
    cash_flow_from_operations: float


app = FastAPI()

@app.post('/index')
def before_index(data: Rekening):
    pass

